"""
═══════════════════════════════════════════════════════════════════════════════
THE MOUNTAIN PATH - WORLD OF FINANCE
Data Fetcher Module
Live data from yfinance with caching and error handling
═══════════════════════════════════════════════════════════════════════════════
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import Dict, Optional, Tuple
import streamlit as st
import warnings
warnings.filterwarnings('ignore')


class DataFetcher:
    """Fetch live data from yfinance with caching"""
    
    CACHE_DURATION = 300  # 5 minutes
    
    @staticmethod
    @st.cache_data(ttl=CACHE_DURATION)
    def fetch_stock_data(symbol: str, period: str = '1y') -> Tuple[Optional[pd.DataFrame], Optional[Dict]]:
        """
        Fetch historical price data and current info
        
        Parameters:
        -----------
        symbol : str
            Stock symbol (e.g., 'HDFCBANK.NS')
        period : str
            Period of historical data ('1y', '2y', '5y', etc.)
            
        Returns:
        --------
        Tuple[Optional[pd.DataFrame], Optional[Dict]]
            (price_history, stock_info) or (None, None) if error
        """
        try:
            import yfinance as yf
            
            # Fetch ticker
            ticker = yf.Ticker(symbol)
            
            # Get historical data
            hist = ticker.history(period=period)
            
            if hist.empty:
                return None, None
            
            # Get info
            info = ticker.info
            
            return hist, info
            
        except Exception as e:
            st.error(f"Error fetching data for {symbol}: {str(e)}")
            return None, None

    @staticmethod
    @st.cache_data(ttl=CACHE_DURATION)
    def fetch_market_index(index_symbol: str = '^NSEI', period: str = '1y') -> Optional[pd.Series]:
        """
        Fetch market index data (for beta calculation)
        
        Parameters:
        -----------
        index_symbol : str
            Index symbol ('^NSEI' for Nifty 50)
        period : str
            Period of data
            
        Returns:
        --------
        Optional[pd.Series]
            Index prices or None if error
        """
        try:
            import yfinance as yf
            
            index = yf.Ticker(index_symbol)
            hist = index.history(period=period)
            
            if hist.empty:
                return None
            
            return hist['Close']
            
        except Exception as e:
            return None

    @staticmethod
    def extract_stock_data(info: Dict, price_history: pd.DataFrame) -> Dict:
        """
        Extract and standardize stock data from yfinance info
        
        Parameters:
        -----------
        info : Dict
            Stock info from yfinance
        price_history : pd.DataFrame
            Historical prices
            
        Returns:
        --------
        Dict : Standardized stock data
        """
        try:
            current_price = price_history['Close'].iloc[-1] if len(price_history) > 0 else None
            
            # 52-week metrics
            high_52w = price_history['Close'].max() if len(price_history) > 0 else None
            low_52w = price_history['Close'].min() if len(price_history) > 0 else None
            
            # Calculate momentum
            if len(price_history) > 252:
                price_52w_ago = price_history['Close'].iloc[-252]
                momentum = (current_price - price_52w_ago) / price_52w_ago if price_52w_ago != 0 else 0
            else:
                momentum = 0
            
            stock_data = {
                'symbol': info.get('symbol', 'N/A'),
                'company_name': info.get('longName', 'N/A'),
                'sector': info.get('sector', 'N/A'),
                'current_price': current_price,
                'pe_ratio': info.get('trailingPE', info.get('forwardPE', None)),
                'pb_ratio': info.get('priceToBook', None),
                'ps_ratio': info.get('priceToSalesTrailing12Months', None),
                'market_cap': info.get('marketCap', None),
                'dividend_yield': info.get('dividendYield', None),
                'eps': info.get('trailingEps', None),
                'book_value': info.get('bookValue', None),
                '52w_high': high_52w,
                '52w_low': low_52w,
                'price_momentum_52w': momentum,
                'avg_volume': info.get('averageVolume', None),
                'last_updated': datetime.now()
            }
            
            return stock_data
            
        except Exception as e:
            return {}

    @staticmethod
    def extract_financial_metrics(info: Dict, ticker_obj=None) -> Dict:
        """
        Extract financial metrics from yfinance
        
        Parameters:
        -----------
        info : Dict
            Stock info
        ticker_obj : Optional
            yfinance Ticker object (for additional data)
            
        Returns:
        --------
        Dict : Financial metrics
        """
        try:
            metrics = {
                # Profitability
                'npm': info.get('profitMargins', None),
                'roe': info.get('returnOnEquity', None),
                'roa': info.get('returnOnAssets', None),
                'roic': info.get('returnOnCapital', None),
                
                # Leverage
                'debt_to_equity': None,
                'debt_to_assets': None,
                'current_ratio': None,
                'quick_ratio': None,
                'interest_coverage': None,
                
                # Growth
                'revenue_growth_yoy': info.get('revenuePerShare', None),
                'earnings_growth_yoy': info.get('earningsGrowth', None),
                'peg_ratio': None,
                
                # Cash Flow
                'free_cash_flow': info.get('freeCashflow', None),
                'operating_cash_flow': info.get('operatingCashflow', None),
                'fcf_to_net_income': None,
            }
            
            # Calculate D/E if available
            try:
                total_debt = info.get('totalDebt', None)
                total_equity = info.get('totalStockholderEquity', None)
                if total_debt and total_equity:
                    metrics['debt_to_equity'] = total_debt / total_equity
            except:
                pass
            
            # Calculate PEG ratio if growth available
            try:
                pe = info.get('trailingPE')
                growth = info.get('earningsGrowth')
                if pe and growth and growth != 0:
                    metrics['peg_ratio'] = pe / (abs(growth) * 100)
            except:
                pass
            
            return metrics
            
        except Exception as e:
            return {}

    @staticmethod
    def validate_data(stock_data: Dict, financial_metrics: Dict) -> bool:
        """
        Validate that we have minimum required data
        
        Parameters:
        -----------
        stock_data : Dict
            Stock data
        financial_metrics : Dict
            Financial metrics
            
        Returns:
        --------
        bool : True if sufficient data
        """
        # Check if we have at least current price
        if not stock_data.get('current_price'):
            return False
        
        # Check if we have at least some valuation metrics
        valuation_metrics = [stock_data.get('pe_ratio'), 
                            stock_data.get('pb_ratio'),
                            stock_data.get('ps_ratio')]
        
        if not any(valuation_metrics):
            return False
        
        return True

    @staticmethod
    def get_nifty50_registry() -> Dict:
        """
        Get registry of Nifty 50 companies with symbols
        
        Returns:
        --------
        Dict : Company registry
        """
        registry = {
            # BANKING
            'HDFC BANK': {'symbol': 'HDFCBANK.NS', 'sector': 'Banking'},
            'ICICI BANK': {'symbol': 'ICICIBANK.NS', 'sector': 'Banking'},
            'AXIS BANK': {'symbol': 'AXISBANK.NS', 'sector': 'Banking'},
            'SBI': {'symbol': 'SBIN.NS', 'sector': 'Banking'},
            'KOTAK BANK': {'symbol': 'KOTAKBANK.NS', 'sector': 'Banking'},
            'INDUSIND BANK': {'symbol': 'INDUSINDBK.NS', 'sector': 'Banking'},
            
            # IT
            'TCS': {'symbol': 'TCS.NS', 'sector': 'Information Technology'},
            'INFOSYS': {'symbol': 'INFY.NS', 'sector': 'Information Technology'},
            'WIPRO': {'symbol': 'WIPRO.NS', 'sector': 'Information Technology'},
            'HCL TECH': {'symbol': 'HCLTECH.NS', 'sector': 'Information Technology'},
            
            # AUTOMOBILES
            'MARUTI': {'symbol': 'MARUTI.NS', 'sector': 'Automobile'},
            'TATA MOTORS': {'symbol': 'TATAMOTORS.NS', 'sector': 'Automobile'},
            'BAJAJ AUTO': {'symbol': 'BAJAJAUT.NS', 'sector': 'Automobile'},
            'HERO MOTOCORP': {'symbol': 'HEROMOTOCORP.NS', 'sector': 'Automobile'},
            
            # PHARMA
            'SUN PHARMA': {'symbol': 'SUNPHARMA.NS', 'sector': 'Pharmaceuticals'},
            'CIPLA': {'symbol': 'CIPLA.NS', 'sector': 'Pharmaceuticals'},
            'LAURUS LABS': {'symbol': 'LAURUSLAB.NS', 'sector': 'Pharmaceuticals'},
            
            # ENERGY
            'RELIANCE': {'symbol': 'RELIANCE.NS', 'sector': 'Energy'},
            'POWER GRID': {'symbol': 'POWERGRID.NS', 'sector': 'Energy'},
            'GAIL': {'symbol': 'GAIL.NS', 'sector': 'Energy'},
            
            # FINANCE
            'BAJAJ FINSERV': {'symbol': 'BAJAJFINSV.NS', 'sector': 'Financial Services'},
            
            # CONSUMER
            'ITC': {'symbol': 'ITC.NS', 'sector': 'Consumer Goods'},
            'NESTLE INDIA': {'symbol': 'NESTLEIND.NS', 'sector': 'Consumer Goods'},
            'BRITANNIA': {'symbol': 'BRITANNIA.NS', 'sector': 'Consumer Goods'},
            'HINDUSTAN UNILEVER': {'symbol': 'HINDUNILVR.NS', 'sector': 'Consumer Goods'},
            
            # METALS
            'TATA STEEL': {'symbol': 'TATASTEEL.NS', 'sector': 'Steel'},
            'HINDALCO': {'symbol': 'HINDALCO.NS', 'sector': 'Metals'},
            
            # CEMENT
            'SHREE CEMENT': {'symbol': 'SHREECEMENT.NS', 'sector': 'Cement'},
            
            # REALTY
            'DLF': {'symbol': 'DLF.NS', 'sector': 'Realty'},
            
            # PORTS
            'ADANI PORTS': {'symbol': 'ADANIPORTS.NS', 'sector': 'Ports & Logistics'},
        }
        
        return registry

    @staticmethod
    def batch_fetch_stocks(symbols: list, period: str = '1y', show_progress: bool = True) -> Dict[str, Tuple]:
        """
        Fetch data for multiple stocks
        
        Parameters:
        -----------
        symbols : list
            List of symbols
        period : str
            Period of data
        show_progress : bool
            Show progress bar
            
        Returns:
        --------
        Dict : Symbol -> (price_history, info)
        """
        results = {}
        
        if show_progress:
            progress_bar = st.progress(0)
            status_text = st.empty()
        
        for i, symbol in enumerate(symbols):
            if show_progress:
                progress = (i + 1) / len(symbols)
                progress_bar.progress(progress)
                status_text.text(f"Fetching {symbol}... ({i+1}/{len(symbols)})")
            
            price_hist, info = DataFetcher.fetch_stock_data(symbol, period)
            results[symbol] = (price_hist, info)
        
        if show_progress:
            status_text.empty()
        
        return results
