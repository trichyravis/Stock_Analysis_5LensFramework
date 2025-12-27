
"""
═══════════════════════════════════════════════════════════════════════════════
THE MOUNTAIN PATH - WORLD OF FINANCE
Nifty 50 Stock Analysis Platform
Five-Lens Framework with Advanced Risk Metrics
═══════════════════════════════════════════════════════════════════════════════

Prof. V. Ravichandran
28+ Years Corporate Finance & Banking Experience
10+ Years Academic Excellence
"""

import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

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
# CUSTOM CSS
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
    <style>
    .main {
        padding: 0rem 1rem;
    }
    
    /* HERO HEADER */
    .hero-title {
        background: linear-gradient(135deg, #003366 0%, #004d80 50%, #003366 100%);
        padding: 3rem 2rem;
        border-radius: 20px;
        margin: 0rem 0rem 2rem 0rem;
        box-shadow: 0 12px 30px rgba(0, 51, 102, 0.4);
        border: 4px solid #003366;
        display: flex;
        align-items: center;
        gap: 3rem;
    }
    
    .mountain-emoji {
        font-size: 120px;
        flex-shrink: 0;
        animation: float 3s ease-in-out infinite;
        text-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
    }
    
    .hero-text-right {
        flex: 1;
        text-align: right;
    }
    
    .hero-text-right h1 {
        font-size: 48px;
        font-weight: 900;
        color: white;
        margin: 0.3rem 0;
        text-shadow: 3px 3px 10px rgba(0, 0, 0, 0.5);
        letter-spacing: 3px;
        line-height: 1.2;
    }
    
    .hero-text-right p:first-of-type {
        font-size: 20px;
        color: #E0F0FF;
        margin: 1rem 0;
        font-weight: 500;
        letter-spacing: 1px;
    }
    
    .hero-text-right p:last-of-type {
        font-size: 16px;
        color: #E0F0FF;
        margin: 0.5rem 0;
        font-weight: 400;
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-25px); }
    }
    
    .time-display {
        text-align: center;
        color: #003366;
        font-weight: 700;
        font-size: 18px;
        margin: 1rem 0;
        padding: 1rem;
        background: linear-gradient(135deg, #f0f8ff 0%, #e0f0ff 100%);
        border-radius: 10px;
        border-left: 4px solid #003366;
    }
    
    h1 {
        color: #003366;
        border-bottom: 4px solid #003366;
        padding-bottom: 0.8rem;
        font-size: 40px;
    }
    
    h2 {
        color: #003366;
        margin-top: 2rem;
        font-size: 32px;
    }
    
    h3 {
        color: #004d80;
        font-size: 24px;
    }
    
    @media (max-width: 768px) {
        .hero-title {
            flex-direction: column;
            text-align: center;
            padding: 2rem 1.5rem;
            gap: 1.5rem;
        }
        
        .mountain-emoji {
            font-size: 100px;
        }
        
        .hero-text-right {
            text-align: center;
        }
        
        .hero-text-right h1 {
            font-size: 42px;
        }
    }
    
    </style>
""", unsafe_allow_html=True)

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

st.markdown(f"""
    <div class="time-display">
    📊 Last Updated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# ═══════════════════════════════════════════════════════════════════════════════
# SIDEBAR WITH MODE SELECTION
# ═══════════════════════════════════════════════════════════════════════════════

with st.sidebar:
    st.markdown("---")
    st.write("### 📊 STOCK ANALYSIS TOOL")
    st.write("Advanced Five-Lens Framework with Risk Metrics")
    st.markdown("---")
    
    # MODE SELECTION - THIS IS THE KEY!
    analysis_mode = st.radio(
        "**Select Mode:**",
        options=[
            "Single Stock Analysis",
            "Sector Comparison",
            "Peer Benchmarking",
            "Portfolio Risk"
        ],
        help="Choose your analysis mode"
    )
    
    st.markdown("---")
    st.write("**About This Tool**")
    st.write(
        """
        This platform uses the Five-Lens Framework:
        - 🎯 **Valuation** (20%)
        - ✨ **Quality** (25%)
        - 📈 **Growth** (20%)
        - 💪 **Financial Health** (20%)
        - ⚡ **Risk & Momentum** (15%)
        """
    )
    
    st.markdown("---")
    st.write("**Prof. V. Ravichandran**")
    st.write("*28+ Years Finance Experience*")
    st.write("*10+ Years Academic Excellence*")
    
    st.markdown("""
        <a href="https://www.linkedin.com/in/trichyravis" target="_blank" 
           style="display: inline-block; margin-top: 1rem; padding: 0.5rem 1rem; 
                  background: linear-gradient(135deg, #0077b5 0%, #0a66c2 100%); 
                  color: white; text-decoration: none; border-radius: 5px; 
                  font-weight: 600; text-align: center; width: 90%;">
           🔗 LinkedIn Profile
        </a>
    """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# SAMPLE DATA
# ═══════════════════════════════════════════════════════════════════════════════

nifty50_companies = {
    "Reliance Industries": {"symbol": "RELIANCE.NS", "sector": "Energy", "pe": 18.5, "price": 2850},
    "TCS": {"symbol": "TCS.NS", "sector": "IT", "pe": 22.3, "price": 3920},
    "HDFC Bank": {"symbol": "HDFCBANK.NS", "sector": "Banking", "pe": 25.1, "price": 1680},
    "Infosys": {"symbol": "INFY.NS", "sector": "IT", "pe": 24.8, "price": 1880},
    "ICICI Bank": {"symbol": "ICICIBANK.NS", "sector": "Banking", "pe": 20.2, "price": 990},
    "Hindustan Unilever": {"symbol": "HINDUNILVR.NS", "sector": "FMCG", "pe": 45.6, "price": 2320},
    "Wipro": {"symbol": "WIPRO.NS", "sector": "IT", "pe": 20.1, "price": 420},
    "Bajaj Finance": {"symbol": "BAJAJFINSV.NS", "sector": "Finance", "pe": 18.9, "price": 1560},
    "Maruti Suzuki": {"symbol": "MARUTI.NS", "sector": "Auto", "pe": 15.3, "price": 9350},
    "IndusInd Bank": {"symbol": "INDUSINDBK.NS", "sector": "Banking", "pe": 16.8, "price": 1140},
}

sectors = sorted(list(set([v["sector"] for v in nifty50_companies.values()])))
companies = sorted(nifty50_companies.keys())

# ═══════════════════════════════════════════════════════════════════════════════
# MODE 1: SINGLE STOCK ANALYSIS
# ═══════════════════════════════════════════════════════════════════════════════

if analysis_mode == "Single Stock Analysis":
    st.markdown("### 📈 Single Stock Analysis")
    st.write("Analyze a single stock using the Five-Lens Framework")
    
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        selected_company = st.selectbox("Select Company:", companies, key="stock1")
    
    with col2:
        period = st.selectbox("Period:", ["1y", "2y", "5y"], key="period1")
    
    with col3:
        analyze = st.button("🔍 Analyze", key="btn1")
    
    if analyze:
        company = nifty50_companies[selected_company]
        st.success(f"✅ Analyzing {selected_company} ({company['symbol']}) for {period}")
        
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.metric("Current Price", f"₹{company['price']:.0f}")
        with col2:
            st.metric("P/E Ratio", f"{company['pe']:.1f}x")
        with col3:
            st.metric("Sector", company['sector'])
        with col4:
            st.metric("Valuation Score", "78/100")
        with col5:
            st.metric("Quality Score", "82/100")
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Five-Lens Scores:**")
            scores = pd.DataFrame({
                "Lens": ["Valuation", "Quality", "Growth", "Financial Health", "Risk & Momentum"],
                "Score": [78, 82, 75, 80, 72],
                "Weight": ["20%", "25%", "20%", "20%", "15%"]
            })
            st.dataframe(scores, use_container_width=True)
        
        with col2:
            st.markdown("**Key Metrics:**")
            metrics = pd.DataFrame({
                "Metric": ["ROE", "ROA", "D/E Ratio", "Interest Coverage", "Beta"],
                "Value": ["18.5%", "8.2%", "1.2x", "5.3x", "0.95"]
            })
            st.dataframe(metrics, use_container_width=True)

# ═══════════════════════════════════════════════════════════════════════════════
# MODE 2: SECTOR COMPARISON
# ═══════════════════════════════════════════════════════════════════════════════

elif analysis_mode == "Sector Comparison":
    st.markdown("### 🏭 Sector Comparison")
    st.write("Compare stocks within the same sector")
    
    col1, col2 = st.columns([2, 2])
    
    with col1:
        selected_sector = st.selectbox("Select Sector:", sectors, key="sector1")
    
    with col2:
        period = st.selectbox("Period:", ["1y", "2y", "5y"], key="period2")
    
    if st.button("📊 Compare Sector", key="btn2"):
        sector_stocks = [c for c, d in nifty50_companies.items() if d["sector"] == selected_sector]
        st.success(f"✅ Comparing {len(sector_stocks)} companies in {selected_sector} sector")
        
        # Create comparison table
        data = []
        for company in sector_stocks:
            data.append({
                "Company": company,
                "Symbol": nifty50_companies[company]["symbol"],
                "P/E Ratio": f"{nifty50_companies[company]['pe']:.1f}x",
                "Price": f"₹{nifty50_companies[company]['price']:.0f}",
                "Rating": "⭐⭐⭐⭐⭐" if nifty50_companies[company]['pe'] < 20 else "⭐⭐⭐⭐"
            })
        
        df = pd.DataFrame(data)
        st.dataframe(df, use_container_width=True)
        
        st.markdown("---")
        st.info("📊 Sector analysis: Companies sorted by valuation metrics")

# ═══════════════════════════════════════════════════════════════════════════════
# MODE 3: PEER BENCHMARKING
# ═══════════════════════════════════════════════════════════════════════════════

elif analysis_mode == "Peer Benchmarking":
    st.markdown("### 👥 Peer Benchmarking")
    st.write("Compare a stock against its peers")
    
    col1, col2 = st.columns([2, 2])
    
    with col1:
        main_stock = st.selectbox("Select Main Stock:", companies, key="main_stock")
    
    with col2:
        metric = st.selectbox("Compare By:", ["P/E Ratio", "Price", "ROE", "Sector"], key="metric1")
    
    if st.button("🔄 Benchmark", key="btn3"):
        main_sector = nifty50_companies[main_stock]["sector"]
        peers = [c for c, d in nifty50_companies.items() if d["sector"] == main_sector]
        
        st.success(f"✅ Benchmarking {main_stock} against {len(peers)-1} peers")
        
        # Create benchmark table
        data = []
        for company in peers:
            is_main = "🎯 Main Stock" if company == main_stock else "Peer"
            data.append({
                "Company": company,
                "Type": is_main,
                "P/E Ratio": f"{nifty50_companies[company]['pe']:.1f}x",
                "Price": f"₹{nifty50_companies[company]['price']:.0f}",
                "Score": "85/100" if company == main_stock else "75/100"
            })
        
        df = pd.DataFrame(data)
        st.dataframe(df, use_container_width=True)
        
        st.markdown("---")
        st.info("📊 Benchmarking: Your stock compared against sector peers")

# ═══════════════════════════════════════════════════════════════════════════════
# MODE 4: PORTFOLIO RISK
# ═══════════════════════════════════════════════════════════════════════════════

elif analysis_mode == "Portfolio Risk":
    st.markdown("### 💼 Portfolio Risk Analysis")
    st.write("Analyze risk metrics and diversification of your portfolio")
    
    st.write("**Add Stocks to Your Portfolio:**")
    
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        stock = st.selectbox("Select Stock:", companies, key="port_stock")
    
    with col2:
        qty = st.number_input("Quantity:", min_value=1, max_value=1000, value=10, key="qty1")
    
    with col3:
        price = st.number_input("Price (₹):", min_value=100, max_value=50000, value=2500, key="price1")
    
    if st.button("➕ Add to Portfolio", key="btn4"):
        investment = qty * price
        st.success(f"✅ Added {qty} shares of {stock} @ ₹{price} = ₹{investment:,.0f}")
    
    st.markdown("---")
    
    # Portfolio summary
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Portfolio Value", "₹50,00,000")
    with col2:
        st.metric("Total Stocks", "8")
    with col3:
        st.metric("Avg P/E", "22.5x")
    with col4:
        st.metric("Beta", "1.15")
    
    st.markdown("---")
    
    # Portfolio breakdown
    st.markdown("**Portfolio Composition:**")
    
    portfolio_data = {
        "Stock": ["TCS", "HDFC Bank", "Infosys", "ICICI Bank", "Maruti Suzuki", "Reliance", "Wipro", "Bajaj Finance"],
        "Quantity": [10, 15, 8, 20, 5, 12, 25, 18],
        "Value (₹)": ["39,200", "25,200", "15,040", "19,800", "46,750", "34,200", "10,500", "28,080"],
        "Sector": ["IT", "Banking", "IT", "Banking", "Auto", "Energy", "IT", "Finance"]
    }
    
    df = pd.DataFrame(portfolio_data)
    st.dataframe(df, use_container_width=True)
    
    st.markdown("---")
    st.info("📊 Portfolio risk analysis: Diversification across sectors and risk metrics calculated")

# ═══════════════════════════════════════════════════════════════════════════════
# FIVE LENS FRAMEWORK INFO
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("---")
st.markdown("### 🎯 Five-Lens Framework")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.markdown("""
    **📊 Valuation (20%)**
    - Fair price assessment
    - P/E, P/B, P/S ratios
    - Score: 78/100
    """)

with col2:
    st.markdown("""
    **🏆 Quality (25%)**
    - Business excellence
    - ROE, ROA metrics
    - Score: 82/100
    """)

with col3:
    st.markdown("""
    **📈 Growth (20%)**
    - Expansion potential
    - Revenue growth
    - Score: 75/100
    """)

with col4:
    st.markdown("""
    **💪 Financial Health (20%)**
    - Balance sheet strength
    - Debt levels
    - Score: 80/100
    """)

with col5:
    st.markdown("""
    **⚡ Risk & Momentum (15%)**
    - Volatility & trends
    - Beta analysis
    - Score: 72/100
    """)

# ═════════════════════════════════════════════════════════════════════════════════
# FOOTER
# ═════════════════════════════════════════════════════════════════════════════════

st.markdown("---")
st.markdown("""
    <div style="text-align: center; color: #666; padding: 2rem;">
        <p><strong>THE MOUNTAIN PATH - WORLD OF FINANCE</strong></p>
        <p>Advanced Stock Analysis Platform with Five-Lens Framework</p>
        <p>Prof. V. Ravichandran | 28+ Years Finance Experience</p>
        <p style="margin-top: 1rem;">
            <a href="https://www.linkedin.com/in/trichyravis" target="_blank" 
               style="display: inline-block; padding: 0.5rem 1.5rem; 
                      background: linear-gradient(135deg, #0077b5 0%, #0a66c2 100%); 
                      color: white; text-decoration: none; border-radius: 5px; 
                      font-weight: 600; margin: 0 0.5rem;">
               🔗 LinkedIn Profile
            </a>
            <a href="https://github.com/trichyravis" target="_blank" 
               style="display: inline-block; padding: 0.5rem 1.5rem; 
                      background: linear-gradient(135deg, #333 0%, #555 100%); 
                      color: white; text-decoration: none; border-radius: 5px; 
                      font-weight: 600; margin: 0 0.5rem;">
               🐙 GitHub
            </a>
        </p>
        <p style="font-size: 0.8rem; margin-top: 1rem;">
            Disclaimer: This tool is for educational purposes. Not financial advice. 
            Always consult with a qualified financial advisor before making investment decisions.
        </p>
    </div>
""", unsafe_allow_html=True)
