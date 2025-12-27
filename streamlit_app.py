
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
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 0rem 1rem;
    }
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
    h1 {
        color: #003366;
        border-bottom: 3px solid #003366;
        padding-bottom: 0.5rem;
    }
    h2 {
        color: #003366;
        margin-top: 1.5rem;
    }
    </style>
""", unsafe_allow_html=True)

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

# ═══════════════════════════════════════════════════════════════════════════════
# MAIN APP
# ═══════════════════════════════════════════════════════════════════════════════

# Header
col1, col2 = st.columns([3, 1])
with col1:
    st.title("🏔️ THE MOUNTAIN PATH - WORLD OF FINANCE")
    st.markdown("### Stock Analysis Platform with Advanced Risk Metrics")
with col2:
    st.metric("Updated", datetime.now().strftime("%H:%M:%S"))

st.markdown("---")

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
                
                # Calculate risk metrics
                risk_metrics = RiskMetricsCalculator.calculate_all_risk_metrics(
                    price_hist['Close'],
                    market_data if market_data is not None else None,
                    stock_data.get('current_price')
                )
                
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
                    st.metric("Current Price", f"₹{stock_data.get('current_price', 'N/A'):.2f}")
                
                with col2:
                    st.metric("P/E Ratio", f"{stock_data.get('pe_ratio', 'N/A'):.1f}x" 
                             if stock_data.get('pe_ratio') else "N/A")
                
                with col3:
                    st.metric("P/B Ratio", f"{stock_data.get('pb_ratio', 'N/A'):.2f}x"
                             if stock_data.get('pb_ratio') else "N/A")
                
                with col4:
                    yield_pct = (stock_data.get('dividend_yield', 0) or 0) * 100
                    st.metric("Div Yield", f"{yield_pct:.2f}%" if yield_pct else "N/A")
                
                with col5:
                    st.metric("Market Cap", f"₹{(stock_data.get('market_cap', 0) or 0)/1e9:.1f}B" 
                             if stock_data.get('market_cap') else "N/A")
                
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
                        st.metric("P/E Ratio", f"{stock_data.get('pe_ratio', 'N/A'):.1f}x"
                                 if stock_data.get('pe_ratio') else "N/A")
                    with col2:
                        st.metric("P/B Ratio", f"{stock_data.get('pb_ratio', 'N/A'):.2f}x"
                                 if stock_data.get('pb_ratio') else "N/A")
                    with col3:
                        st.metric("P/S Ratio", f"{stock_data.get('ps_ratio', 'N/A'):.2f}x"
                                 if stock_data.get('ps_ratio') else "N/A")
                    with col4:
                        st.metric("Div Yield", f"{((stock_data.get('dividend_yield', 0) or 0)*100):.2f}%")
                
                with tab2:
                    st.write(f"**Quality Score: {lens_scores.quality:.1f}/100**")
                    col1, col2, col3, col4 = st.columns(4)
                    with col1:
                        st.metric("ROE", f"{((financial_metrics.get('roe', 0) or 0)*100):.1f}%")
                    with col2:
                        st.metric("NPM", f"{((financial_metrics.get('npm', 0) or 0)*100):.1f}%")
                    with col3:
                        st.metric("ROA", f"{((financial_metrics.get('roa', 0) or 0)*100):.1f}%")
                    with col4:
                        st.metric("ROIC", f"{((financial_metrics.get('roic', 0) or 0)*100):.1f}%")
                
                with tab3:
                    st.write(f"**Growth Score: {lens_scores.growth:.1f}/100**")
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Revenue Growth", f"{((financial_metrics.get('revenue_growth_yoy', 0) or 0)*100):.1f}%")
                    with col2:
                        st.metric("Earnings Growth", f"{((financial_metrics.get('earnings_growth_yoy', 0) or 0)*100):.1f}%")
                    with col3:
                        st.metric("PEG Ratio", f"{financial_metrics.get('peg_ratio', 'N/A'):.2f}"
                                 if financial_metrics.get('peg_ratio') else "N/A")
                
                with tab4:
                    col1, col2 = st.columns(2)
                    with col1:
                        st.write(f"**Financial Health Score: {lens_scores.financial_health:.1f}/100**")
                        col_a, col_b, col_c = st.columns(3)
                        with col_a:
                            st.metric("D/E Ratio", f"{financial_metrics.get('debt_to_equity', 'N/A'):.2f}"
                                     if financial_metrics.get('debt_to_equity') else "N/A")
                        with col_b:
                            st.metric("Current Ratio", f"{financial_metrics.get('current_ratio', 'N/A'):.2f}"
                                     if financial_metrics.get('current_ratio') else "N/A")
                        with col_c:
                            st.metric("Interest Coverage", f"{financial_metrics.get('interest_coverage', 'N/A'):.2f}x"
                                     if financial_metrics.get('interest_coverage') else "N/A")
                    
                    with col2:
                        st.write(f"**Risk & Momentum Score: {lens_scores.risk_momentum:.1f}/100**")
                        col_a, col_b, col_c = st.columns(3)
                        with col_a:
                            st.metric("Beta", f"{risk_metrics.get('beta', 1.0):.2f}x")
                        with col_b:
                            st.metric("Volatility (252d)", f"{(risk_metrics.get('volatility_252d', 0.25)*100):.1f}%")
                        with col_c:
                            st.metric("Sharpe Ratio", f"{risk_metrics.get('sharpe_ratio', 0.5):.2f}")
                
                st.markdown("---")
                
                # Risk Profile Summary
                st.markdown("### ⚠️ RISK PROFILE")
                risk_summary = RiskMetricsCalculator.risk_profile_summary(risk_metrics)
                st.write(risk_summary)
                
                # Investment Recommendation
                st.markdown("### 💡 INVESTMENT RECOMMENDATION")
                recommendation = framework.generate_recommendation(lens_scores, stock_data)
                st.markdown(recommendation)

# ═══════════════════════════════════════════════════════════════════════════════
# MODE 2: SECTOR COMPARISON
# ═════════════════════════════════════════════════════════════════════════════

elif analysis_mode == "Sector Comparison":
    
    st.markdown("### 📊 SECTOR COMPARISON")
    
    registry = DataFetcher.get_nifty50_registry()
    sectors = sorted(set(data['sector'] for data in registry.values()))
    
    selected_sector = st.selectbox("Select Sector:", sectors)
    
    sector_companies = {name: data for name, data in registry.items() 
                       if data['sector'] == selected_sector}
    
    if st.button("🔍 Analyze Sector", type="primary"):
        
        all_results = []
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        for i, (company_name, company_data) in enumerate(sector_companies.items()):
            
            progress = (i + 1) / len(sector_companies)
            progress_bar.progress(progress)
            status_text.text(f"Analyzing {company_name}... ({i+1}/{len(sector_companies)})")
            
            symbol = company_data['symbol']
            price_hist, info = DataFetcher.fetch_stock_data(symbol, "1y")
            market_data = DataFetcher.fetch_market_index("^NSEI", "1y")
            
            if price_hist is not None:
                stock_data = DataFetcher.extract_stock_data(info, price_hist)
                financial_metrics = DataFetcher.extract_financial_metrics(info)
                risk_metrics = RiskMetricsCalculator.calculate_all_risk_metrics(
                    price_hist['Close'], market_data, stock_data.get('current_price')
                )
                
                framework = FiveLensFramework()
                lens_scores = framework.evaluate_stock(stock_data, financial_metrics, risk_metrics)
                
                all_results.append({
                    'Company': company_name,
                    'Symbol': symbol,
                    'Composite': lens_scores.composite,
                    'Valuation': lens_scores.valuation,
                    'Quality': lens_scores.quality,
                    'Growth': lens_scores.growth,
                    'Health': lens_scores.financial_health,
                    'Risk': lens_scores.risk_momentum,
                    'Price': stock_data.get('current_price'),
                    'P/E': stock_data.get('pe_ratio'),
                })
        
        progress_bar.empty()
        status_text.empty()
        
        if all_results:
            df_results = pd.DataFrame(all_results).sort_values('Composite', ascending=False)
            
            # Display table
            st.markdown("### Rankings by Composite Score")
            st.dataframe(df_results, use_container_width=True)
            
            # Visualization
            col1, col2 = st.columns(2)
            
            with col1:
                fig = px.bar(df_results, x='Company', y='Composite', 
                            color='Composite', color_continuous_scale='RdYlGn',
                            title="Composite Scores Comparison")
                fig.update_layout(height=400)
                st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                fig = go.Figure()
                for col in ['Valuation', 'Quality', 'Growth', 'Health', 'Risk']:
                    fig.add_trace(go.Box(y=df_results[col], name=col))
                fig.update_layout(title="Score Distribution", height=400)
                st.plotly_chart(fig, use_container_width=True)

# ═════════════════════════════════════════════════════════════════════════════
# MODE 3: PEER BENCHMARKING
# ═════════════════════════════════════════════════════════════════════════════

elif analysis_mode == "Peer Benchmarking":
    
    st.markdown("### 🏆 PEER BENCHMARKING")
    
    registry = DataFetcher.get_nifty50_registry()
    selected_stocks = st.multiselect(
        "Select stocks to compare:",
        sorted(registry.keys()),
        default=list(sorted(registry.keys()))[:3]
    )
    
    if st.button("📊 Generate Benchmark Report", type="primary"):
        
        all_data = []
        progress_bar = st.progress(0)
        
        for i, company_name in enumerate(selected_stocks):
            
            progress = (i + 1) / len(selected_stocks)
            progress_bar.progress(progress)
            
            symbol = registry[company_name]['symbol']
            price_hist, info = DataFetcher.fetch_stock_data(symbol, "1y")
            market_data = DataFetcher.fetch_market_index("^NSEI", "1y")
            
            if price_hist is not None:
                stock_data = DataFetcher.extract_stock_data(info, price_hist)
                financial_metrics = DataFetcher.extract_financial_metrics(info)
                risk_metrics = RiskMetricsCalculator.calculate_all_risk_metrics(
                    price_hist['Close'], market_data, stock_data.get('current_price')
                )
                
                framework = FiveLensFramework()
                lens_scores = framework.evaluate_stock(stock_data, financial_metrics, risk_metrics)
                
                all_data.append({
                    'Company': company_name,
                    'Valuation': lens_scores.valuation,
                    'Quality': lens_scores.quality,
                    'Growth': lens_scores.growth,
                    'Financial Health': lens_scores.financial_health,
                    'Risk & Momentum': lens_scores.risk_momentum,
                    'Composite': lens_scores.composite,
                })
        
        progress_bar.empty()
        
        if all_data:
            df_bench = pd.DataFrame(all_data)
            
            # Heatmap
            fig = px.imshow(df_bench.set_index('Company')[['Valuation', 'Quality', 'Growth', 
                                                             'Financial Health', 'Risk & Momentum']].T,
                           color_continuous_scale='RdYlGn',
                           text_auto='.1f',
                           title="Peer Comparison Heatmap")
            st.plotly_chart(fig, use_container_width=True)
            
            # Radar comparison
            fig = go.Figure()
            for _, row in df_bench.iterrows():
                fig.add_trace(go.Scatterpolar(
                    r=[row['Valuation'], row['Quality'], row['Growth'], 
                       row['Financial Health'], row['Risk & Momentum']],
                    theta=['Valuation', 'Quality', 'Growth', 'Financial Health', 'Risk & Momentum'],
                    fill='toself',
                    name=row['Company']
                ))
            
            fig.update_layout(
                polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
                title="Peer Comparison Radar",
                height=500
            )
            st.plotly_chart(fig, use_container_width=True)
            
            # Table
            st.dataframe(df_bench.sort_values('Composite', ascending=False), use_container_width=True)

# ═════════════════════════════════════════════════════════════════════════════
# MODE 4: PORTFOLIO RISK
# ═════════════════════════════════════════════════════════════════════════════

elif analysis_mode == "Portfolio Risk":
    
    st.markdown("### 📈 PORTFOLIO RISK ANALYSIS")
    
    registry = DataFetcher.get_nifty50_registry()
    
    col1, col2 = st.columns([3, 1])
    with col1:
        portfolio_stocks = st.multiselect(
            "Select stocks for portfolio:",
            sorted(registry.keys()),
            default=list(sorted(registry.keys()))[:5]
        )
    
    with col2:
        if st.button("Calculate", type="primary"):
            st.session_state.calculate_portfolio = True
    
    if 'calculate_portfolio' in st.session_state:
        
        # Get weights
        st.markdown("**Portfolio Weights**")
        col_names = st.columns(len(portfolio_stocks))
        weights = {}
        
        for i, stock in enumerate(portfolio_stocks):
            with col_names[i]:
                weight = st.number_input(
                    f"{stock}",
                    min_value=0.0,
                    max_value=100.0,
                    value=100.0/len(portfolio_stocks),
                    step=1.0
                )
                weights[stock] = weight / 100.0
        
        # Normalize
        total_weight = sum(weights.values())
        weights = {k: v/total_weight for k, v in weights.items()}
        
        if st.button("🔍 Analyze Portfolio Risk", type="primary"):
            
            all_prices = {}
            progress_bar = st.progress(0)
            
            for i, stock in enumerate(portfolio_stocks):
                progress = (i + 1) / len(portfolio_stocks)
                progress_bar.progress(progress)
                
                symbol = registry[stock]['symbol']
                price_hist, _ = DataFetcher.fetch_stock_data(symbol, "1y")
                
                if price_hist is not None:
                    all_prices[stock] = price_hist['Close']
            
            progress_bar.empty()
            
            if all_prices:
                # Calculate portfolio metrics
                st.markdown("### Portfolio Risk Metrics")
                
                # Individual volatilities
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.write("**Individual Stock Volatilities**")
                    for stock, prices in all_prices.items():
                        vol = RiskMetricsCalculator.calculate_volatility(prices)
                        st.metric(stock, f"{vol*100:.1f}%")
                
                with col2:
                    st.write("**Portfolio Weights**")
                    for stock, weight in weights.items():
                        st.metric(stock, f"{weight*100:.1f}%")
                
                with col3:
                    st.write("**Price Momentum (52w)**")
                    for stock, prices in all_prices.items():
                        if len(prices) > 252:
                            momentum = (prices.iloc[-1] - prices.iloc[-252]) / prices.iloc[-252]
                            st.metric(stock, f"{momentum*100:+.1f}%")
                
                # Correlation matrix
                st.markdown("### Correlation Matrix")
                corr_matrix = RiskMetricsCalculator.calculate_correlation_matrix(all_prices)
                
                fig = px.imshow(corr_matrix,
                               color_continuous_scale='RdBu',
                               text_auto='.2f',
                               title="Stock Correlation Matrix",
                               zmin=-1, zmax=1)
                st.plotly_chart(fig, use_container_width=True)
                
                # Summary statistics
                st.markdown("### Summary Statistics")
                summary_data = []
                for stock, prices in all_prices.items():
                    summary_data.append({
                        'Stock': stock,
                        'Return': f"{((prices.iloc[-1] / prices.iloc[0] - 1)*100):+.1f}%",
                        'Volatility': f"{RiskMetricsCalculator.calculate_volatility(prices)*100:.1f}%",
                        'Max Drawdown': f"{RiskMetricsCalculator.calculate_drawdown(prices)[0]*100:.1f}%",
                    })
                
                df_summary = pd.DataFrame(summary_data)
                st.dataframe(df_summary, use_container_width=True)

# ═════════════════════════════════════════════════════════════════════════════
# FOOTER
# ═════════════════════════════════════════════════════════════════════════════

st.markdown("---")
st.markdown("""
    <div style="text-align: center; color: #666; padding: 2rem;">
        <p><strong>THE MOUNTAIN PATH - WORLD OF FINANCE</strong></p>
        <p>Advanced Stock Analysis Platform with Five-Lens Framework</p>
        <p>Prof. V. Ravichandran | 28+ Years Finance Experience</p>
        <p style="font-size: 0.8rem; margin-top: 1rem;">
            Disclaimer: This tool is for educational purposes. Not financial advice. 
            Always consult with a qualified financial advisor before making investment decisions.
        </p>
    </div>
""", unsafe_allow_html=True)
