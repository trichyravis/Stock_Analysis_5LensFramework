
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
            price_hist = ticker.history(period=period)
            
            if price_hist.empty:
                return None, {}
            
            info = ticker.info
            return price_hist, info
        
        except Exception as e:
            print(f"Error fetching data for {symbol}: {e}")
            return None, {}
    
    @staticmethod
    def fetch_market_index(index_symbol: str = "^NSEI", period: str = "1y") -> Optional[pd.DataFrame]:
        """
        Fetch market index data (Nifty 50) with retry logic
        
        Args:
            index_symbol: Index symbol (default: ^NSEI for NSE)
            period: Time period
        
        Returns:
            Price history DataFrame or None
        """
        tickers_to_try = [
            "^NSEI",           # Nifty 50 (primary)
            "^BSESN",          # BSE Sensex (fallback)
            "NIFTYBEES.NS"     # Nifty ETF (fallback)
        ]
        
        for ticker in tickers_to_try:
            max_retries = 3
            
            for attempt in range(max_retries):
                try:
                    print(f"[Market Index] [{ticker}] Fetch attempt {attempt + 1}/{max_retries}")
                    
                    index = yf.Ticker(ticker)
                    market_data = index.history(period=period)
                    
                    if market_data is not None and not market_data.empty:
                        print(f"[Market Index] [{ticker}] ✅ SUCCESS! Got {len(market_data)} rows")
                        return market_data
                    
                    print(f"[Market Index] [{ticker}] Empty or None data")
                    if attempt < max_retries - 1:
                        time.sleep(random.uniform(2, 5))
                        
                except Exception as e:
                    print(f"[Market Index] [{ticker}] Error ({type(e).__name__}): {str(e)[:50]}")
                    if attempt < max_retries - 1:
                        time.sleep(random.uniform(3, 7))
            
            print(f"[Market Index] [{ticker}] Failed after {max_retries} attempts\n")
        
        print("[Market Index] ⚠️ Could not fetch market index from any source")
        return None
    
    @staticmethod
    def calculate_beta(
        symbol: str,
        stock_data: pd.DataFrame,
        market_data: pd.DataFrame
    ) -> Optional[float]:
        """
        Calculate stock beta relative to market index with robust data alignment.
        
        KEY FIX: Strip timezones before alignment to handle timezone mismatches
        between stock and market index data.
        
        Args:
            symbol: Stock symbol for logging
            stock_data: Pre-fetched historical price data for the stock
            market_data: Pre-fetched historical price data for the index (Nifty 50)
        
        Returns:
            Beta value (float) or None if calculation fails
            
        Beta Interpretation:
            β > 1.0:  Stock is more volatile than market (higher risk)
            β = 1.0:  Stock moves with the market
            β < 1.0:  Stock is less volatile than market (lower risk)
            
        Example:
            TCS: β ≈ 1.15 (IT sector, higher volatility)
            HDFCBANK: β ≈ 0.95 (Banks, market-like)
            NESTLEIND: β ≈ 0.75 (FMCG, defensive)
        """
        try:
            # Validate inputs
            if stock_data is None or market_data is None:
                print(f"[Beta] [{symbol}] ❌ None input (stock_data or market_data)")
                return None
            
            if stock_data.empty or market_data.empty:
                print(f"[Beta] [{symbol}] ❌ Empty input (stock_data or market_data)")
                return None
            
            print(f"[Beta] [{symbol}] Starting calculation...")
            print(f"[Beta] [{symbol}] Stock data: {len(stock_data)} rows")
            print(f"[Beta] [{symbol}] Market data: {len(market_data)} rows")
            
            # 1. Strip timezones and extract Close prices
            # This fixes date alignment issues caused by timezone mismatches
            # Stock data might be 00:00:00+00:00 while market is 00:00:00+05:30
            # tz_localize(None) makes both timezone-naive so they align properly
            s_prices = stock_data['Close'].tz_localize(None)
            m_prices = market_data['Close'].tz_localize(None)
            
            # 2. Compute daily percentage returns
            s_returns = s_prices.pct_change().dropna()
            m_returns = m_prices.pct_change().dropna()
            
            print(f"[Beta] [{symbol}] Stock returns: {len(s_returns)} points")
            print(f"[Beta] [{symbol}] Market returns: {len(m_returns)} points")
            
            # 3. Align the data on the same dates
            df_returns = pd.concat([s_returns, m_returns], axis=1, join="inner")
            df_returns.columns = ['stock', 'market']
            
            aligned_count = len(df_returns)
            print(f"[Beta] [{symbol}] Aligned data: {aligned_count} points")
            
            # 4. Validate aligned data
            if aligned_count < 30:
                print(f"[Beta] [{symbol}] ❌ Insufficient aligned data ({aligned_count} < 30 required)")
                return None
            
            # 5. Calculate Beta using Covariance / Variance
            # Beta = Cov(stock_returns, market_returns) / Var(market_returns)
            covariance_matrix = np.cov(df_returns['stock'], df_returns['market'])
            covariance = covariance_matrix[0, 1]
            market_variance = covariance_matrix[1, 1]
            
            # Validate variance
            if market_variance == 0:
                print(f"[Beta] [{symbol}] ❌ Market variance is zero")
                return None
            
            # Calculate and validate beta
            beta = covariance / market_variance
            
            # Check for invalid values
            if np.isnan(beta) or np.isinf(beta):
                print(f"[Beta] [{symbol}] ❌ Invalid beta value (NaN or Inf)")
                return None
            
            # Return rounded beta
            beta_rounded = round(float(beta), 4)
            print(f"[Beta] [{symbol}] ✅ SUCCESS! Beta = {beta_rounded}")
            return beta_rounded
            
        except Exception as e:
            error_type = type(e).__name__
            error_msg = str(e)[:80]
            print(f"[Beta] [{symbol}] ❌ Error ({error_type}): {error_msg}")
            return None
    
    @staticmethod
    def extract_stock_data(info: Dict, price_hist: pd.DataFrame) -> Dict:
        """Extract key stock data"""
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
        """Extract financial metrics with multiple fallback approaches"""
        try:
            metrics = {}
            
            # Profitability Metrics
            metrics['roe'] = info.get('returnOnEquity')
            metrics['npm'] = info.get('profitMargins')
            metrics['roa'] = info.get('returnOnAssets')
            metrics['roic'] = info.get('returnOnCapital')
            
            # Debt to Equity Ratio
            debt_to_equity = info.get('debtToEquity')
            if debt_to_equity is None:
                try:
                    total_debt = info.get('totalDebt')
                    total_equity = info.get('totalEquity')
                    if total_debt and total_equity and total_equity > 0:
                        debt_to_equity = total_debt / total_equity
                except:
                    pass
            metrics['debt_to_equity'] = debt_to_equity
            
            # Current Ratio
            current_ratio = info.get('currentRatio')
            if current_ratio is None:
                try:
                    current_assets = info.get('currentAssets')
                    current_liabilities = info.get('currentLiabilities')
                    if current_assets and current_liabilities and current_liabilities > 0:
                        current_ratio = current_assets / current_liabilities
                except:
                    pass
            metrics['current_ratio'] = current_ratio
            
            # Interest Coverage
            interest_coverage = info.get('interestCoverage')
            if interest_coverage is None:
                try:
                    earnings = info.get('ebit') or info.get('operatingIncome')
                    interest_expense = info.get('interestExpense')
                    if earnings and interest_expense and interest_expense > 0:
                        interest_coverage = earnings / interest_expense
                except:
                    pass
            metrics['interest_coverage'] = interest_coverage
            
            # Growth Metrics
            metrics['revenue_growth_yoy'] = info.get('revenueGrowth')
            metrics['earnings_growth_yoy'] = info.get('earningsGrowth')
            metrics['peg_ratio'] = info.get('pegRatio')
            
            return metrics
            
        except Exception as e:
            print(f"Error extracting financial metrics: {e}")
            return {
                'roe': None, 'npm': None, 'roa': None, 'roic': None,
                'debt_to_equity': None, 'current_ratio': None,
                'interest_coverage': None, 'revenue_growth_yoy': None,
                'earnings_growth_yoy': None, 'peg_ratio': None,
            }
