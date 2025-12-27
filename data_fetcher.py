
import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import requests
from typing import Dict, Tuple, Optional
import time
import random

class DataFetcher:
    """Fetch and process stock data from yfinance"""
    
    NIFTY50_REGISTRY = {
        'ADANIPORTS': {'symbol': 'ADANIPORTS.NS', 'sector': 'Ports & Services'},
        'ASIANPAINT': {'symbol': 'ASIANPAINT.NS', 'sector': 'Chemicals'},
        'AXISBANK': {'symbol': 'AXISBANK.NS', 'sector': 'Banks'},
        'BAJAJFINSV': {'symbol': 'BAJAJFINSV.NS', 'sector': 'Financial Services'},
        'BAJAJFS': {'symbol': 'BAJAJFS.NS', 'sector': 'Financial Services'},
        'BAJAJ-AUTO': {'symbol': 'BAJAJ-AUTO.NS', 'sector': 'Automobiles'},
        'BPCL': {'symbol': 'BPCL.NS', 'sector': 'Oil & Gas'},
        'BHARTIARTL': {'symbol': 'BHARTIARTL.NS', 'sector': 'Telecommunications'},
        'BRITANNIA': {'symbol': 'BRITANNIA.NS', 'sector': 'FMCG'},
        'CIPLA': {'symbol': 'CIPLA.NS', 'sector': 'Pharmaceuticals'},
        'COALINDIA': {'symbol': 'COALINDIA.NS', 'sector': 'Metals & Mining'},
        'COLPAL': {'symbol': 'COLPAL.NS', 'sector': 'FMCG'},
        'DRREDDY': {'symbol': 'DRREDDY.NS', 'sector': 'Pharmaceuticals'},
        'EICHERMOT': {'symbol': 'EICHERMOT.NS', 'sector': 'Automobiles'},
        'GAIL': {'symbol': 'GAIL.NS', 'sector': 'Oil & Gas'},
        'GRASIM': {'symbol': 'GRASIM.NS', 'sector': 'Chemicals'},
        'HCLTECH': {'symbol': 'HCLTECH.NS', 'sector': 'IT'},
        'HDFCBANK': {'symbol': 'HDFCBANK.NS', 'sector': 'Banks'},
        'HEROMOTOCO': {'symbol': 'HEROMOTOCO.NS', 'sector': 'Automobiles'},
        'HINDALCO': {'symbol': 'HINDALCO.NS', 'sector': 'Metals & Mining'},
        'HINDUNILVR': {'symbol': 'HINDUNILVR.NS', 'sector': 'FMCG'},
        'ICICIBANK': {'symbol': 'ICICIBANK.NS', 'sector': 'Banks'},
        'INDIGO': {'symbol': 'INDIGO.NS', 'sector': 'Airlines'},
        'INFY': {'symbol': 'INFY.NS', 'sector': 'IT'},
        'IOCL': {'symbol': 'IOCL.NS', 'sector': 'Oil & Gas'},
        'ITC': {'symbol': 'ITC.NS', 'sector': 'Diversified'},
        'JSWSTEEL': {'symbol': 'JSWSTEEL.NS', 'sector': 'Metals & Mining'},
        'KOTAKBANK': {'symbol': 'KOTAKBANK.NS', 'sector': 'Banks'},
        'LT': {'symbol': 'LT.NS', 'sector': 'Engineering'},
        'LTIM': {'symbol': 'LTIM.NS', 'sector': 'IT'},
        'MARUTI': {'symbol': 'MARUTI.NS', 'sector': 'Automobiles'},
        'MAXHEALTH': {'symbol': 'MAXHEALTH.NS', 'sector': 'Healthcare'},
        'MINDTREE': {'symbol': 'MINDTREE.NS', 'sector': 'IT'},
        'NESTLEIND': {'symbol': 'NESTLEIND.NS', 'sector': 'FMCG'},
        'NTPC': {'symbol': 'NTPC.NS', 'sector': 'Power'},
        'ONGC': {'symbol': 'ONGC.NS', 'sector': 'Oil & Gas'},
        'POWERGRID': {'symbol': 'POWERGRID.NS', 'sector': 'Power'},
        'RELIANCE': {'symbol': 'RELIANCE.NS', 'sector': 'Oil & Gas'},
        'SBICARD': {'symbol': 'SBICARD.NS', 'sector': 'Financial Services'},
        'SBILIFE': {'symbol': 'SBILIFE.NS', 'sector': 'Financial Services'},
        'SBIN': {'symbol': 'SBIN.NS', 'sector': 'Banks'},
        'SUNPHARMA': {'symbol': 'SUNPHARMA.NS', 'sector': 'Pharmaceuticals'},
        'TCS': {'symbol': 'TCS.NS', 'sector': 'IT'},
        'TECHM': {'symbol': 'TECHM.NS', 'sector': 'IT'},
        'TITAN': {'symbol': 'TITAN.NS', 'sector': 'Consumer Discretionary'},
        'TRENT': {'symbol': 'TRENT.NS', 'sector': 'Retail'},
        'ULTRACEMCO': {'symbol': 'ULTRACEMCO.NS', 'sector': 'Cement'},
        'WIPRO': {'symbol': 'WIPRO.NS', 'sector': 'IT'},
    }
    
    @staticmethod
    def get_nifty50_registry() -> Dict:
        """Return Nifty 50 registry"""
        return DataFetcher.NIFTY50_REGISTRY
    
    @staticmethod
    def fetch_stock_data(symbol: str, period: str = "1y") -> Tuple[Optional[pd.DataFrame], Dict]:
        """
        Fetch stock data from yfinance
        
        Args:
            symbol: Stock symbol (e.g., 'INFY.NS')
            period: Time period (1y, 2y, 5y)
        
        Returns:
            Tuple of (price_history DataFrame, info dict)
        """
        try:
            ticker = yf.Ticker(symbol)
            
            # Fetch historical data
            price_hist = ticker.history(period=period)
            
            if price_hist.empty:
                return None, {}
            
            # Fetch info
            info = ticker.info
            
            return price_hist, info
        
        except Exception as e:
            print(f"Error fetching data for {symbol}: {e}")
            return None, {}
    
    @staticmethod
    def fetch_market_index(index_symbol: str = "^NSEI", period: str = "1y") -> Optional[pd.DataFrame]:
        """
        Fetch market index data (Nifty 50)
        With retry logic, timeout, and fallback tickers
        
        Args:
            index_symbol: Index symbol (default: ^NSEI for NSE)
            period: Time period
        
        Returns:
            Price history DataFrame
        """
        # Try multiple tickers for better reliability
        tickers_to_try = [
            "^NSEI",           # Primary: Nifty 50 (NSE)
            "^BSESN",          # Fallback 1: BSE Sensex
            "NIFTYBEES.NS"     # Fallback 2: Nifty ETF
        ]
        
        for ticker in tickers_to_try:
            max_retries = 3
            
            for attempt in range(max_retries):
                try:
                    print(f"\n[Market Data] [{ticker}] Fetch attempt {attempt + 1}/{max_retries}")
                    
                    index = yf.Ticker(ticker)
                    market_data = index.history(period=period)
                    
                    # Validate data
                    if market_data is None:
                        print(f"[Market Data] [{ticker}] ❌ No data returned (None)")
                        if attempt < max_retries - 1:
                            wait_time = random.uniform(2, 5)
                            print(f"[Market Data] [{ticker}] Waiting {wait_time:.1f}s before retry...")
                            time.sleep(wait_time)
                        continue
                    
                    if market_data.empty:
                        print(f"[Market Data] [{ticker}] ❌ Empty dataframe")
                        if attempt < max_retries - 1:
                            wait_time = random.uniform(2, 5)
                            print(f"[Market Data] [{ticker}] Waiting {wait_time:.1f}s before retry...")
                            time.sleep(wait_time)
                        continue
                    
                    # Success!
                    print(f"[Market Data] [{ticker}] ✅ SUCCESS! Got {len(market_data)} rows")
                    return market_data
                    
                except Exception as e:
                    error_type = type(e).__name__
                    error_msg = str(e)[:80]  # First 80 chars of error
                    print(f"[Market Data] [{ticker}] ❌ Error ({error_type}): {error_msg}")
                    
                    if attempt < max_retries - 1:
                        wait_time = random.uniform(3, 7)
                        print(f"[Market Data] [{ticker}] Waiting {wait_time:.1f}s before retry...")
                        time.sleep(wait_time)
                    else:
                        print(f"[Market Data] [{ticker}] Failed after {max_retries} attempts")
            
            print(f"[Market Data] [{ticker}] ⚠️ Gave up on this ticker, trying next...\n")
        
        print("[Market Data] ⚠️ Could not fetch any market index data - Beta will be N/A")
        return None
    
    @staticmethod
    def calculate_beta(
        symbol: str,
        period: str = "1y",
        index_symbol: str = "^NSEI"
    ) -> Optional[float]:
        """
        Calculate stock beta relative to market index.
        
        Beta measures systematic risk - how much the stock moves relative to market.
        Beta = 1.0 means stock moves with market
        Beta > 1.0 means stock is more volatile than market
        Beta < 1.0 means stock is less volatile than market
        
        Args:
            symbol: Stock symbol (e.g., 'INFY.NS')
            period: Time period (e.g., '6mo', '1y', '2y', '5y')
            index_symbol: Market index ticker (default: '^NSEI' for Nifty 50)
        
        Returns:
            Beta value (float) or None if cannot be computed
            
        Example:
            beta = DataFetcher.calculate_beta('INFY.NS', '1y', '^NSEI')
            if beta is not None:
                print(f"Beta: {beta}x")
            else:
                print("Beta unavailable")
        """
        try:
            print(f"\n[Beta] [{symbol}] Calculating beta for {period}...")
            
            # Fetch stock data
            print(f"[Beta] [{symbol}] Fetching stock data...")
            stock_ticker = yf.Ticker(symbol)
            stock_data = stock_ticker.history(period=period)
            if stock_data is None or stock_data.empty:
                print(f"[Beta] [{symbol}] ❌ No stock data")
                return None
            
            # Fetch market index data (with retry logic)
            print(f"[Beta] [{symbol}] Fetching market index data ({index_symbol})...")
            market_data = DataFetcher.fetch_market_index(index_symbol, period)
            if market_data is None or market_data.empty:
                print(f"[Beta] [{symbol}] ❌ No market index data")
                return None
            
            # Extract prices
            stock_prices = stock_data['Close']
            market_prices = market_data['Close']
            
            # Compute daily returns
            stock_returns = stock_prices.pct_change()
            market_returns = market_prices.pct_change()
            
            # Align dates and combine
            returns = pd.concat([stock_returns, market_returns], axis=1, join="inner")
            returns.columns = ['stock', 'market']
            returns.dropna(inplace=True)
            
            # Validate data points
            if len(returns) < 30:
                print(f"[Beta] [{symbol}] ❌ Insufficient data ({len(returns)} points, need 30+)")
                return None
            
            print(f"[Beta] [{symbol}] Computing beta ({len(returns)} aligned data points)...")
            
            # Beta = Cov(stock, market) / Var(market)
            cov = np.cov(returns['stock'], returns['market'])[0, 1]
            var = np.var(returns['market'])
            
            if var == 0:
                print(f"[Beta] [{symbol}] ❌ Market variance is zero")
                return None
            
            beta = cov / var
            beta_rounded = round(beta, 4)
            
            # Check for reasonable beta value
            if np.isnan(beta_rounded) or np.isinf(beta_rounded):
                print(f"[Beta] [{symbol}] ❌ Invalid beta value")
                return None
            
            print(f"[Beta] [{symbol}] ✅ SUCCESS! Beta = {beta_rounded}")
            return beta_rounded
            
        except Exception as e:
            error_type = type(e).__name__
            error_msg = str(e)[:80]
            print(f"[Beta] [{symbol}] ❌ Error ({error_type}): {error_msg}")
            return None
    
    @staticmethod
    def extract_stock_data(info: Dict, price_hist: pd.DataFrame) -> Dict:
        """
        Extract key stock data
        
        Args:
            info: Stock info dictionary from yfinance
            price_hist: Historical price data
        
        Returns:
            Dictionary with key metrics
        """
        try:
            current_price = info.get('currentPrice') or price_hist['Close'].iloc[-1]
            
            return {
                'current_price': current_price,
                'pe_ratio': info.get('trailingPE'),
                'pb_ratio': info.get('priceToBook'),
                'ps_ratio': info.get('priceToSalesTrailing12Months'),
                'dividend_yield': info.get('dividendYield'),
                'market_cap': info.get('marketCap'),
                '52_week_high': info.get('fiftyTwoWeekHigh'),
                '52_week_low': info.get('fiftyTwoWeekLow'),
                '52_week_change': info.get('fiftyTwoWeekChangePercent'),
            }
        except Exception as e:
            print(f"Error extracting stock data: {e}")
            return {}
    
    @staticmethod
    def extract_financial_metrics(info: Dict) -> Dict:
        """
        Extract financial metrics with multiple fallback approaches
        Handles missing data gracefully
        
        Args:
            info: Stock info dictionary from yfinance
        
        Returns:
            Dictionary with financial metrics
        """
        try:
            metrics = {}
            
            # ROE (Return on Equity) - Primary source
            metrics['roe'] = info.get('returnOnEquity')
            
            # NPM (Net Profit Margin) - Primary source
            metrics['npm'] = info.get('profitMargins')
            
            # ROA (Return on Assets) - Primary source
            metrics['roa'] = info.get('returnOnAssets')
            
            # ROIC (Return on Invested Capital) - Primary source
            metrics['roic'] = info.get('returnOnCapital')
            
            # Debt to Equity Ratio - Multiple approaches
            debt_to_equity = None
            
            # Approach 1: Direct from info
            if debt_to_equity is None:
                debt_to_equity = info.get('debtToEquity')
            
            # Approach 2: Calculate from total debt and equity
            if debt_to_equity is None:
                try:
                    total_debt = info.get('totalDebt')
                    total_equity = info.get('totalEquity')
                    book_value = info.get('bookValue')
                    shares_outstanding = info.get('sharesOutstanding', 1)
                    
                    if total_debt and total_equity and total_equity > 0:
                        debt_to_equity = total_debt / total_equity
                    elif total_debt and book_value and shares_outstanding and book_value * shares_outstanding > 0:
                        debt_to_equity = total_debt / (book_value * shares_outstanding)
                except Exception as e:
                    print(f"Error calculating D/E ratio: {e}")
            
            metrics['debt_to_equity'] = debt_to_equity
            
            # Current Ratio - Multiple approaches
            current_ratio = None
            
            # Approach 1: Direct from info
            if current_ratio is None:
                current_ratio = info.get('currentRatio')
            
            # Approach 2: Calculate from current assets and liabilities
            if current_ratio is None:
                try:
                    current_assets = info.get('currentAssets')
                    current_liabilities = info.get('currentLiabilities')
                    
                    if current_assets and current_liabilities and current_liabilities > 0:
                        current_ratio = current_assets / current_liabilities
                except Exception as e:
                    print(f"Error calculating Current ratio: {e}")
            
            metrics['current_ratio'] = current_ratio
            
            # Interest Coverage - Multiple approaches
            interest_coverage = None
            
            # Approach 1: Direct from info
            if interest_coverage is None:
                interest_coverage = info.get('interestCoverage')
            
            # Approach 2: Calculate from EBIT and interest expense
            if interest_coverage is None:
                try:
                    ebit = info.get('ebit')
                    operating_income = info.get('operatingIncome')
                    interest_expense = info.get('interestExpense')
                    
                    earnings = ebit or operating_income
                    
                    if earnings and interest_expense and interest_expense > 0:
                        interest_coverage = earnings / interest_expense
                except Exception as e:
                    print(f"Error calculating Interest coverage: {e}")
            
            metrics['interest_coverage'] = interest_coverage
            
            # Revenue Growth YoY
            metrics['revenue_growth_yoy'] = info.get('revenueGrowth')
            
            # Earnings Growth YoY
            metrics['earnings_growth_yoy'] = info.get('earningsGrowth')
            
            # PEG Ratio
            metrics['peg_ratio'] = info.get('pegRatio')
            
            return metrics
            
        except Exception as e:
            print(f"Error extracting financial metrics: {e}")
            return {
                'roe': None,
                'npm': None,
                'roa': None,
                'roic': None,
                'debt_to_equity': None,
                'current_ratio': None,
                'interest_coverage': None,
                'revenue_growth_yoy': None,
                'earnings_growth_yoy': None,
                'peg_ratio': None,
            }
