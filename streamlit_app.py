
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
from datetime import datetime, timedelta
import plotly.graph_objects as go
import plotly.express as px
from five_lens_framework import FiveLensFramework
from risk_metrics import RiskMetricsCalculator
from data_fetcher import DataFetcher

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
# ENHANCED CUSTOM CSS - BIG PROMINENT HEADER
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
    <style>
    .main {
        padding: 0rem 1rem;
    }
    
    /* ════════════════════════════════════════════════════════════ */
    /* HERO HEADER - BIG AND PROMINENT */
    /* ════════════════════════════════════════════════════════════ */
    
    .hero-title {
        background: linear-gradient(135deg, #003366 0%, #004d80 50%, #003366 100%);
        padding: 4rem 2rem;
        border-radius: 20px;
        text-align: center;
        margin: 0rem 0rem 2rem 0rem;
        box-shadow: 0 12px 30px rgba(0, 51, 102, 0.4);
        border: 4px solid #003366;
    }
    
    /* Mountain emoji - HUGE AND ANIMATED */
    .mountain-emoji {
        font-size: 160px;
        margin-bottom: 1.5rem;
        display: block;
        animation: float 3s ease-in-out infinite;
        text-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
    }
    
    /* Main title - VERY LARGE */
    .hero-title h1 {
        font-size: 56px;
        font-weight: 900;
        color: white;
        margin: 0.3rem 0;
        text-shadow: 3px 3px 10px rgba(0, 0, 0, 0.5);
        letter-spacing: 3px;
        line-height: 1.2;
    }
    
    /* Subtitle */
    .hero-title p {
        font-size: 18px;
        color: #E0F0FF;
        margin: 0.7rem 0;
        font-weight: 500;
        letter-spacing: 1px;
    }
    
    /* Floating animation */
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-25px); }
    }
    
    /* ════════════════════════════════════════════════════════════ */
    /* METRIC CARDS */
    /* ════════════════════════════════════════════════════════════ */
    
    .metric-card {
        background: linear-gradient(135deg, #003366 0%, #004d80 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
    }
    
    .score-excellent {
        background: linear-gradient(135deg, #00d084 0%, #00a860 100%);
    }
    .score-good {
        background: linear-gradient(135deg, #0084ff 0%, #0066cc 100%);
    }
    .score-fair {
        background: linear-gradient(135deg, #ffa500 0%, #ff8c00 100%);
    }
    .score-poor {
        background: linear-gradient(135deg, #ff4757 0%, #ff3838 100%);
    }
    
    /* ════════════════════════════════════════════════════════════ */
    /* HEADINGS */
    /* ════════════════════════════════════════════════════════════ */
    
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
    
    /* ════════════════════════════════════════════════════════════ */
    /* TABS */
    /* ════════════════════════════════════════════════════════════ */
    
    .stTabs [data-baseweb="tab-list"] {
        gap: 2px;
    }
    
    [data-testid="stTab"] {
        padding: 1rem;
        font-weight: 600;
        color: #003366;
    }
    
    /* ════════════════════════════════════════════════════════════ */
    /* TIME DISPLAY */
    /* ════════════════════════════════════════════════════════════ */
    
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
    
    </style>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# ENHANCED HERO HEADER - BIG AND PROMINENT
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
    <div class="hero-title">
        <div class="mountain-emoji">🏔️</div>
        <h1>THE MOUNTAIN PATH</h1>
        <h1 style="margin-top: -0.5rem; margin-bottom: 1.5rem;">WORLD OF FINANCE</h1>
        <p>Stock Analysis Platform Using Five Lens Framework</p>
        <p style="font-size: 16px;">Valuation (20%) • Quality (25%) • Growth (20%) • Financial Health (20%) • Risk & Momentum (15%)</p>
    </div>
""", unsafe_allow_html=True)

# Time display
st.markdown(f"""
    <div class="time-display">
    📊 Last Updated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# ═══════════════════════════════════════════════════════════════════════════════
# SIDEBAR
# ═══════════════════════════════════════════════════════════════════════════════

st.sidebar.markdown("---")
st.sidebar.write("### 📊 STOCK ANALYSIS TOOL")
st.sidebar.write("Advanced Five-Lens Framework with Risk Metrics")
st.sidebar.markdown("---")

# Select analysis mode
analysis_mode = st.sidebar.radio(
    "Select Mode:",
    ["Single Stock Analysis", "Sector Comparison", "Peer Benchmarking", "Portfolio Risk"]
)

st.sidebar.markdown("---")
st.sidebar.write("**About This Tool**")
st.sidebar.write(
    """
    This platform uses the Five-Lens Framework to evaluate stocks:
    - 🎯 **Valuation Lens** (20%)
    - ✨ **Quality Lens** (25%)
    - 📈 **Growth Lens** (20%)
    - 💪 **Financial Health** (20%)
    - ⚡ **Risk & Momentum** (15%)
    """
)

st.sidebar.markdown("---")
st.sidebar.write("**Prof. V. Ravichandran**")
st.sidebar.write("*28+ Years Finance Experience*")
st.sidebar.write("*10+ Years Academic Excellence*")

# LinkedIn Profile Link
st.sidebar.markdown("""
    <a href="https://www.linkedin.com/in/trichyravis" target="_blank" 
       style="display: inline-block; margin-top: 1rem; padding: 0.5rem 1rem; 
              background: linear-gradient(135deg, #0077b5 0%, #0a66c2 100%); 
              color: white; text-decoration: none; border-radius: 5px; 
              font-weight: 600; text-align: center;">
       🔗 LinkedIn Profile
    </a>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# MODE 1: SINGLE STOCK ANALYSIS
# ═══════════════════════════════════════════════════════════════════════════════

if analysis_mode == "Single Stock Analysis":
    
    # Get registry
    registry = DataFetcher.get_nifty50_registry()
    company_names = sorted(registry.keys())
    
    # Select stock
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        selected_company = st.selectbox(
            "Select Company:",
            company_names,
            index=0
        )
    
    with col2:
        period = st.selectbox("Period:", ["1y", "2y", "5y"])
    
    with col3:
        analyze_btn = st.button("🔍 Analyze Stock", type="primary")
    
    if analyze_btn or 'current_stock' in st.session_state:
        st.session_state.current_stock = selected_company
        
        with st.spinner(f"Fetching data for {selected_company}..."):
            
            company_data = registry[selected_company]
            symbol = company_data['symbol']
            
            # Fetch data
            price_hist, info = DataFetcher.fetch_stock_data(symbol, period)
            market_data = DataFetcher.fetch_market_index("^NSEI", period)
            
            if price_hist is None:
                st.error(f"❌ Could not fetch data for {selected_company}")
                st.info("Please check your internet connection or try another stock.")
            else:
                
                # Extract data
                stock_data = DataFetcher.extract_stock_data(info, price_hist)
                financial_metrics = DataFetcher.extract_financial_metrics(info)
                
                # ✅ Calculate Beta
                beta = DataFetcher.calculate_beta(selected_company, price_hist, market_data)
                
                # Calculate risk metrics
                risk_metrics = RiskMetricsCalculator.calculate_all_risk_metrics(
                    price_hist['Close'],
                    market_data if market_data is not None else None,
                    stock_data.get('current_price')
                )
                
                # ✅ Add beta to risk metrics
                risk_metrics['beta'] = beta
                
                # Evaluate using Five-Lens Framework
                framework = FiveLensFramework()
                lens_scores = framework.evaluate_stock(stock_data, financial_metrics, risk_metrics)
                
                # ═════════════════════════════════════════════════════════════
                # DISPLAY RESULTS
                # ═════════════════════════════════════════════════════════════
                
                st.markdown(f"## {selected_company} ({symbol})")
                
                # Key Metrics Row
                col1, col2, col3, col4, col5 = st.columns(5)
                
                with col1:
                    current_price = stock_data.get('current_price')
                    if current_price:
                        st.metric("Current Price", f"₹{current_price:.2f}")
                    else:
                        st.metric("Current Price", "N/A")
                
                with col2:
                    pe_ratio = stock_data.get('pe_ratio')
                    if pe_ratio and not np.isnan(pe_ratio):
                        st.metric("P/E Ratio", f"{pe_ratio:.1f}x")
                    else:
                        st.metric("P/E Ratio", "N/A")
                
                with col3:
                    pb_ratio = stock_data.get('pb_ratio')
                    if pb_ratio and not np.isnan(pb_ratio):
                        st.metric("P/B Ratio", f"{pb_ratio:.2f}x")
                    else:
                        st.metric("P/B Ratio", "N/A")
                
                with col4:
                    div_yield = stock_data.get('dividend_yield') or 0
                    yield_pct = div_yield * 100
                    st.metric("Div Yield", f"{yield_pct:.2f}%")
                
                with col5:
                    market_cap = stock_data.get('market_cap')
                    if market_cap:
                        st.metric("Market Cap", f"₹{market_cap/1e9:.1f}B")
                    else:
                        st.metric("Market Cap", "N/A")
                
                st.markdown("---")
                
                # Five-Lens Scores
                st.markdown("### 🎯 FIVE-LENS FRAMEWORK SCORES")
                
                col1, col2, col3, col4, col5 = st.columns(5)
                
                def score_color(score):
                    if score >= 80:
                        return "🟢"
                    elif score >= 70:
                        return "🔵"
                    elif score >= 60:
                        return "🟡"
                    else:
                        return "🔴"
                
                with col1:
                    st.markdown(f"### {score_color(lens_scores.valuation)} Valuation")
                    st.metric("", f"{lens_scores.valuation:.1f}/100")
                
                with col2:
                    st.markdown(f"### {score_color(lens_scores.quality)} Quality")
                    st.metric("", f"{lens_scores.quality:.1f}/100")
                
                with col3:
                    st.markdown(f"### {score_color(lens_scores.growth)} Growth")
                    st.metric("", f"{lens_scores.growth:.1f}/100")
                
                with col4:
                    st.markdown(f"### {score_color(lens_scores.financial_health)} Health")
                    st.metric("", f"{lens_scores.financial_health:.1f}/100")
                
                with col5:
                    st.markdown(f"### {score_color(lens_scores.risk_momentum)} Risk")
                    st.metric("", f"{lens_scores.risk_momentum:.1f}/100")
                
                # Composite Score
                signal, color = FiveLensFramework.get_signal(lens_scores.composite)
                col1, col2, col3 = st.columns([1, 2, 1])
                with col2:
                    st.markdown(f"""
                    <div style="background: linear-gradient(135deg, #003366 0%, #004d80 100%); 
                                padding: 2rem; border-radius: 10px; text-align: center; color: white;">
                        <h3 style="color: white; margin: 0;">COMPOSITE SCORE</h3>
                        <h1 style="color: white; margin: 0.5rem 0;">{lens_scores.composite:.1f}/100</h1>
                        <h4 style="color: white; margin: 0;">{signal}</h4>
                    </div>
                    """, unsafe_allow_html=True)
                
                st.markdown("---")
                
                # Visualization
                col1, col2 = st.columns(2)
                
                with col1:
                    # Radar Chart
                    scores_dict = lens_scores.to_dict()
                    scores_dict.pop('Composite Score')
                    
                    fig = go.Figure(data=go.Scatterpolar(
                        r=list(scores_dict.values()),
                        theta=list(scores_dict.keys()),
                        fill='toself',
                        name='Score'
                    ))
                    
                    fig.update_layout(
                        polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
                        title="Five-Lens Framework Radar",
                        height=400
                    )
                    
                    st.plotly_chart(fig, use_container_width=True)
                
                with col2:
                    # Price Chart
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(
                        x=price_hist.index,
                        y=price_hist['Close'],
                        mode='lines',
                        name='Price',
                        line=dict(color='#003366', width=2)
                    ))
                    
                    fig.update_layout(
                        title="Price Trend",
                        xaxis_title="Date",
                        yaxis_title="Price (₹)",
                        height=400,
                        hovermode='x unified'
                    )
                    
                    st.plotly_chart(fig, use_container_width=True)
                
                st.markdown("---")
                
                # Detailed Breakdown
                st.markdown("### 📊 DETAILED ANALYSIS")
                
                tab1, tab2, tab3, tab4 = st.tabs(
                    ["Valuation", "Quality", "Growth", "Financial Health & Risk"]
                )
                
                with tab1:
                    st.write(f"**Valuation Score: {lens_scores.valuation:.1f}/100**")
                    col1, col2, col3, col4 = st.columns(4)
                    with col1:
                        pe_ratio = stock_data.get('pe_ratio')
                        if pe_ratio and not np.isnan(pe_ratio):
                            st.metric("P/E Ratio", f"{pe_ratio:.1f}x")
                        else:
                            st.metric("P/E Ratio", "N/A")
                    with col2:
                        pb_ratio = stock_data.get('pb_ratio')
                        if pb_ratio and not np.isnan(pb_ratio):
                            st.metric("P/B Ratio", f"{pb_ratio:.2f}x")
                        else:
                            st.metric("P/B Ratio", "N/A")
                    with col3:
                        ps_ratio = stock_data.get('ps_ratio')
                        if ps_ratio and not np.isnan(ps_ratio):
                            st.metric("P/S Ratio", f"{ps_ratio:.2f}x")
                        else:
                            st.metric("P/S Ratio", "N/A")
                    with col4:
                        div_yield = stock_data.get('dividend_yield') or 0
                        st.metric("Div Yield", f"{(div_yield*100):.2f}%")
                
                with tab2:
                    st.write(f"**Quality Score: {lens_scores.quality:.1f}/100**")
                    col1, col2, col3, col4 = st.columns(4)
                    with col1:
                        roe = financial_metrics.get('roe') or 0
                        st.metric("ROE", f"{(roe*100):.1f}%")
                    with col2:
                        npm = financial_metrics.get('npm') or 0
                        st.metric("NPM", f"{(npm*100):.1f}%")
                    with col3:
                        roa = financial_metrics.get('roa') or 0
                        st.metric("ROA", f"{(roa*100):.1f}%")
                    with col4:
                        roic = financial_metrics.get('roic') or 0
                        st.metric("ROIC", f"{(roic*100):.1f}%")
                
                with tab3:
                    st.write(f"**Growth Score: {lens_scores.growth:.1f}/100**")
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        rev_growth = financial_metrics.get('revenue_growth_yoy') or 0
                        st.metric("Revenue Growth", f"{(rev_growth*100):.1f}%")
                    with col2:
                        earnings_growth = financial_metrics.get('earnings_growth_yoy') or 0
                        st.metric("Earnings Growth", f"{(earnings_growth*100):.1f}%")
                    with col3:
                        peg = financial_metrics.get('peg_ratio')
                        if peg and not np.isnan(peg):
                            st.metric("PEG Ratio", f"{peg:.2f}")
                        else:
                            st.metric("PEG Ratio", "N/A")
                
                with tab4:
                    col1, col2 = st.columns(2)
                    with col1:
                        st.write(f"**Financial Health Score: {lens_scores.financial_health:.1f}/100**")
                        col_a, col_b, col_c = st.columns(3)
                        
                        with col_a:
                            de_ratio = financial_metrics.get('debt_to_equity')
                            if de_ratio is not None and not np.isnan(de_ratio):
                                st.metric("D/E Ratio", f"{de_ratio:.2f}")
                            else:
                                st.metric("D/E Ratio", "N/A", help="Balance sheet data unavailable")
                        
                        with col_b:
                            cr = financial_metrics.get('current_ratio')
                            if cr is not None and not np.isnan(cr):
                                st.metric("Current Ratio", f"{cr:.2f}")
                            else:
                                st.metric("Current Ratio", "N/A", help="Balance sheet data unavailable")
                        
                        with col_c:
                            ic = financial_metrics.get('interest_coverage')
                            if ic is not None and not np.isnan(ic):
                                st.metric("Interest Coverage", f"{ic:.2f}x")
                            else:
                                st.metric("Interest Coverage", "N/A", help="Financial data unavailable")
                    
                    with col2:
                        st.write(f"**Risk & Momentum Score: {lens_scores.risk_momentum:.1f}/100**")
                        col_a, col_b, col_c = st.columns(3)
                        
                        with col_a:
                            if beta is not None and not np.isnan(beta):
                                st.metric("Beta", f"{beta:.2f}x")
                            else:
                                st.metric("Beta", "N/A", help="Market data not available")
                        
                        with col_b:
                            volatility = risk_metrics.get('volatility_252d', 0.25)
                            st.metric("Volatility (252d)", f"{(volatility*100):.1f}%")
                        
                        with col_c:
                            sharpe = risk_metrics.get('sharpe_ratio', 0.5)
                            st.metric("Sharpe Ratio", f"{sharpe:.2f}")
                
                st.markdown("---")
                
                # Risk Profile Summary
                st.markdown("### ⚠️ RISK PROFILE")
                risk_summary = RiskMetricsCalculator.risk_profile_summary(risk_metrics)
                st.write(risk_summary)
                
                # Investment Recommendation
                st.markdown("### 💡 INVESTMENT RECOMMENDATION")
                recommendation = framework.generate_recommendation(lens_scores, stock_data)
                st.markdown(recommendation)

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
