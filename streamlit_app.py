
"""
═══════════════════════════════════════════════════════════════════════════════
THE MOUNTAIN PATH - WORLD OF FINANCE
Nifty 50 Stock Analysis Platform - Enhanced Landing Page
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
# PROFESSIONAL CUSTOM CSS - LANDING PAGE DESIGN
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
    <style>
    .main {
        padding: 0rem 0rem;
    }
    
    /* ════════════════════════════════════════════════════════════ */
    /* LANDING PAGE HERO SECTION */
    /* ════════════════════════════════════════════════════════════ */
    
    .landing-hero {
        background: linear-gradient(180deg, #001f3f 0%, #003d7a 40%, #00547a 100%);
        padding: 4rem 2rem;
        text-align: center;
        margin: 0;
        min-height: 600px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        position: relative;
    }
    
    /* Mountain emoji */
    .landing-mountain {
        font-size: 140px;
        margin-bottom: 2rem;
        animation: float 3s ease-in-out infinite;
        text-shadow: 0 8px 20px rgba(0, 0, 0, 0.4);
    }
    
    /* Main title */
    .landing-title {
        font-size: 56px;
        font-weight: 900;
        color: white;
        margin: 1rem 0;
        text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.5);
        letter-spacing: 2px;
    }
    
    /* Subtitle with gold color */
    .landing-subtitle {
        font-size: 40px;
        color: #FFD700;
        margin: 0.5rem 0 1.5rem 0;
        font-weight: 600;
        letter-spacing: 1px;
        text-shadow: 1px 1px 4px rgba(0, 0, 0, 0.3);
    }
    
    /* Tagline */
    .landing-tagline {
        font-size: 22px;
        color: #E0F0FF;
        margin: 1rem 0 3rem 0;
        font-weight: 400;
        letter-spacing: 0.5px;
    }
    
    /* Five lens cards container */
    .five-lens-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
        gap: 1.5rem;
        margin: 3rem 0;
        max-width: 1200px;
    }
    
    /* Lens card styling */
    .lens-card {
        background: linear-gradient(135deg, rgba(0, 51, 102, 0.6) 0%, rgba(0, 77, 128, 0.6) 100%);
        border: 2px solid rgba(255, 255, 255, 0.2);
        border-radius: 12px;
        padding: 1.5rem;
        text-align: center;
        transition: all 0.3s ease;
        color: white;
    }
    
    .lens-card:hover {
        border-color: rgba(255, 215, 0, 0.6);
        transform: translateY(-5px);
        box-shadow: 0 8px 20px rgba(255, 215, 0, 0.3);
    }
    
    /* Quality card special styling (highest weight) */
    .lens-card.quality-card {
        background: linear-gradient(135deg, rgba(255, 215, 0, 0.2) 0%, rgba(184, 134, 11, 0.2) 100%);
        border: 2px solid rgba(255, 215, 0, 0.6);
        box-shadow: 0 0 20px rgba(255, 215, 0, 0.4);
    }
    
    .lens-card.quality-card:hover {
        box-shadow: 0 8px 30px rgba(255, 215, 0, 0.6);
    }
    
    /* Lens icon */
    .lens-icon {
        font-size: 48px;
        margin-bottom: 1rem;
    }
    
    /* Lens name */
    .lens-name {
        font-size: 18px;
        font-weight: 600;
        margin: 0.5rem 0;
    }
    
    /* Lens percentage */
    .lens-percentage {
        font-size: 14px;
        color: #FFD700;
        font-weight: 600;
    }
    
    /* Action buttons */
    .button-container {
        margin: 3rem 0;
        display: flex;
        gap: 1.5rem;
        justify-content: center;
        flex-wrap: wrap;
    }
    
    .cta-button {
        padding: 0.75rem 2rem;
        font-size: 16px;
        font-weight: 600;
        border-radius: 8px;
        border: none;
        cursor: pointer;
        transition: all 0.3s ease;
        text-decoration: none;
        display: inline-block;
    }
    
    .button-primary {
        background: linear-gradient(135deg, #FFD700 0%, #FFA500 100%);
        color: #003366;
    }
    
    .button-primary:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(255, 215, 0, 0.4);
    }
    
    .button-secondary {
        background: transparent;
        color: white;
        border: 2px solid white;
    }
    
    .button-secondary:hover {
        background: rgba(255, 255, 255, 0.1);
        border-color: #FFD700;
        color: #FFD700;
    }
    
    /* ════════════════════════════════════════════════════════════ */
    /* MAIN APP STYLING */
    /* ════════════════════════════════════════════════════════════ */
    
    .app-header {
        padding: 1rem;
        background: linear-gradient(135deg, #003366 0%, #004d80 100%);
        border-radius: 10px;
        margin: 1rem;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #003366 0%, #004d80 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
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
    /* FLOATING ANIMATION */
    /* ════════════════════════════════════════════════════════════ */
    
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-25px); }
    }
    
    /* ════════════════════════════════════════════════════════════ */
    /* RESPONSIVE DESIGN */
    /* ════════════════════════════════════════════════════════════ */
    
    @media (max-width: 768px) {
        .landing-hero {
            min-height: 400px;
            padding: 2rem 1rem;
        }
        
        .landing-mountain {
            font-size: 100px;
            margin-bottom: 1rem;
        }
        
        .landing-title {
            font-size: 42px;
        }
        
        .landing-subtitle {
            font-size: 28px;
        }
        
        .landing-tagline {
            font-size: 18px;
        }
        
        .five-lens-container {
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 1rem;
        }
    }
    
    @media (max-width: 480px) {
        .landing-hero {
            min-height: 300px;
        }
        
        .landing-mountain {
            font-size: 80px;
        }
        
        .landing-title {
            font-size: 32px;
        }
        
        .landing-subtitle {
            font-size: 22px;
        }
        
        .five-lens-container {
            grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
        }
    }
    
    </style>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# SESSION STATE FOR APP MODE
# ═══════════════════════════════════════════════════════════════════════════════

if 'show_landing' not in st.session_state:
    st.session_state.show_landing = True

# ═══════════════════════════════════════════════════════════════════════════════
# LANDING PAGE
# ═══════════════════════════════════════════════════════════════════════════════

if st.session_state.show_landing:
    
    st.markdown("""
        <div class="landing-hero">
            <div class="landing-mountain">🏔️</div>
            <div class="landing-title">THE MOUNTAIN PATH</div>
            <div class="landing-subtitle">World of Finance</div>
            <div class="landing-tagline">Your Intelligent Stock Analysis Platform</div>
            
            <div class="five-lens-container">
                <div class="lens-card">
                    <div class="lens-icon">📊</div>
                    <div class="lens-name">Valuation</div>
                    <div class="lens-percentage">(20%)</div>
                </div>
                
                <div class="lens-card quality-card">
                    <div class="lens-icon">🏆</div>
                    <div class="lens-name">Quality</div>
                    <div class="lens-percentage">(25%)</div>
                </div>
                
                <div class="lens-card">
                    <div class="lens-icon">📈</div>
                    <div class="lens-name">Growth</div>
                    <div class="lens-percentage">(20%)</div>
                </div>
                
                <div class="lens-card">
                    <div class="lens-icon">💰</div>
                    <div class="lens-name">Financial Health</div>
                    <div class="lens-percentage">(20%)</div>
                </div>
                
                <div class="lens-card">
                    <div class="lens-icon">⚡</div>
                    <div class="lens-name">Risk & Momentum</div>
                    <div class="lens-percentage">(15%)</div>
                </div>
            </div>
            
            <div class="button-container">
                <button class="cta-button button-primary" onclick="document.querySelector('button').click()">
                    📊 Explore Stocks
                </button>
                <button class="cta-button button-secondary">
                    Learn Framework →
                </button>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Add buttons to navigate
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        if st.button("🚀 Launch Stock Analysis Platform", key="launch_app", use_container_width=True):
            st.session_state.show_landing = False
            st.rerun()

# ═══════════════════════════════════════════════════════════════════════════════
# MAIN APP
# ═══════════════════════════════════════════════════════════════════════════════

else:
    
    # Back to landing button
    if st.button("← Back to Home", key="back_home"):
        st.session_state.show_landing = True
        st.rerun()
    
    st.markdown("---")
    
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
                
                # Calculate Beta
                beta = DataFetcher.calculate_beta(selected_company, price_hist, market_data)
                
                # Calculate risk metrics
                risk_metrics = RiskMetricsCalculator.calculate_all_risk_metrics(
                    price_hist['Close'],
                    market_data if market_data is not None else None,
                    stock_data.get('current_price')
                )
                
                # Add beta to risk metrics
                risk_metrics['beta'] = beta
                
                # Evaluate using Five-Lens Framework
                framework = FiveLensFramework()
                lens_scores = framework.evaluate_stock(stock_data, financial_metrics, risk_metrics)
                
                # DISPLAY RESULTS
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

# ═════════════════════════════════════════════════════════════════════════════════
# SIDEBAR
# ═════════════════════════════════════════════════════════════════════════════════

st.sidebar.markdown("---")
st.sidebar.write("### 📊 STOCK ANALYSIS TOOL")
st.sidebar.write("Advanced Five-Lens Framework")
st.sidebar.markdown("---")

st.sidebar.write("**About This Tool**")
st.sidebar.write(
    """
    Five-Lens Framework:
    - 🎯 Valuation (20%)
    - ✨ Quality (25%)
    - 📈 Growth (20%)
    - 💪 Financial Health (20%)
    - ⚡ Risk & Momentum (15%)
    """
)

st.sidebar.markdown("---")
st.sidebar.write("**Prof. V. Ravichandran**")
st.sidebar.write("*28+ Years Finance Experience*")
st.sidebar.write("*10+ Years Academic Excellence*")

st.sidebar.markdown("""
    <a href="https://www.linkedin.com/in/trichyravis" target="_blank" 
       style="display: inline-block; margin-top: 1rem; padding: 0.5rem 1rem; 
              background: linear-gradient(135deg, #0077b5 0%, #0a66c2 100%); 
              color: white; text-decoration: none; border-radius: 5px; 
              font-weight: 600; text-align: center;">
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
