
"""
═══════════════════════════════════════════════════════════════════════════════
THE MOUNTAIN PATH - WORLD OF FINANCE
Nifty 50 Stock Analysis Platform - With Dynamic Portfolio Management
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
    
    /* HERO HEADER - COMPACT DESIGN */
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
# SESSION STATE FOR PORTFOLIO
# ═══════════════════════════════════════════════════════════════════════════════

if 'portfolio' not in st.session_state:
    st.session_state.portfolio = []

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
    "Reliance Industries": {"symbol": "RELIANCE.NS", "sector": "Energy", "pe": 18.5, "price": 2850, "pb": 1.8, "ps": 0.9, "beta": 1.05},
    "TCS": {"symbol": "TCS.NS", "sector": "IT", "pe": 22.3, "price": 3920, "pb": 4.2, "ps": 3.1, "beta": 0.92},
    "HDFC Bank": {"symbol": "HDFCBANK.NS", "sector": "Banking", "pe": 25.1, "price": 1680, "pb": 3.5, "ps": 5.2, "beta": 0.88},
    "Infosys": {"symbol": "INFY.NS", "sector": "IT", "pe": 24.8, "price": 1880, "pb": 3.8, "ps": 2.9, "beta": 0.95},
    "ICICI Bank": {"symbol": "ICICIBANK.NS", "sector": "Banking", "pe": 20.2, "price": 990, "pb": 2.1, "ps": 4.5, "beta": 0.91},
    "Hindustan Unilever": {"symbol": "HINDUNILVR.NS", "sector": "FMCG", "pe": 45.6, "price": 2320, "pb": 12.5, "ps": 8.2, "beta": 0.85},
    "Wipro": {"symbol": "WIPRO.NS", "sector": "IT", "pe": 20.1, "price": 420, "pb": 3.2, "ps": 1.8, "beta": 0.93},
    "Bajaj Finance": {"symbol": "BAJAJFINSV.NS", "sector": "Finance", "pe": 18.9, "price": 1560, "pb": 2.8, "ps": 3.5, "beta": 1.02},
    "Maruti Suzuki": {"symbol": "MARUTI.NS", "sector": "Auto", "pe": 15.3, "price": 9350, "pb": 1.5, "ps": 0.7, "beta": 1.15},
    "IndusInd Bank": {"symbol": "INDUSINDBK.NS", "sector": "Banking", "pe": 16.8, "price": 1140, "pb": 1.9, "ps": 3.8, "beta": 0.98},
}

sectors = sorted(list(set([v["sector"] for v in nifty50_companies.values()])))
companies = sorted(nifty50_companies.keys())

# ═══════════════════════════════════════════════════════════════════════════════
# MODE 1: SINGLE STOCK ANALYSIS (ABBREVIATED)
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
            st.metric("P/B Ratio", f"{company['pb']:.1f}x")
        with col4:
            st.metric("P/S Ratio", f"{company['ps']:.1f}x")
        with col5:
            st.metric("Beta", f"{company['beta']:.2f}")
        
        st.markdown("---")
        st.markdown("### 🎯 FIVE-LENS FRAMEWORK SCORES")
        
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.metric("Valuation", "78/100")
        with col2:
            st.metric("Quality", "82/100")
        with col3:
            st.metric("Growth", "75/100")
        with col4:
            st.metric("Health", "80/100")
        with col5:
            st.metric("Risk", "72/100")

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
        
        data = []
        for company in sector_stocks:
            data.append({
                "Company": company,
                "Symbol": nifty50_companies[company]["symbol"],
                "P/E Ratio": f"{nifty50_companies[company]['pe']:.1f}x",
                "P/B Ratio": f"{nifty50_companies[company]['pb']:.1f}x",
                "Price (₹)": f"{nifty50_companies[company]['price']:.0f}",
                "Rating": "⭐⭐⭐⭐⭐" if nifty50_companies[company]['pe'] < 20 else "⭐⭐⭐⭐"
            })
        
        df = pd.DataFrame(data)
        st.dataframe(df, use_container_width=True)

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
        metric = st.selectbox("Compare By:", ["P/E Ratio", "P/B Ratio", "Price", "Beta"], key="metric1")
    
    if st.button("🔄 Benchmark", key="btn3"):
        main_sector = nifty50_companies[main_stock]["sector"]
        peers = [c for c, d in nifty50_companies.items() if d["sector"] == main_sector]
        
        st.success(f"✅ Benchmarking {main_stock} against {len(peers)-1} peers")
        
        data = []
        for company in peers:
            is_main = "🎯 Main Stock" if company == main_stock else "Peer"
            data.append({
                "Company": company,
                "Type": is_main,
                "P/E Ratio": f"{nifty50_companies[company]['pe']:.1f}x",
                "Beta": f"{nifty50_companies[company]['beta']:.2f}",
                "Score": "85/100" if company == main_stock else "75/100"
            })
        
        df = pd.DataFrame(data)
        st.dataframe(df, use_container_width=True)

# ═══════════════════════════════════════════════════════════════════════════════
# MODE 4: PORTFOLIO RISK - WITH DYNAMIC PORTFOLIO MANAGEMENT
# ═══════════════════════════════════════════════════════════════════════════════

elif analysis_mode == "Portfolio Risk":
    st.markdown("### 💼 Portfolio Risk Analysis")
    st.write("Build and analyze your stock portfolio with dynamic add/remove functionality")
    
    st.markdown("---")
    st.markdown("#### ➕ ADD STOCKS TO YOUR PORTFOLIO")
    
    col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
    
    with col1:
        add_stock = st.selectbox("Select Stock to Add:", companies, key="port_stock_add")
    
    with col2:
        add_qty = st.number_input("Qty:", min_value=1, max_value=10000, value=10, key="qty_add", step=1)
    
    with col3:
        add_price = st.number_input("Price (₹):", min_value=100, max_value=50000, value=int(nifty50_companies[add_stock]["price"]), key="price_add", step=10)
    
    with col4:
        if st.button("➕ ADD", key="btn_add", use_container_width=True):
            # Check if stock already exists
            existing = [p for p in st.session_state.portfolio if p["company"] == add_stock]
            
            if existing:
                st.warning(f"⚠️ {add_stock} already in portfolio. Delete first to add again with different values.")
            else:
                investment_value = add_qty * add_price
                st.session_state.portfolio.append({
                    "company": add_stock,
                    "symbol": nifty50_companies[add_stock]["symbol"],
                    "qty": add_qty,
                    "price": add_price,
                    "value": investment_value,
                    "beta": nifty50_companies[add_stock]["beta"],
                    "sector": nifty50_companies[add_stock]["sector"]
                })
                st.success(f"✅ Added {add_qty} shares of {add_stock} @ ₹{add_price} = ₹{investment_value:,.0f}")
                st.rerun()
    
    st.markdown("---")
    
    # Display Portfolio if it has items
    if st.session_state.portfolio:
        st.markdown("#### 📋 YOUR PORTFOLIO COMPOSITION")
        
        # Create portfolio dataframe
        portfolio_df = []
        total_value = 0
        total_beta_weighted = 0
        
        for item in st.session_state.portfolio:
            portfolio_df.append({
                "Company": item["company"],
                "Symbol": item["symbol"],
                "Quantity": item["qty"],
                "Entry Price (₹)": f"{item['price']:.0f}",
                "Value (₹)": f"{item['value']:,.0f}",
                "Sector": item["sector"],
                "Beta": f"{item['beta']:.2f}"
            })
            total_value += item["value"]
            total_beta_weighted += item["value"] * item["beta"]
        
        df = pd.DataFrame(portfolio_df)
        st.dataframe(df, use_container_width=True)
        
        st.markdown("---")
        
        # Portfolio Summary Metrics
        st.markdown("#### 📊 PORTFOLIO METRICS")
        
        col1, col2, col3, col4, col5 = st.columns(5)
        
        with col1:
            st.metric("Total Value", f"₹{total_value:,.0f}")
        
        with col2:
            st.metric("# of Stocks", len(st.session_state.portfolio))
        
        with col3:
            avg_price = total_value / sum(item["qty"] for item in st.session_state.portfolio) if st.session_state.portfolio else 0
            st.metric("Avg Price", f"₹{avg_price:,.0f}")
        
        with col4:
            portfolio_beta = total_beta_weighted / total_value if total_value > 0 else 0
            st.metric("Portfolio Beta", f"{portfolio_beta:.2f}")
        
        with col5:
            # Sector count
            sectors_in_portfolio = len(set(item["sector"] for item in st.session_state.portfolio))
            st.metric("# of Sectors", sectors_in_portfolio)
        
        st.markdown("---")
        
        # Portfolio Risk Analysis
        st.markdown("#### ⚠️ PORTFOLIO RISK ANALYSIS")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Risk Metrics:**")
            risk_data = {
                "Metric": [
                    "Portfolio Volatility",
                    "Sharpe Ratio",
                    "Max Drawdown",
                    "Interest Coverage"
                ],
                "Value": [
                    f"{18.2 + (portfolio_beta - 1) * 5:.1f}%",
                    f"{1.45 - (portfolio_beta - 1) * 0.3:.2f}",
                    "-12.5%",
                    "5.3x"
                ]
            }
            risk_df = pd.DataFrame(risk_data)
            st.dataframe(risk_df, use_container_width=True)
        
        with col2:
            st.markdown("**Health Indicators:**")
            col_a, col_b, col_c = st.columns(3)
            with col_a:
                st.metric("D/E Ratio", "1.2x")
            with col_b:
                st.metric("Current Ratio", "1.8x")
            with col_c:
                st.metric("Risk Level", "MODERATE" if portfolio_beta < 1.2 else "HIGH")
        
        st.markdown("---")
        
        # Sector Diversification
        st.markdown("#### 🏭 SECTOR DIVERSIFICATION")
        
        sector_breakdown = {}
        for item in st.session_state.portfolio:
            sector = item["sector"]
            value = item["value"]
            if sector not in sector_breakdown:
                sector_breakdown[sector] = 0
            sector_breakdown[sector] += value
        
        sector_data = []
        for sector, value in sector_breakdown.items():
            pct = (value / total_value * 100) if total_value > 0 else 0
            sector_data.append({
                "Sector": sector,
                "Value (₹)": f"{value:,.0f}",
                "% of Portfolio": f"{pct:.1f}%",
                "Status": "✅ Good" if pct < 40 else "⚠️ Concentrated"
            })
        
        sector_df = pd.DataFrame(sector_data)
        st.dataframe(sector_df, use_container_width=True)
        
        st.markdown("---")
        
        # Delete Stock Section
        st.markdown("#### ❌ REMOVE STOCKS FROM PORTFOLIO")
        
        col1, col2 = st.columns([3, 1])
        
        with col1:
            stock_to_delete = st.selectbox(
                "Select stock to remove:",
                options=[item["company"] for item in st.session_state.portfolio],
                key="delete_stock"
            )
        
        with col2:
            if st.button("❌ DELETE", key="btn_delete", use_container_width=True):
                st.session_state.portfolio = [p for p in st.session_state.portfolio if p["company"] != stock_to_delete]
                st.success(f"✅ Removed {stock_to_delete} from portfolio")
                st.rerun()
        
        st.markdown("---")
        
        # Clear Portfolio Button
        if st.button("🗑️ CLEAR ALL PORTFOLIO", key="btn_clear_all"):
            st.session_state.portfolio = []
            st.success("✅ Portfolio cleared!")
            st.rerun()
    
    else:
        st.info("📊 Your portfolio is empty. Add stocks above to start analyzing!")
        st.write("Once you add stocks, you'll see:")
        st.write("- Portfolio composition table")
        st.write("- Total value and metrics")
        st.write("- Risk analysis")
        st.write("- Sector diversification")
        st.write("- Option to delete individual stocks or clear all")

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
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card" style="border: 2px solid #FFD700;">
        <div style="font-size: 24px; margin-bottom: 0.5rem;">🏆</div>
        <strong>Quality (25%)</strong>
        <div style="font-size: 18px; color: #FFD700; margin-top: 0.5rem;">82/100</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <div style="font-size: 24px; margin-bottom: 0.5rem;">📈</div>
        <strong>Growth (20%)</strong>
        <div style="font-size: 18px; color: #FFD700; margin-top: 0.5rem;">75/100</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="metric-card">
        <div style="font-size: 24px; margin-bottom: 0.5rem;">💪</div>
        <strong>Financial Health (20%)</strong>
        <div style="font-size: 18px; color: #FFD700; margin-top: 0.5rem;">80/100</div>
    </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown("""
    <div class="metric-card">
        <div style="font-size: 24px; margin-bottom: 0.5rem;">⚡</div>
        <strong>Risk & Momentum (15%)</strong>
        <div style="font-size: 18px; color: #FFD700; margin-top: 0.5rem;">72/100</div>
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
        </p>
        <p style="font-size: 0.8rem; margin-top: 1rem;">
            Disclaimer: This tool is for educational purposes. Not financial advice. 
            Always consult with a qualified financial advisor before making investment decisions.
        </p>
    </div>
""", unsafe_allow_html=True)
