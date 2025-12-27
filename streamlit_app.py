
import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
import time
from typing import Dict, Tuple, Optional, List

# ═══════════════════════════════════════════════════════════════════════════════
# BACKEND LOGIC: DATA & RISK CALCULATORS
# ═══════════════════════════════════════════════════════════════════════════════

class DataFetcher:
    """Robust data fetching with timezone handling and fallback mechanisms"""
    
    NIFTY50_REGISTRY = {
        'RELIANCE': {'symbol': 'RELIANCE.NS', 'sector': 'Energy'},
        'HDFCBANK': {'symbol': 'HDFCBANK.NS', 'sector': 'Financials'},
        'INFY': {'symbol': 'INFY.NS', 'sector': 'IT'},
        'TCS': {'symbol': 'TCS.NS', 'sector': 'IT'},
        'ICICIBANK': {'symbol': 'ICICIBANK.NS', 'sector': 'Financials'},
        'HINDUNILVR': {'symbol': 'HINDUNILVR.NS', 'sector': 'FMCG'},
        'ITC': {'symbol': 'ITC.NS', 'sector': 'FMCG'},
        'SBIN': {'symbol': 'SBIN.NS', 'sector': 'Financials'},
        'BHARTIARTL': {'symbol': 'BHARTIARTL.NS', 'sector': 'Telecom'},
        'ADANIPORTS': {'symbol': 'ADANIPORTS.NS', 'sector': 'Infrastructure'}
        # Expanded registry can be added here...
    }

    @staticmethod
    def fetch_stock_data(symbol: str, period: str = "1y") -> Tuple[Optional[pd.DataFrame], Dict]:
        try:
            ticker = yf.Ticker(symbol)
            hist = ticker.history(period=period)
            return (hist, ticker.info) if not hist.empty else (None, {})
        except Exception: return None, {}

    @staticmethod
    def fetch_market_index(symbol: str = "^NSEI", period: str = "1y") -> Optional[pd.DataFrame]:
        try:
            idx = yf.Ticker(symbol).history(period=period)
            return idx if not idx.empty else None
        except Exception: return None

    @staticmethod
    def calculate_beta(stock_prices: pd.Series, market_prices: pd.Series) -> Optional[float]:
        """Core Beta calculation using timezone-neutral alignment"""
        try:
            # 1. Align timezones and get returns
            s_ret = stock_prices.tz_localize(None).pct_change().dropna()
            m_ret = market_prices.tz_localize(None).pct_change().dropna()
            
            # 2. Inner join to match dates
            combined = pd.concat([s_ret, m_ret], axis=1, join='inner').dropna()
            if len(combined) < 30: return None
            
            # 3. Beta = Cov(s,m) / Var(m)
            cov = np.cov(combined.iloc[:, 0], combined.iloc[:, 1])[0, 1]
            var = np.var(combined.iloc[:, 1])
            return round(cov / var, 3) if var != 0 else None
        except Exception: return None

    @staticmethod
    def extract_stock_data(info: Dict, price_hist: pd.DataFrame) -> Dict:
        return {
            'current_price': info.get('currentPrice', price_hist['Close'].iloc[-1]),
            'pe_ratio': info.get('trailingPE'),
            'pb_ratio': info.get('priceToBook'),
            'ps_ratio': info.get('priceToSalesTrailing12Months'),
            'dividend_yield': info.get('dividendYield', 0),
            'market_cap': info.get('marketCap')
        }

    @staticmethod
    def extract_financial_metrics(info: Dict) -> Dict:
        return {
            'roe': info.get('returnOnEquity', 0),
            'npm': info.get('profitMargins', 0),
            'roa': info.get('returnOnAssets', 0),
            'roic': info.get('returnOnCapital', 0),
            'debt_to_equity': info.get('debtToEquity'),
            'current_ratio': info.get('currentRatio'),
            'interest_coverage': info.get('interestCoverage'),
            'revenue_growth_yoy': info.get('revenueGrowth', 0),
            'earnings_growth_yoy': info.get('earningsGrowth', 0),
            'peg_ratio': info.get('pegRatio')
        }

class FiveLensFramework:
    """The signature framework for Prof. V. Ravichandran's analysis"""
    
    class Scores:
        def __init__(self, v, q, g, h, r):
            self.valuation = v
            self.quality = q
            self.growth = g
            self.financial_health = h
            self.risk_momentum = r
            self.composite = (v*0.20 + q*0.25 + g*0.20 + h*0.20 + r*0.15)
            
        def to_dict(self):
            return {
                'Valuation': self.valuation, 'Quality': self.quality, 
                'Growth': self.growth, 'Financial Health': self.financial_health,
                'Risk & Momentum': self.risk_momentum, 'Composite Score': self.composite
            }

    def evaluate_stock(self, stock_data, fin_metrics, risk_metrics) -> Scores:
        # Simplified scoring logic (0-100 scale)
        v = 70 if (stock_data.get('pe_ratio') or 25) < 20 else 50
        q = fin_metrics.get('roe', 0) * 400 # 15% ROE -> 60 points
        g = fin_metrics.get('revenue_growth_yoy', 0) * 300
        h = 80 if (fin_metrics.get('debt_to_equity') or 100) < 50 else 40
        
        # Risk Score: 100 - (Beta * 30) -> Lower Beta = Higher Score
        beta = risk_metrics.get('beta', 1.0)
        r = max(0, min(100, 100 - (beta * 30)))
        
        return self.Scores(min(v, 100), min(q, 100), min(g, 100), min(h, 100), r)

# ═══════════════════════════════════════════════════════════════════════════════
# STREAMLIT INTERFACE
# ═══════════════════════════════════════════════════════════════════════════════

st.set_page_config(page_title="Mountain Path - Stock Analysis", layout="wide")

# Custom Styles
st.markdown("""
    <style>
    .metric-container { background-color: #f0f2f6; padding: 15px; border-radius: 10px; border-left: 5px solid #003366; }
    h1 { color: #003366; }
    </style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("🏔️ Navigation")
analysis_mode = st.sidebar.radio("Analysis Mode", 
    ["Single Stock Analysis", "Sector Comparison", "Peer Benchmarking", "Portfolio Risk"])

st.sidebar.info("Framework: Valuation (20%), Quality (25%), Growth (20%), Health (20%), Risk (15%)")

# Fetch Market Data once at top-level to speed up app
market_data = DataFetcher.fetch_market_index("^NSEI")

if analysis_mode == "Single Stock Analysis":
    st.title("📈 Single Stock Analysis")
    registry = DataFetcher.NIFTY50_REGISTRY
    selected_company = st.selectbox("Select Company", sorted(registry.keys()))
    
    if st.button("Analyze Stock"):
        with st.spinner("Processing Five-Lens Framework..."):
            ticker_symbol = registry[selected_company]['symbol']
            price_hist, info = DataFetcher.fetch_stock_data(ticker_symbol)
            
            if price_hist is not None:
                stock_data = DataFetcher.extract_stock_data(info, price_hist)
                fin_metrics = DataFetcher.extract_financial_metrics(info)
                
                # Manual Beta Calculation
                beta = DataFetcher.calculate_beta(price_hist['Close'], market_data['Close'])
                risk_metrics = {'beta': beta or info.get('beta', 1.0)}
                
                # Framework Evaluation
                framework = FiveLensFramework()
                scores = framework.evaluate_stock(stock_data, fin_metrics, risk_metrics)
                
                # --- UI DISPLAY ---
                col1, col2, col3, col4 = st.columns(4)
                col1.metric("Current Price", f"₹{stock_data['current_price']:.2f}")
                col2.metric("Beta (Calculated)", f"{risk_metrics['beta']:.2f}")
                col3.metric("P/E Ratio", f"{stock_data['pe_ratio'] or 'N/A'}")
                col4.metric("Composite Score", f"{scores.composite:.1f}/100")

                st.markdown("---")
                
                # Radar Chart
                fig = go.Figure(data=go.Scatterpolar(
                    r=[scores.valuation, scores.quality, scores.growth, scores.financial_health, scores.risk_momentum],
                    theta=['Valuation','Quality','Growth','Health','Risk'],
                    fill='toself', line_color='#003366'
                ))
                fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 100])), title=f"{selected_company} Risk Radar")
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.error("Data Fetch Error. Please try again.")

elif analysis_mode == "Portfolio Risk":
    st.title("💼 Portfolio Risk Analysis")
    
    registry = DataFetcher.NIFTY50_REGISTRY
    selected_stocks = st.multiselect("Select Portfolio Holdings", sorted(registry.keys()), default=['RELIANCE', 'INFY'])
    
    if selected_stocks:
        weights = {}
        cols = st.columns(len(selected_stocks))
        for i, stock in enumerate(selected_stocks):
            weights[stock] = cols[i].number_input(f"Weight % ({stock})", 0, 100, 100//len(selected_stocks))
        
        if st.button("Calculate Portfolio Beta"):
            port_beta = 0
            results = []
            for stock in selected_stocks:
                _, info = DataFetcher.fetch_stock_data(registry[stock]['symbol'])
                b = info.get('beta', 1.0)
                w = weights[stock] / 100
                port_beta += (b * w)
                results.append({"Stock": stock, "Beta": b, "Weight": f"{w*100}%"})
            
            st.write("### Portfolio Composition")
            st.table(pd.DataFrame(results))
            
            st.subheader(f"Weighted Portfolio Beta: {port_beta:.2f}")
            if port_beta > 1.1: st.warning("Aggressive Portfolio: Highly sensitive to Nifty movements.")
            elif port_beta < 0.9: st.success("Defensive Portfolio: Built for capital protection.")
            else: st.info("Balanced Portfolio: Moving in sync with the market.")

# Footer
st.markdown("---")
st.caption("Prof. V. Ravichandran | 28+ Years Finance Experience | Educational Research Tool")
