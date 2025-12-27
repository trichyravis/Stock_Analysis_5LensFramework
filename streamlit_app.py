
"""
═══════════════════════════════════════════════════════════════════════════════
THE MOUNTAIN PATH - WORLD OF FINANCE
Nifty 50 Stock Analysis Platform - Multiple Analysis Modes
Five-Lens Framework with Advanced Risk Metrics
═══════════════════════════════════════════════════════════════════════════════

Prof. V. Ravichandran
28+ Years Corporate Finance & Banking Experience
10+ Years Academic Excellence
"""

import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import plotly.graph_objects as go
import plotly.express as px

# ═══════════════════════════════════════════════════════════════════════════════
# PAGE CONFIG
# ═══════════════════════════════════════════════════════════════════════════════

st.set_page_config(
    page_title="The Mountain Path - Stock Analysis",
    page_icon="🏔️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ═══════════════════════════════════════════════════════════════════════════════
# PROFESSIONAL CUSTOM CSS
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
    <style>
    .main {
        padding: 0rem 0rem;
    }
    
    /* ════════════════════════════════════════════════════════════ */
    /* CLEAN HERO HEADER */
    /* ════════════════════════════════════════════════════════════ */
    
    .hero-title {
        background: linear-gradient(135deg, #003d70 0%, #005a9d 100%);
        padding: 2.5rem 3rem;
        border-radius: 25px;
        margin: 1rem 1rem 0rem 1rem;
        box-shadow: 0 10px 40px rgba(0, 51, 102, 0.3);
        border: none;
        display: flex;
        align-items: center;
        gap: 3rem;
    }
    
    .mountain-emoji {
        font-size: 80px;
        flex-shrink: 0;
        animation: float 3s ease-in-out infinite;
        text-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
    }
    
    .hero-text-right {
        flex: 1;
        text-align: right;
    }
    
    .hero-text-right h1 {
        font-size: 42px;
        font-weight: 900;
        color: white;
        margin: 0.2rem 0;
        text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.5);
        letter-spacing: 2px;
        line-height: 1.1;
    }
    
    .hero-text-right p:first-of-type {
        font-size: 18px;
        color: #E0F0FF;
        margin: 1rem 0 0.5rem 0;
        font-weight: 400;
        letter-spacing: 0.5px;
    }
    
    .hero-text-right p:last-of-type {
        font-size: 14px;
        color: #D0E8FF;
        margin: 0.5rem 0 0;
        font-weight: 400;
    }
    
    .time-display {
        text-align: center;
        color: #0066cc;
        padding: 1rem;
        font-size: 14px;
        font-weight: 500;
        margin: 0.5rem 1rem;
    }
    
    /* ════════════════════════════════════════════════════════════ */
    /* MODE SELECTION BUTTONS */
    /* ════════════════════════════════════════════════════════════ */
    
    .mode-button {
        padding: 1rem 1.5rem;
        border: 2px solid #003366;
        border-radius: 10px;
        background: white;
        color: #003366;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
        font-size: 15px;
    }
    
    .mode-button:hover {
        background: #003366;
        color: white;
        box-shadow: 0 4px 12px rgba(0, 51, 102, 0.3);
    }
    
    .mode-button.active {
        background: linear-gradient(135deg, #003d70 0%, #005a9d 100%);
        color: white;
        border-color: #005a9d;
        box-shadow: 0 6px 16px rgba(0, 51, 102, 0.4);
    }
    
    /* ════════════════════════════════════════════════════════════ */
    /* FLOATING ANIMATION */
    /* ════════════════════════════════════════════════════════════ */
    
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-15px); }
    }
    
    /* ════════════════════════════════════════════════════════════ */
    /* METRIC CARDS */
    /* ════════════════════════════════════════════════════════════ */
    
    .metric-card {
        background: linear-gradient(135deg, #003d70 0%, #005a9d 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        box-shadow: 0 4px 15px rgba(0, 51, 102, 0.2);
    }
    
    /* ════════════════════════════════════════════════════════════ */
    /* HEADINGS */
    /* ════════════════════════════════════════════════════════════ */
    
    h1 {
        color: #003366;
        border-bottom: 3px solid #003366;
        padding-bottom: 0.8rem;
        font-size: 32px;
    }
    
    h2 {
        color: #003366;
        margin-top: 1.5rem;
        font-size: 26px;
    }
    
    h3 {
        color: #005a9d;
        font-size: 20px;
    }
    
    /* ════════════════════════════════════════════════════════════ */
    /* RESPONSIVE DESIGN */
    /* ════════════════════════════════════════════════════════════ */
    
    @media (max-width: 768px) {
        .hero-title {
            flex-direction: column;
            text-align: center;
            padding: 2rem 1.5rem;
            gap: 1.5rem;
            margin: 1rem 0.5rem;
        }
        
        .mountain-emoji {
            font-size: 70px;
            margin: 0;
        }
        
        .hero-text-right {
            text-align: center;
        }
        
        .hero-text-right h1 {
            font-size: 36px;
        }
        
        .hero-text-right p:first-of-type {
            font-size: 16px;
        }
    }
    
    @media (max-width: 480px) {
        .hero-title {
            padding: 1.5rem 1rem;
        }
        
        .mountain-emoji {
            font-size: 60px;
        }
        
        .hero-text-right h1 {
            font-size: 28px;
            letter-spacing: 1px;
        }
        
        .hero-text-right p:first-of-type {
            font-size: 14px;
        }
        
        .hero-text-right p:last-of-type {
            font-size: 12px;
        }
    }
    
    </style>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# SESSION STATE INITIALIZATION
# ═══════════════════════════════════════════════════════════════════════════════

if 'analysis_mode' not in st.session_state:
    st.session_state.analysis_mode = "Single Stock Analysis"

# ═══════════════════════════════════════════════════════════════════════════════
# HEADER
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
    <div class="hero-title">
        <div class="mountain-emoji">🏔️</div>
        <div class="hero-text-right">
            <h1>THE MOUNTAIN PATH</h1>
            <h1>WORLD OF FINANCE</h1>
            <p>Stock Analysis Platform Using Five Lens Framework</p>
            <p>Valuation (20%) • Quality (25%) • Growth (20%) • Financial Health (20%) • Risk & Momentum (15%)</p>
        </div>
    </div>
""", unsafe_allow_html=True)

# Time display
now = datetime.now()
st.markdown(f"""
    <div class="time-display">
        📊 Last Updated: {now.strftime('%Y-%m-%d %H:%M:%S')}
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# ═══════════════════════════════════════════════════════════════════════════════
# MODE SELECTION
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("### 📊 Select Analysis Mode")

col1, col2, col3, col4 = st.columns(4)

modes = ["Single Stock Analysis", "Sector Comparison", "Peer Benchmarking", "Portfolio Risk"]

with col1:
    if st.button(f"📈 {modes[0]}", key="mode_1", use_container_width=True):
        st.session_state.analysis_mode = modes[0]

with col2:
    if st.button(f"🏭 {modes[1]}", key="mode_2", use_container_width=True):
        st.session_state.analysis_mode = modes[1]

with col3:
    if st.button(f"👥 {modes[2]}", key="mode_3", use_container_width=True):
        st.session_state.analysis_mode = modes[2]

with col4:
    if st.button(f"💼 {modes[3]}", key="mode_4", use_container_width=True):
        st.session_state.analysis_mode = modes[3]

st.markdown(f"**Current Mode:** {st.session_state.analysis_mode}")
st.markdown("---")

# ═══════════════════════════════════════════════════════════════════════════════
# NIFTY 50 REGISTRY
# ═══════════════════════════════════════════════════════════════════════════════

nifty50_registry = {
    "Reliance Industries": {"symbol": "RELIANCE.NS", "sector": "Energy", "pe": 18.5},
    "TCS": {"symbol": "TCS.NS", "sector": "IT", "pe": 22.3},
    "HDFC Bank": {"symbol": "HDFCBANK.NS", "sector": "Banking", "pe": 25.1},
    "Infosys": {"symbol": "INFY.NS", "sector": "IT", "pe": 24.8},
    "ICICI Bank": {"symbol": "ICICIBANK.NS", "sector": "Banking", "pe": 20.2},
    "Hindustan Unilever": {"symbol": "HINDUNILVR.NS", "sector": "FMCG", "pe": 45.6},
    "Wipro": {"symbol": "WIPRO.NS", "sector": "IT", "pe": 20.1},
    "Bajaj Finance": {"symbol": "BAJAJFINSV.NS", "sector": "Finance", "pe": 18.9},
    "Maruti Suzuki": {"symbol": "MARUTI.NS", "sector": "Auto", "pe": 15.3},
    "IndusInd Bank": {"symbol": "INDUSINDBK.NS", "sector": "Banking", "pe": 16.8},
}

sectors = sorted(list(set([v["sector"] for v in nifty50_registry.values()])))
company_names = sorted(nifty50_registry.keys())

# ═══════════════════════════════════════════════════════════════════════════════
# MODE 1: SINGLE STOCK ANALYSIS
# ═══════════════════════════════════════════════════════════════════════════════

if st.session_state.analysis_mode == "Single Stock Analysis":
    st.markdown("### 📈 Single Stock Analysis")
    st.write("Analyze a single stock using the Five-Lens Framework")
    
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        selected_company = st.selectbox(
            "Select Company:",
            company_names,
            key="single_stock_select"
        )
    
    with col2:
        period = st.selectbox("Period:", ["1y", "2y", "5y"], key="single_period")
    
    with col3:
        analyze_btn = st.button("🔍 Analyze", type="primary", key="single_analyze")
    
    if analyze_btn:
        company_data = nifty50_registry[selected_company]
        st.success(f"Analyzing {selected_company} ({company_data['symbol']}) for {period}")
        
        col1, col2, col3, col4, col5 = st.columns(5)
        
        with col1:
            st.metric("P/E Ratio", f"{company_data['pe']:.1f}x")
        with col2:
            st.metric("Sector", company_data['sector'])
        with col3:
            st.metric("Price", "₹2,345.50")
        with col4:
            st.metric("Market Cap", "₹15.2B")
        with col5:
            st.metric("Dividend", "2.5%")
        
        st.markdown("---")
        st.info("📊 Detailed analysis coming soon! Framework implementation in progress.")

# ═══════════════════════════════════════════════════════════════════════════════
# MODE 2: SECTOR COMPARISON
# ═══════════════════════════════════════════════════════════════════════════════

elif st.session_state.analysis_mode == "Sector Comparison":
    st.markdown("### 🏭 Sector Comparison")
    st.write("Compare stocks within the same sector")
    
    col1, col2 = st.columns([2, 2])
    
    with col1:
        selected_sector = st.selectbox(
            "Select Sector:",
            sectors,
            key="sector_select"
        )
    
    with col2:
        period = st.selectbox("Period:", ["1y", "2y", "5y"], key="sector_period")
    
    sector_companies = [c for c, d in nifty50_registry.items() if d["sector"] == selected_sector]
    
    if st.button("📊 Compare Sector", type="primary", key="sector_compare"):
        st.success(f"Comparing {len(sector_companies)} companies in {selected_sector} sector")
        
        # Create comparison table
        comparison_data = {
            "Company": sector_companies,
            "Sector": [selected_sector] * len(sector_companies),
            "P/E Ratio": [nifty50_registry[c]["pe"] for c in sector_companies],
            "Rating": ["⭐⭐⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐", "⭐⭐"][:len(sector_companies)],
        }
        
        df = pd.DataFrame(comparison_data)
        st.dataframe(df, use_container_width=True)
        
        st.markdown("---")
        st.info("📊 Sector analysis coming soon! Detailed metrics and rankings in development.")

# ═══════════════════════════════════════════════════════════════════════════════
# MODE 3: PEER BENCHMARKING
# ═══════════════════════════════════════════════════════════════════════════════

elif st.session_state.analysis_mode == "Peer Benchmarking":
    st.markdown("### 👥 Peer Benchmarking")
    st.write("Compare a stock against its peers")
    
    col1, col2 = st.columns([2, 2])
    
    with col1:
        main_company = st.selectbox(
            "Select Main Stock:",
            company_names,
            key="main_stock_select"
        )
    
    with col2:
        comparison_metric = st.selectbox(
            "Compare By:",
            ["P/E Ratio", "ROE", "Debt/Equity", "Dividend Yield"],
            key="metric_select"
        )
    
    main_sector = nifty50_registry[main_company]["sector"]
    peer_companies = [c for c, d in nifty50_registry.items() if d["sector"] == main_sector]
    
    if st.button("🔄 Benchmark", type="primary", key="benchmark_btn"):
        st.success(f"Benchmarking {main_company} against peers")
        
        # Create benchmark table
        benchmark_data = {
            "Company": peer_companies,
            "Status": ["Main Stock" if c == main_company else "Peer" for c in peer_companies],
            comparison_metric: [nifty50_registry[c]["pe"] + np.random.uniform(-2, 2) for c in peer_companies],
        }
        
        df = pd.DataFrame(benchmark_data)
        st.dataframe(df, use_container_width=True)
        
        st.markdown("---")
        st.info("📊 Benchmarking analysis coming soon! Detailed peer comparison metrics in development.")

# ═══════════════════════════════════════════════════════════════════════════════
# MODE 4: PORTFOLIO RISK
# ═══════════════════════════════════════════════════════════════════════════════

elif st.session_state.analysis_mode == "Portfolio Risk":
    st.markdown("### 💼 Portfolio Risk Analysis")
    st.write("Analyze risk metrics and diversification of your portfolio")
    
    st.write("**Add Stocks to Your Portfolio:**")
    
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        portfolio_stock = st.selectbox(
            "Select Stock:",
            company_names,
            key="portfolio_stock_select"
        )
    
    with col2:
        quantity = st.number_input("Quantity:", min_value=1, max_value=1000, value=10, key="qty_input")
    
    with col3:
        price = st.number_input("Price (₹):", min_value=100, max_value=50000, value=2500, key="price_input")
    
    if st.button("➕ Add to Portfolio", type="primary", key="add_portfolio"):
        st.success(f"Added {quantity} shares of {portfolio_stock} @ ₹{price}")
    
    st.markdown("---")
    
    # Portfolio summary
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Portfolio Value", "₹50,00,000")
    with col2:
        st.metric("Stocks", "8")
    with col3:
        st.metric("Avg P/E", "22.5x")
    with col4:
        st.metric("Beta", "1.15")
    
    st.markdown("---")
    st.info("📊 Portfolio risk analysis coming soon! Diversification metrics and risk assessment in development.")

# ═════════════════════════════════════════════════════════════════════════════════
# FIVE LENS FRAMEWORK INFO
# ═════════════════════════════════════════════════════════════════════════════════

st.markdown("---")
st.markdown("### 🎯 Five-Lens Framework")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.markdown("""
    <div class="metric-card">
        <div style="font-size: 24px; margin-bottom: 0.5rem;">📊</div>
        <strong>Valuation</strong>
        <div style="font-size: 18px; color: #FFD700; margin-top: 0.5rem;">20%</div>
        <small>Fair price</small>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card" style="border: 2px solid #FFD700; background: linear-gradient(135deg, #003d70 0%, #1a5a9d 100%);">
        <div style="font-size: 24px; margin-bottom: 0.5rem;">🏆</div>
        <strong>Quality</strong>
        <div style="font-size: 18px; color: #FFD700; margin-top: 0.5rem;">25%</div>
        <small>Excellence</small>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <div style="font-size: 24px; margin-bottom: 0.5rem;">📈</div>
        <strong>Growth</strong>
        <div style="font-size: 18px; color: #FFD700; margin-top: 0.5rem;">20%</div>
        <small>Expansion</small>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="metric-card">
        <div style="font-size: 24px; margin-bottom: 0.5rem;">💰</div>
        <strong>Financial Health</strong>
        <div style="font-size: 18px; color: #FFD700; margin-top: 0.5rem;">20%</div>
        <small>Strength</small>
    </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown("""
    <div class="metric-card">
        <div style="font-size: 24px; margin-bottom: 0.5rem;">⚡</div>
        <strong>Risk & Momentum</strong>
        <div style="font-size: 18px; color: #FFD700; margin-top: 0.5rem;">15%</div>
        <small>Trend</small>
    </div>
    """, unsafe_allow_html=True)

# ═════════════════════════════════════════════════════════════════════════════════
# SIDEBAR
# ═════════════════════════════════════════════════════════════════════════════════

st.sidebar.markdown("---")
st.sidebar.write("### 📊 STOCK ANALYSIS TOOL")
st.sidebar.write("Five-Lens Framework Platform")
st.sidebar.markdown("---")

st.sidebar.write("**Analysis Modes:**")
st.sidebar.write("""
📈 **Single Stock Analysis**
Deep dive into individual stocks

🏭 **Sector Comparison**
Compare stocks within same sector

👥 **Peer Benchmarking**
Compare against competitors

💼 **Portfolio Risk**
Analyze your portfolio
""")

st.sidebar.markdown("---")
st.sidebar.write("**Five-Lens Framework:**")
st.sidebar.write("""
🎯 Valuation (20%)
✨ Quality (25%)
📈 Growth (20%)
💪 Financial Health (20%)
⚡ Risk & Momentum (15%)
""")

st.sidebar.markdown("---")
st.sidebar.write("**Prof. V. Ravichandran**")
st.sidebar.write("*28+ Years Finance Experience*")
st.sidebar.write("*10+ Years Academic Excellence*")

st.sidebar.markdown("""
    <a href="https://www.linkedin.com/in/trichyravis" target="_blank" 
       style="display: inline-block; margin-top: 1rem; padding: 0.5rem 1rem; 
              background: linear-gradient(135deg, #0077b5 0%, #0a66c2 100%); 
              color: white; text-decoration: none; border-radius: 8px; 
              font-weight: 600; text-align: center; width: 90%;">
       🔗 LinkedIn Profile
    </a>
""", unsafe_allow_html=True)

# ═════════════════════════════════════════════════════════════════════════════════
# FOOTER
# ═════════════════════════════════════════════════════════════════════════════════

st.markdown("---")
st.markdown("""
    <div style="text-align: center; color: #666; padding: 2rem;">
        <p><strong>THE MOUNTAIN PATH - WORLD OF FINANCE</strong></p>
        <p>Stock Analysis Platform Using Five Lens Framework</p>
        <p>Prof. V. Ravichandran | 28+ Years Finance Experience</p>
        <p style="margin-top: 1rem;">
            <a href="https://www.linkedin.com/in/trichyravis" target="_blank" 
               style="display: inline-block; padding: 0.5rem 1.5rem; 
                      background: linear-gradient(135deg, #0077b5 0%, #0a66c2 100%); 
                      color: white; text-decoration: none; border-radius: 8px; 
                      font-weight: 600; margin: 0 0.5rem;">
               🔗 LinkedIn Profile
            </a>
        </p>
        <p style="font-size: 0.8rem; margin-top: 1rem; color: #999;">
            Disclaimer: This tool is for educational purposes. Not financial advice. 
            Always consult with a qualified financial advisor before making investment decisions.
        </p>
    </div>
""", unsafe_allow_html=True)
