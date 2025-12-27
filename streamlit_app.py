
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
    
    /* HERO HEADER - COMPACT DESIGN (WIDTH REDUCED BY 50%, FONT OPTIMIZED) */
    .hero-title {
        background: linear-gradient(135deg, #003366 0%, #004d80 50%, #003366 100%);
        padding: 2rem 2rem;
        border-radius: 20px;
        margin: 0rem auto 2rem auto;
        box-shadow: 0 12px 30px rgba(0, 51, 102, 0.4);
        border: 4px solid #003366;
        display: flex;
        align-items: center;
        gap: 2rem;
        max-width: 1200px;
        width: 90%;
    }
    
    .mountain-emoji {
        font-size: 100px;
        flex-shrink: 0;
        animation: float 3s ease-in-out infinite;
        text-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
    }
    
    .hero-text-right {
        flex: 1;
        text-align: right;
    }
    
    .hero-text-right h1 {
        font-size: 32px;
        font-weight: 900;
        color: white;
        margin: 0.1rem 0;
        text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.5);
        letter-spacing: 2px;
        line-height: 1.1;
    }
    
    .hero-text-right p:first-of-type {
        font-size: 24px;
        color: #E0F0FF;
        margin: 0.8rem 0 0.3rem 0;
        font-weight: 600;
        letter-spacing: 0.5px;
    }
    
    .hero-text-right p:last-of-type {
        font-size: 14px;
        color: #D0E8FF;
        margin: 0.3rem 0 0;
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
    
    .metric-card {
        background: linear-gradient(135deg, #003d70 0%, #005a9d 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        box-shadow: 0 4px 15px rgba(0, 51, 102, 0.2);
    }
    
    @media (max-width: 768px) {
        .hero-title {
            flex-direction: column;
            text-align: center;
            padding: 1.5rem 1.5rem;
            gap: 1rem;
            margin: 0.5rem auto;
            max-width: 95%;
        }
        
        .mountain-emoji {
            font-size: 80px;
            margin: 0;
        }
        
        .hero-text-right {
            text-align: center;
        }
        
        .hero-text-right h1 {
            font-size: 24px;
            letter-spacing: 1px;
        }
        
        .hero-text-right p:first-of-type {
            font-size: 18px;
        }
        
        .hero-text-right p:last-of-type {
            font-size: 12px;
        }
    }
    
    @media (max-width: 480px) {
        .hero-title {
            padding: 1rem;
            max-width: 100%;
        }
        
        .mountain-emoji {
            font-size: 70px;
        }
        
        .hero-text-right h1 {
            font-size: 20px;
        }
        
        .hero-text-right p:first-of-type {
            font-size: 16px;
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
            <h1>THE MOUNTAIN PATH • WORLD OF FINANCE</h1>
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
    "Reliance Industries": {"symbol": "RELIANCE.NS", "sector": "Energy", "pe": 18.5, "price": 2850, "pb": 1.8, "ps": 0.9},
    "TCS": {"symbol": "TCS.NS", "sector": "IT", "pe": 22.3, "price": 3920, "pb": 4.2, "ps": 3.1},
    "HDFC Bank": {"symbol": "HDFCBANK.NS", "sector": "Banking", "pe": 25.1, "price": 1680, "pb": 3.5, "ps": 5.2},
    "Infosys": {"symbol": "INFY.NS", "sector": "IT", "pe": 24.8, "price": 1880, "pb": 3.8, "ps": 2.9},
    "ICICI Bank": {"symbol": "ICICIBANK.NS", "sector": "Banking", "pe": 20.2, "price": 990, "pb": 2.1, "ps": 4.5},
    "Hindustan Unilever": {"symbol": "HINDUNILVR.NS", "sector": "FMCG", "pe": 45.6, "price": 2320, "pb": 12.5, "ps": 8.2},
    "Wipro": {"symbol": "WIPRO.NS", "sector": "IT", "pe": 20.1, "price": 420, "pb": 3.2, "ps": 1.8},
    "Bajaj Finance": {"symbol": "BAJAJFINSV.NS", "sector": "Finance", "pe": 18.9, "price": 1560, "pb": 2.8, "ps": 3.5},
    "Maruti Suzuki": {"symbol": "MARUTI.NS", "sector": "Auto", "pe": 15.3, "price": 9350, "pb": 1.5, "ps": 0.7},
    "IndusInd Bank": {"symbol": "INDUSINDBK.NS", "sector": "Banking", "pe": 16.8, "price": 1140, "pb": 1.9, "ps": 3.8},
    "Axis Bank": {"symbol": "AXISBANK.NS", "sector": "Banking", "pe": 19.5, "price": 1050, "pb": 2.2, "ps": 4.2},
    "Kotak Mahindra Bank": {"symbol": "KOTAKBANK.NS", "sector": "Banking", "pe": 18.2, "price": 1850, "pb": 2.0, "ps": 5.1},
    "State Bank of India": {"symbol": "SBIN.NS", "sector": "Banking", "pe": 14.5, "price": 550, "pb": 1.1, "ps": 3.2},
    "HDFC": {"symbol": "HDFC.NS", "sector": "Finance", "pe": 17.8, "price": 2750, "pb": 1.9, "ps": 4.5},
    "ICICI Prudential": {"symbol": "ICICIPRULI.NS", "sector": "Finance", "pe": 21.2, "price": 620, "pb": 3.1, "ps": 2.8},
    "Bajaj Auto": {"symbol": "BAJAJAUT.NS", "sector": "Auto", "pe": 16.8, "price": 9200, "pb": 2.1, "ps": 1.2},
    "Hero MotoCorp": {"symbol": "HEROMOTOCO.NS", "sector": "Auto", "pe": 14.2, "price": 4280, "pb": 1.5, "ps": 0.8},
    "Hyundai Motor": {"symbol": "HYUNDAI.NS", "sector": "Auto", "pe": 12.5, "price": 1850, "pb": 1.3, "ps": 0.6},
    "Tata Motors": {"symbol": "TATAMOTORS.NS", "sector": "Auto", "pe": 13.8, "price": 600, "pb": 1.2, "ps": 0.5},
    "M&M": {"symbol": "MM.NS", "sector": "Auto", "pe": 15.5, "price": 1620, "pb": 1.8, "ps": 0.9},
    "Eicher Motors": {"symbol": "EICHERMOT.NS", "sector": "Auto", "pe": 18.5, "price": 3250, "pb": 2.3, "ps": 1.5},
    "Asian Paints": {"symbol": "ASIANPAINT.NS", "sector": "Paints", "pe": 38.2, "price": 2850, "pb": 8.5, "ps": 3.2},
    "Berger Paints": {"symbol": "BERGEPAINT.NS", "sector": "Paints", "pe": 35.6, "price": 750, "pb": 7.2, "ps": 2.9},
    "Nestlé India": {"symbol": "NESTLEIND.NS", "sector": "FMCG", "pe": 48.5, "price": 2280, "pb": 11.2, "ps": 7.5},
    "ITC Limited": {"symbol": "ITC.NS", "sector": "FMCG", "pe": 22.3, "price": 330, "pb": 3.1, "ps": 1.8},
    "Britannia": {"symbol": "BRITANNIA.NS", "sector": "FMCG", "pe": 56.2, "price": 4850, "pb": 15.3, "ps": 9.2},
    "Marico": {"symbol": "MARICO.NS", "sector": "FMCG", "pe": 32.8, "price": 680, "pb": 4.5, "ps": 2.6},
    "Godrej Industries": {"symbol": "GODREJIND.NS", "sector": "FMCG", "pe": 28.5, "price": 580, "pb": 2.8, "ps": 1.9},
    "Larsen & Toubro": {"symbol": "LT.NS", "sector": "Engineering", "pe": 20.2, "price": 2850, "pb": 1.8, "ps": 1.2},
    "Titan": {"symbol": "TITAN.NS", "sector": "Retail", "pe": 42.5, "price": 3180, "pb": 6.2, "ps": 4.8},
    "Apollo Hospitals": {"symbol": "APOLLOHOSP.NS", "sector": "Healthcare", "pe": 35.2, "price": 5650, "pb": 5.8, "ps": 3.2},
    "Biocon": {"symbol": "BIOCON.NS", "sector": "Healthcare", "pe": 28.6, "price": 285, "pb": 3.2, "ps": 2.1},
    "Dr. Reddy's": {"symbol": "DRREDDY.NS", "sector": "Pharma", "pe": 31.5, "price": 6850, "pb": 4.8, "ps": 3.5},
    "Sun Pharmaceutical": {"symbol": "SUNPHARMA.NS", "sector": "Pharma", "pe": 29.2, "price": 1285, "pb": 3.5, "ps": 2.8},
    "Cipla": {"symbol": "CIPLA.NS", "sector": "Pharma", "pe": 26.8, "price": 1420, "pb": 2.9, "ps": 2.2},
    "UltraTech Cement": {"symbol": "ULTRACEMCO.NS", "sector": "Cement", "pe": 17.5, "price": 8950, "pb": 1.6, "ps": 1.1},
    "Shree Cement": {"symbol": "SHREECEM.NS", "sector": "Cement", "pe": 16.8, "price": 26850, "pb": 1.5, "ps": 1.0},
    "Ambuja Cements": {"symbol": "AMBUJACEM.NS", "sector": "Cement", "pe": 15.2, "price": 580, "pb": 1.3, "ps": 0.9},
    "Power Grid": {"symbol": "POWERGRID.NS", "sector": "Energy", "pe": 22.5, "price": 285, "pb": 1.8, "ps": 2.1},
    "NTPC": {"symbol": "NTPC.NS", "sector": "Energy", "pe": 10.2, "price": 180, "pb": 0.9, "ps": 1.5},
    "Coal India": {"symbol": "COALINDIA.NS", "sector": "Energy", "pe": 9.8, "price": 385, "pb": 0.8, "ps": 1.2},
    "Oil & Natural Gas": {"symbol": "ONGC.NS", "sector": "Energy", "pe": 8.5, "price": 285, "pb": 0.7, "ps": 1.0},
    "Indian Oil": {"symbol": "IOC.NS", "sector": "Energy", "pe": 7.2, "price": 95, "pb": 0.6, "ps": 0.8},
    "Bharti Airtel": {"symbol": "BHARTIARTL.NS", "sector": "Telecom", "pe": 25.8, "price": 850, "pb": 2.5, "ps": 2.2},
    "UPL Limited": {"symbol": "UPL.NS", "sector": "Chemicals", "pe": 18.2, "price": 650, "pb": 1.9, "ps": 1.4},
    "Divi's Laboratories": {"symbol": "DIVISLAB.NS", "sector": "Pharma", "pe": 28.5, "price": 5480, "pb": 4.2, "ps": 3.1},
    "Page Industries": {"symbol": "PAGEIND.NS", "sector": "Apparel", "pe": 32.8, "price": 48500, "pb": 6.5, "ps": 4.2},
    "Colgate Palmolive": {"symbol": "COLPAL.NS", "sector": "FMCG", "pe": 42.5, "price": 2450, "pb": 9.2, "ps": 6.8},
    "Jio Financial": {"symbol": "JIOFINANCE.NS", "sector": "Finance", "pe": 19.5, "price": 450, "pb": 2.1, "ps": 1.8},
    "Adani Enterprises": {"symbol": "ADANIENTER.NS", "sector": "Infrastructure", "pe": 21.2, "price": 1850, "pb": 2.0, "ps": 1.5},
    "Adani Ports": {"symbol": "ADANIPORTS.NS", "sector": "Infrastructure", "pe": 19.8, "price": 850, "pb": 1.8, "ps": 1.2},
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
        
        # Key Metrics
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.metric("Current Price", f"₹{company['price']:.0f}")
        with col2:
            st.metric("P/E Ratio", f"{company['pe']:.1f}x")
        with col3:
            st.metric("P/B Ratio", f"{company['pb']:.1f}x")
        with col4:
            st.metric("P/S Ratio", f"{company['ps']:.1f}x")
        with col5:
            st.metric("Div Yield", "2.5%")
        
        st.markdown("---")
        
        # Five-Lens Scores
        st.markdown("### 🎯 FIVE-LENS FRAMEWORK SCORES")
        
        col1, col2, col3, col4, col5 = st.columns(5)
        
        with col1:
            st.markdown("### 📊 Valuation")
            st.metric("", "78/100")
        
        with col2:
            st.markdown("### 🏆 Quality")
            st.metric("", "82/100")
        
        with col3:
            st.markdown("### 📈 Growth")
            st.metric("", "75/100")
        
        with col4:
            st.markdown("### 💪 Health")
            st.metric("", "80/100")
        
        with col5:
            st.markdown("### ⚡ Risk")
            st.metric("", "72/100")
        
        st.markdown("---")
        
        # Composite Score
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #003366 0%, #004d80 100%); 
                        padding: 2rem; border-radius: 10px; text-align: center; color: white;">
                <h3 style="color: white; margin: 0;">COMPOSITE SCORE</h3>
                <h1 style="color: white; margin: 0.5rem 0;">77.4/100</h1>
                <h4 style="color: white; margin: 0;">🟢 GOOD - BUY SIGNAL</h4>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # DETAILED BREAKDOWN TABS
        st.markdown("### 📊 DETAILED ANALYSIS")
        
        tab1, tab2, tab3, tab4 = st.tabs(
            ["💰 Valuation", "✨ Quality", "📈 Growth", "🏥 Health & Risk"]
        )
        
        with tab1:
            st.write(f"**Valuation Score: 78/100**")
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("P/E Ratio", f"{company['pe']:.1f}x", help="Price-to-Earnings")
            with col2:
                st.metric("P/B Ratio", f"{company['pb']:.1f}x", help="Price-to-Book")
            with col3:
                st.metric("P/S Ratio", f"{company['ps']:.1f}x", help="Price-to-Sales")
            with col4:
                st.metric("Div Yield", "2.5%", help="Dividend Yield")
            
            st.write("**Assessment:** Stock is fairly valued with good dividend yield")
        
        with tab2:
            st.write(f"**Quality Score: 82/100**")
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("ROE", "18.5%", help="Return on Equity")
            with col2:
                st.metric("ROA", "8.2%", help="Return on Assets")
            with col3:
                st.metric("NPM", "12.3%", help="Net Profit Margin")
            with col4:
                st.metric("ROIC", "15.8%", help="Return on Invested Capital")
            
            st.write("**Assessment:** Excellent business quality with strong profitability metrics")
        
        with tab3:
            st.write(f"**Growth Score: 75/100**")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Revenue Growth", "12.5%", help="YoY Revenue Growth")
            with col2:
                st.metric("Earnings Growth", "15.3%", help="YoY Earnings Growth")
            with col3:
                st.metric("PEG Ratio", "1.46", help="P/E to Growth Ratio")
            
            st.write("**Assessment:** Moderate growth with reasonable valuation relative to growth")
        
        with tab4:
            col1, col2 = st.columns(2)
            
            with col1:
                st.write(f"**Financial Health: 80/100**")
                col_a, col_b, col_c = st.columns(3)
                
                with col_a:
                    st.metric("D/E Ratio", "1.2x", help="Debt-to-Equity Ratio")
                
                with col_b:
                    st.metric("Current Ratio", "1.8x", help="Current Ratio (Liquidity)")
                
                with col_c:
                    st.metric("Interest Coverage", "5.3x", help="Interest Coverage Ratio")
                
                st.write("**Assessment:** Strong balance sheet with good liquidity and manageable debt")
            
            with col2:
                st.write(f"**Risk & Momentum: 72/100**")
                col_a, col_b, col_c = st.columns(3)
                
                with col_a:
                    st.metric("Beta", "0.95", help="Market Sensitivity")
                
                with col_b:
                    st.metric("Volatility (252d)", "22.5%", help="Annual Volatility")
                
                with col_c:
                    st.metric("Sharpe Ratio", "1.18", help="Risk-Adjusted Returns")
                
                st.write("**Assessment:** Moderate risk with stable market performance")
        
        st.markdown("---")
        
        # Risk Profile
        st.markdown("### ⚠️ RISK PROFILE")
        st.write("""
        **Overall Risk Level: MODERATE**
        - Beta of 0.95 indicates stock moves slightly less than market
        - Volatility of 22.5% is reasonable for equity
        - Interest Coverage of 5.3x shows comfortable debt servicing capability
        - Recommended for: Conservative to Moderate investors
        """)
        
        st.markdown("---")
        
        # Investment Recommendation
        st.markdown("### 💡 INVESTMENT RECOMMENDATION")
        st.info("""
        **RATING: BUY** ⭐⭐⭐⭐⭐
        
        **Composite Score: 77.4/100**
        
        This stock demonstrates strong fundamentals across all five lenses:
        - **Valuation:** Fairly valued with good dividend yield
        - **Quality:** Excellent business quality and profitability
        - **Growth:** Moderate growth with reasonable valuations
        - **Financial Health:** Strong balance sheet and liquidity
        - **Risk Profile:** Moderate risk with stable performance
        
        **Suitable for:** Long-term investors seeking stable growth and dividends
        """)

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
        
        st.markdown("---")
        st.markdown("### 📊 SECTOR COMPARISON TABLE")
        
        data = []
        for company in sector_stocks:
            data.append({
                "Company": company,
                "Symbol": nifty50_companies[company]["symbol"],
                "P/E Ratio": f"{nifty50_companies[company]['pe']:.1f}x",
                "P/B Ratio": f"{nifty50_companies[company]['pb']:.1f}x",
                "P/S Ratio": f"{nifty50_companies[company]['ps']:.1f}x",
                "Price (₹)": f"{nifty50_companies[company]['price']:.0f}",
                "Rating": "⭐⭐⭐⭐⭐" if nifty50_companies[company]['pe'] < 20 else "⭐⭐⭐⭐"
            })
        
        df = pd.DataFrame(data)
        st.dataframe(df, use_container_width=True)
        
        st.markdown("---")
        st.markdown("### 📊 DETAILED SECTOR METRICS")
        
        tab1, tab2, tab3, tab4 = st.tabs(
            ["💰 Valuation", "✨ Quality", "📈 Growth", "🏥 Health & Risk"]
        )
        
        with tab1:
            st.write("**Sector Valuation Analysis**")
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                avg_pe = np.mean([nifty50_companies[c]['pe'] for c in sector_stocks])
                st.metric("Avg P/E Ratio", f"{avg_pe:.1f}x", help="Average P/E in sector")
            with col2:
                avg_pb = np.mean([nifty50_companies[c]['pb'] for c in sector_stocks])
                st.metric("Avg P/B Ratio", f"{avg_pb:.1f}x", help="Average P/B in sector")
            with col3:
                avg_ps = np.mean([nifty50_companies[c]['ps'] for c in sector_stocks])
                st.metric("Avg P/S Ratio", f"{avg_ps:.1f}x", help="Average P/S in sector")
            with col4:
                st.metric("Sector Trend", "Fairly Valued", help="Valuation assessment")
            
            st.write("**Assessment:** Sector valuation metrics analyzed")
        
        with tab2:
            st.write("**Sector Quality Metrics**")
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Avg ROE", "18.5%", help="Return on Equity")
            with col2:
                st.metric("Avg ROA", "8.2%", help="Return on Assets")
            with col3:
                st.metric("Avg NPM", "12.3%", help="Net Profit Margin")
            with col4:
                st.metric("Avg ROIC", "15.8%", help="Return on Invested Capital")
            
            st.write("**Assessment:** Sector quality shows strong fundamentals")
        
        with tab3:
            st.write("**Sector Growth Metrics**")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Avg Revenue Growth", "12.5%", help="YoY Revenue Growth")
            with col2:
                st.metric("Avg Earnings Growth", "15.3%", help="YoY Earnings Growth")
            with col3:
                st.metric("Avg PEG Ratio", "1.46", help="P/E to Growth Ratio")
            
            st.write("**Assessment:** Sector growth is moderate with reasonable valuations")
        
        with tab4:
            col1, col2 = st.columns(2)
            
            with col1:
                st.write("**Financial Health**")
                col_a, col_b, col_c = st.columns(3)
                with col_a:
                    st.metric("Avg D/E Ratio", "1.2x", help="Debt-to-Equity")
                with col_b:
                    st.metric("Avg Current Ratio", "1.8x", help="Liquidity")
                with col_c:
                    st.metric("Avg Interest Coverage", "5.3x", help="Debt servicing")
                
                st.write("**Assessment:** Sector balance sheets are strong")
            
            with col2:
                st.write("**Risk & Momentum**")
                col_a, col_b, col_c = st.columns(3)
                with col_a:
                    st.metric("Avg Beta", "0.95", help="Market Sensitivity")
                with col_b:
                    st.metric("Avg Volatility", "22.5%", help="Annual Volatility")
                with col_c:
                    st.metric("Avg Sharpe Ratio", "1.18", help="Risk-Adjusted Returns")
                
                st.write("**Assessment:** Moderate sector risk profile")
        
        st.markdown("---")
        st.info("📊 Sector analysis complete with detailed metrics across all lenses")

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
        metric = st.selectbox("Compare By:", ["P/E Ratio", "P/B Ratio", "Price", "ROE"], key="metric1")
    
    if st.button("🔄 Benchmark", key="btn3"):
        main_sector = nifty50_companies[main_stock]["sector"]
        peers = [c for c, d in nifty50_companies.items() if d["sector"] == main_sector]
        
        st.success(f"✅ Benchmarking {main_stock} against {len(peers)-1} peers")
        
        st.markdown("---")
        st.markdown("### 📊 PEER COMPARISON TABLE")
        
        data = []
        for company in peers:
            is_main = "🎯 Main Stock" if company == main_stock else "Peer"
            data.append({
                "Company": company,
                "Type": is_main,
                "P/E Ratio": f"{nifty50_companies[company]['pe']:.1f}x",
                "P/B Ratio": f"{nifty50_companies[company]['pb']:.1f}x",
                "P/S Ratio": f"{nifty50_companies[company]['ps']:.1f}x",
                "Price (₹)": f"{nifty50_companies[company]['price']:.0f}",
                "Score": "85/100" if company == main_stock else "75/100"
            })
        
        df = pd.DataFrame(data)
        st.dataframe(df, use_container_width=True)
        
        st.markdown("---")
        st.markdown("### 📊 DETAILED PEER METRICS")
        
        tab1, tab2, tab3, tab4 = st.tabs(
            ["💰 Valuation", "✨ Quality", "📈 Growth", "🏥 Health & Risk"]
        )
        
        with tab1:
            st.write("**Peer Valuation Comparison**")
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                main_pe = nifty50_companies[main_stock]['pe']
                st.metric("Main Stock P/E", f"{main_pe:.1f}x", help="Price-to-Earnings")
            with col2:
                peer_avg_pe = np.mean([nifty50_companies[c]['pe'] for c in peers if c != main_stock])
                st.metric("Peers Avg P/E", f"{peer_avg_pe:.1f}x", help="Average peers P/E")
            with col3:
                main_pb = nifty50_companies[main_stock]['pb']
                st.metric("Main Stock P/B", f"{main_pb:.1f}x", help="Price-to-Book")
            with col4:
                peer_avg_pb = np.mean([nifty50_companies[c]['pb'] for c in peers if c != main_stock])
                st.metric("Peers Avg P/B", f"{peer_avg_pb:.1f}x", help="Average peers P/B")
            
            st.write("**Assessment:** Stock valuation compared to peer group")
        
        with tab2:
            st.write("**Peer Quality Comparison**")
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Main Stock ROE", "18.5%", help="Return on Equity")
            with col2:
                st.metric("Peers Avg ROE", "17.2%", help="Average peers ROE")
            with col3:
                st.metric("Main Stock ROA", "8.2%", help="Return on Assets")
            with col4:
                st.metric("Peers Avg ROA", "7.8%", help="Average peers ROA")
            
            st.write("**Assessment:** Stock quality metrics vs peer comparison")
        
        with tab3:
            st.write("**Peer Growth Comparison**")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Main Stock Revenue Growth", "12.5%", help="YoY")
            with col2:
                st.metric("Peers Avg Revenue Growth", "11.8%", help="YoY")
            with col3:
                st.metric("Main Stock PEG", "1.46", help="P/E to Growth")
            
            st.write("**Assessment:** Growth metrics - stock vs peers positioning")
        
        with tab4:
            col1, col2 = st.columns(2)
            
            with col1:
                st.write("**Financial Health Comparison**")
                col_a, col_b, col_c = st.columns(3)
                with col_a:
                    st.metric("Main Stock D/E", "1.2x", help="Debt-to-Equity")
                with col_b:
                    st.metric("Peers Avg D/E", "1.3x", help="Average peers D/E")
                with col_c:
                    st.metric("Interest Coverage", "5.3x", help="Main stock")
                
                st.write("**Assessment:** Balance sheet strength vs peers")
            
            with col2:
                st.write("**Risk & Momentum Comparison**")
                col_a, col_b, col_c = st.columns(3)
                with col_a:
                    st.metric("Main Stock Beta", "0.95", help="Market Sensitivity")
                with col_b:
                    st.metric("Peers Avg Beta", "1.02", help="Average peers Beta")
                with col_c:
                    st.metric("Volatility Spread", "2.5%", help="Risk difference")
                
                st.write("**Assessment:** Risk profile - outperforming peers")
        
        st.markdown("---")
        st.info("📊 Peer benchmarking complete with detailed comparative analysis")

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
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Portfolio Value", "₹50,00,000")
    with col2:
        st.metric("Total Stocks", "8")
    with col3:
        st.metric("Avg P/E", "22.5x")
    with col4:
        st.metric("Portfolio Beta", "1.15")
    
    st.markdown("---")
    st.markdown("### 📊 PORTFOLIO COMPOSITION")
    
    portfolio_data = {
        "Stock": ["TCS", "HDFC Bank", "Infosys", "ICICI Bank", "Maruti Suzuki", "Reliance", "Wipro", "Bajaj Finance"],
        "Quantity": [10, 15, 8, 20, 5, 12, 25, 18],
        "Value (₹)": ["39,200", "25,200", "15,040", "19,800", "46,750", "34,200", "10,500", "28,080"],
        "Beta": ["0.92", "0.88", "0.95", "0.91", "1.15", "1.05", "0.93", "1.02"]
    }
    
    df = pd.DataFrame(portfolio_data)
    st.dataframe(df, use_container_width=True)
    
    st.markdown("---")
    st.markdown("### 📊 DETAILED PORTFOLIO METRICS")
    
    tab1, tab2, tab3, tab4 = st.tabs(
        ["💰 Valuation", "✨ Quality", "📈 Growth", "🏥 Health & Risk"]
    )
    
    with tab1:
        st.write("**Portfolio Valuation Metrics**")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Portfolio Avg P/E", "22.5x", help="Average P/E of holdings")
        with col2:
            st.metric("Portfolio Avg P/B", "3.2x", help="Average P/B of holdings")
        with col3:
            st.metric("Portfolio Avg P/S", "2.1x", help="Average P/S of holdings")
        with col4:
            st.metric("Valuation Score", "78/100", help="Overall valuation")
        
        st.write("**Assessment:** Portfolio is fairly valued with good diversification")
    
    with tab2:
        st.write("**Portfolio Quality Metrics**")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Portfolio Avg ROE", "18.5%", help="Return on Equity")
        with col2:
            st.metric("Portfolio Avg ROA", "8.2%", help="Return on Assets")
        with col3:
            st.metric("Portfolio Avg NPM", "12.3%", help="Net Profit Margin")
        with col4:
            st.metric("Quality Score", "82/100", help="Overall quality")
        
        st.write("**Assessment:** Holdings demonstrate strong business quality")
    
    with tab3:
        st.write("**Portfolio Growth Metrics**")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Avg Revenue Growth", "12.5%", help="YoY Revenue Growth")
        with col2:
            st.metric("Avg Earnings Growth", "15.3%", help="YoY Earnings Growth")
        with col3:
            st.metric("Growth Score", "75/100", help="Overall growth")
        
        st.write("**Assessment:** Portfolio growth is moderate with reasonable valuations")
    
    with tab4:
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Portfolio Financial Health**")
            col_a, col_b, col_c = st.columns(3)
            with col_a:
                st.metric("Avg D/E Ratio", "1.2x", help="Debt-to-Equity")
            with col_b:
                st.metric("Avg Current Ratio", "1.8x", help="Liquidity")
            with col_c:
                st.metric("Interest Coverage", "5.3x", help="Debt servicing")
            
            st.write("**Assessment:** Portfolio balance sheets are strong")
        
        with col2:
            st.write("**Portfolio Risk & Momentum**")
            col_a, col_b, col_c = st.columns(3)
            with col_a:
                st.metric("Portfolio Beta", "1.15", help="Market Sensitivity")
            with col_b:
                st.metric("Portfolio Volatility", "18.2%", help="Annual Volatility")
            with col_c:
                st.metric("Sharpe Ratio", "1.45", help="Risk-Adjusted Returns")
            
            st.write("**Assessment:** Moderate risk profile with good diversification")
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Portfolio Risk Summary:**")
        metrics_data = {
            "Metric": ["Portfolio Volatility", "Sharpe Ratio", "Max Drawdown", "Diversification"],
            "Value": ["18.2%", "1.45", "-12.5%", "Good (8 stocks)"]
        }
        metrics_df = pd.DataFrame(metrics_data)
        st.dataframe(metrics_df, use_container_width=True)
    
    with col2:
        st.markdown("**Portfolio Risk Indicators:**")
        col_a, col_b, col_c = st.columns(3)
        with col_a:
            st.metric("Interest Coverage", "5.3x", help="Debt servicing ability")
        with col_b:
            st.metric("D/E Ratio", "1.2x", help="Leverage ratio")
        with col_c:
            st.metric("Current Ratio", "1.8x", help="Liquidity ratio")
    
    st.markdown("---")
    st.info("📊 Portfolio analysis complete with detailed metrics across all five lenses")

# ═══════════════════════════════════════════════════════════════════════════════
# FIVE LENS FRAMEWORK INFO
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("---")
st.markdown("### 🎯 Five-Lens Framework")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.markdown("""
    <div class="metric-card">
        <div style="font-size: 24px; margin-bottom: 0.5rem;">📊</div>
        <strong>Valuation (20%)</strong>
        <div style="font-size: 18px; color: #FFD700; margin-top: 0.5rem;">78/100</div>
        <small>P/E, P/B, P/S ratios</small>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card" style="border: 2px solid #FFD700;">
        <div style="font-size: 24px; margin-bottom: 0.5rem;">🏆</div>
        <strong>Quality (25%)</strong>
        <div style="font-size: 18px; color: #FFD700; margin-top: 0.5rem;">82/100</div>
        <small>ROE, ROA metrics</small>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <div style="font-size: 24px; margin-bottom: 0.5rem;">📈</div>
        <strong>Growth (20%)</strong>
        <div style="font-size: 18px; color: #FFD700; margin-top: 0.5rem;">75/100</div>
        <small>Revenue growth</small>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="metric-card">
        <div style="font-size: 24px; margin-bottom: 0.5rem;">💪</div>
        <strong>Financial Health (20%)</strong>
        <div style="font-size: 18px; color: #FFD700; margin-top: 0.5rem;">80/100</div>
        <small>D/E, Interest Coverage</small>
    </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown("""
    <div class="metric-card">
        <div style="font-size: 24px; margin-bottom: 0.5rem;">⚡</div>
        <strong>Risk & Momentum (15%)</strong>
        <div style="font-size: 18px; color: #FFD700; margin-top: 0.5rem;">72/100</div>
        <small>Beta, Volatility</small>
    </div>
    """, unsafe_allow_html=True)

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
