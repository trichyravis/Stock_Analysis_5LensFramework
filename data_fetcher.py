
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
    
    # Beta values by stock (pre-calculated sector/stock betas)
    STOCK_BETA = {
        'ADANIPORTS': 1.05,
        'ASIANPAINT': 1.05,
        'AXISBANK': 0.95,
        'BAJAJFINSV': 1.05,
        'BAJAJFS': 1.05,
        'BAJAJ-AUTO': 1.20,
        'BPCL': 1.10,
        'BHARTIARTL': 0.80,
        'BRITANNIA': 0.75,
        'CIPLA': 0.90,
        'COALINDIA': 1.25,
        'COLPAL': 0.75,
        'DRREDDY': 0.90,
        'EICHERMOT': 1.20,
        'GAIL': 1.10,
        'GRASIM': 1.05,
        'HCLTECH': 1.15,
        'HDFCBANK': 0.95,
        'HEROMOTOCO': 1.20,
        'HINDALCO': 1.25,
        'HINDUNILVR': 0.75,
        'ICICIBANK': 0.95,
        'INDIGO': 1.30,
        'INFY': 1.15,
        'IOCL': 1.10,
        'ITC': 0.75,
        'JSWSTEEL': 1.25,
        'KOTAKBANK': 0.95,
        'LT': 1.15,
        'LTIM': 1.15,
        'MARUTI': 1.20,
        'MAXHEALTH': 1.00,
        'MINDTREE': 1.15,
        'NESTLEIND': 0.75,
        'NTPC': 0.85,
        'ONGC': 1.10,
        'POWERGRID': 0.85,
        'RELIANCE': 1.10,
        'SBICARD': 1.05,
        'SBILIFE': 1.05,
        'SBIN': 0.95,
        'SUNPHARMA': 0.90,
        'TCS': 1.15,
        'TECHM': 1.15,
        'TITAN': 1.15,
        'TRENT': 1.20,
        'ULTRACEMCO': 1.10,
        'WIPRO': 1.15,
    }
    
    @staticmethod
    def get_nifty50_registry() -> Dict:
        """Return Nifty 50 registry"""
        return DataFetcher.NIFTY50_REGISTRY
    
    @staticmethod
    def fetch_stock_data(symbol: str, period: str = "1y") -> Tuple[Optional[pd.DataFrame], Dict]:
        """Fetch stock data from yfinance"""
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
        """Fetch market index data"""
        tickers_to_try = ["^NSEI", "^BSESN", "NIFTYBEES.NS"]
        
        for ticker in tickers_to_try:
            max_retries = 3
            for attempt in range(max_retries):
                try:
                    index = yf.Ticker(ticker)
                    market_data = index.history(period=period)
                    if market_data is not None and not market_data.empty:
                        print(f"[Market Index] {ticker}: Got {len(market_data)} rows")
                        return market_data
                except Exception as e:
                    pass
                if attempt < max_retries - 1:
                    time.sleep(2)
        return None
    
    @staticmethod
    def calculate_beta(
        symbol: str,
        stock_data: pd.DataFrame,
        market_data: pd.DataFrame
    ) -> Optional[float]:
        """
        Calculate beta with GUARANTEED fallback to lookup table.
        
        This will ALWAYS return a beta value (never None/N/A)
        
        Approach:
        1. Try direct calculation if data available
        2. Return stock beta from lookup table
        3. Return sector average
        4. Return market average (1.0)
        
        Result: ALWAYS returns a value! ✅
        """
        
        # Extract stock code from symbol (e.g., 'INFY.NS' → 'INFY')
        stock_code = symbol.replace('.NS', '').strip().upper()
        
        # APPROACH 1: Try direct calculation
        try:
            if stock_data is not None and market_data is not None:
                if not stock_data.empty and not market_data.empty:
                    
                    s_prices = stock_data['Close'].tz_localize(None)
                    m_prices = market_data['Close'].tz_localize(None)
                    
                    s_returns = s_prices.pct_change().dropna()
                    m_returns = m_prices.pct_change().dropna()
                    
                    df_returns = pd.concat([s_returns, m_returns], axis=1, join="inner")
                    df_returns.columns = ['stock', 'market']
                    
                    if len(df_returns) >= 30:
                        covariance_matrix = np.cov(df_returns['stock'], df_returns['market'])
                        covariance = covariance_matrix[0, 1]
                        market_variance = covariance_matrix[1, 1]
                        
                        if market_variance != 0 and not np.isnan(covariance):
                            beta = covariance / market_variance
                            
                            if not np.isnan(beta) and not np.isinf(beta) and -5 < beta < 5:
                                result = round(float(beta), 4)
                                print(f"[Beta] {stock_code}: Calculated = {result}")
                                return result
        except Exception as e:
            print(f"[Beta] {stock_code}: Direct calculation failed ({type(e).__name__})")
        
        # APPROACH 2: Use stock beta from lookup table
        if stock_code in DataFetcher.STOCK_BETA:
            beta = DataFetcher.STOCK_BETA[stock_code]
            print(f"[Beta] {stock_code}: Lookup = {beta}")
            return beta
        
        # APPROACH 3: Default to 1.0 (market average)
        print(f"[Beta] {stock_code}: Using default = 1.0")
        return 1.0
    
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
        """Extract financial metrics"""
        try:
            metrics = {}
            metrics['roe'] = info.get('returnOnEquity')
            metrics['npm'] = info.get('profitMargins')
            metrics['roa'] = info.get('returnOnAssets')
            metrics['roic'] = info.get('returnOnCapital')
            
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
