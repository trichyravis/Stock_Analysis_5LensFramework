# 🏔️ THE MOUNTAIN PATH - WORLD OF FINANCE

## Advanced Stock Analysis Platform with Five-Lens Framework

**Prof. V. Ravichandran**  
*28+ Years Corporate Finance & Banking Experience*  
*10+ Years Academic Excellence*

---

## 📋 TABLE OF CONTENTS

1. [Overview](#overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Framework Details](#framework-details)
6. [Risk Metrics](#risk-metrics)
7. [Architecture](#architecture)

---

## 🎯 OVERVIEW

This is a **production-ready Streamlit application** for analyzing Indian Nifty 50 stocks using an advanced **Five-Lens Framework** with comprehensive risk metrics.

The platform combines:
- **Live data** from Yahoo Finance
- **Advanced risk analytics** (VaR, CVaR, Sharpe Ratio, Beta, etc.)
- **Multi-dimensional stock evaluation** across 5 key lenses
- **Professional visualizations** with Plotly
- **Institutional-grade risk management** tools

---

## ✨ FEATURES

### 1. **Single Stock Analysis**
   - Comprehensive evaluation of any Nifty 50 stock
   - Five-Lens Framework scoring (0-100)
   - Radar chart visualization
   - Price trend analysis
   - Risk profile summary
   - Investment recommendation

### 2. **Sector Comparison**
   - Analyze all stocks in a sector
   - Comparative rankings
   - Score distribution analysis
   - Identify best performers

### 3. **Peer Benchmarking**
   - Compare multiple stocks side-by-side
   - Heatmap and radar visualizations
   - Identify relative strengths/weaknesses

### 4. **Portfolio Risk Analysis**
   - Portfolio-level risk metrics
   - Correlation analysis
   - Diversification benefits
   - Summary statistics

---

## 🚀 INSTALLATION

### Prerequisites
- Python 3.8+
- pip package manager
- Internet connection (for live data)

### Step 1: Clone Repository
```bash
git clone <repository-url>
cd the-mountain-path
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run Streamlit App
```bash
streamlit run streamlit_app.py
```

The app will open at: **http://localhost:8501**

---

## 📊 USAGE GUIDE

### Mode 1: Single Stock Analysis
1. Select a company from dropdown
2. Choose analysis period (1Y, 2Y, 5Y)
3. Click "Analyze Stock"
4. Review comprehensive analysis results

**Output includes:**
- Five-Lens scores
- Composite investment signal
- Detailed financial metrics
- Risk profile
- Investment recommendation

### Mode 2: Sector Comparison
1. Select sector from list
2. Click "Analyze Sector"
3. View rankings and comparisons
4. Identify best performers in sector

### Mode 3: Peer Benchmarking
1. Select 2+ stocks for comparison
2. Click "Generate Benchmark Report"
3. Compare across all dimensions
4. View heatmaps and radar charts

### Mode 4: Portfolio Risk
1. Select stocks for portfolio
2. Set portfolio weights
3. Click "Analyze Portfolio Risk"
4. Review correlation and risk metrics

---

## 🎯 FIVE-LENS FRAMEWORK

### Framework Overview

Each stock is evaluated across **5 dimensions** with **0-100 scoring**:

#### **LENS 1: VALUATION LENS (20% weight)**
Evaluates if stock is overpriced or underpriced

**Metrics:**
- P/E Ratio (Price-to-Earnings)
- P/B Ratio (Price-to-Book)
- Dividend Yield
- P/S Ratio (Price-to-Sales)

**Scoring Logic:**
- P/E: Excellent (10-15x) → 90 points
- P/B: Fair value (1.5-3.0) → 80 points
- Dividend: Good yield (2-3%) → 85 points
- P/S: Low multiple (<2x) → 90 points

**Use Case:** Find undervalued stocks with margin of safety

---

#### **LENS 2: QUALITY LENS (25% weight)**
Evaluates quality of business and earnings

**Metrics:**
- Return on Equity (ROE)
- Net Profit Margin (NPM)
- Return on Invested Capital (ROIC)
- Earnings Quality

**Scoring Logic:**
- ROE: Excellent (>25%) → 95 points
- NPM: Good (10-15%) → 90 points
- ROIC: Strong (>15%) → 90 points
- ROA: High (>10%) → 95 points

**Use Case:** Identify high-quality businesses with sustainable competitive advantages

---

#### **LENS 3: GROWTH LENS (20% weight)**
Evaluates growth prospects and momentum

**Metrics:**
- Revenue Growth YoY
- Earnings Growth YoY
- PEG Ratio (P/E to Growth)

**Scoring Logic:**
- Revenue Growth: Strong (10-15%) → 85 points
- Earnings Growth: Excellent (15-25%) → 90 points
- PEG Ratio: Fair (<1.0) → 95 points

**Use Case:** Find growth stocks with expanding margins

---

#### **LENS 4: FINANCIAL HEALTH LENS (20% weight)**
Evaluates solvency, liquidity, and stability

**Metrics:**
- Debt-to-Equity Ratio
- Current Ratio (Liquidity)
- Interest Coverage Ratio
- Free Cash Flow

**Scoring Logic:**
- D/E: Optimal (0.5-1.0) → 90 points
- Current Ratio: Healthy (1.5-2.5) → 90 points
- Interest Coverage: Strong (>5x) → 90 points
- FCF: Positive → 75 points

**Use Case:** Assess financial stability and bankruptcy risk

---

#### **LENS 5: RISK & MOMENTUM LENS (15% weight)**
Evaluates volatility, risk profile, and price momentum

**Metrics:**
- Beta (Systematic Risk)
- Volatility (252-day annualized)
- Sharpe Ratio (Risk-adjusted Return)
- Price Momentum (52-week)

**Scoring Logic:**
- Beta: Low (0.7-1.0) → 90 points
- Volatility: Moderate (<20%) → 80 points
- Sharpe: Good (0.5-1.0) → 85 points
- Momentum: Positive (10-25%) → 80 points

**Use Case:** Manage portfolio risk and identify stable vs. volatile stocks

---

### Composite Score Interpretation

```
85-100  : 🚀 Strong Buy   (Excellent across all lenses)
75-84   : ✅ Buy          (Good fundamentals, reasonable risk)
65-74   : 🟡 Hold/Accumulate (Fairly valued, monitor)
50-64   : ⚠️  Watch        (Mixed signals, caution needed)
<50     : 🔴 Avoid        (Significant concerns)
```

---

## 📊 RISK METRICS

### Value-at-Risk (VaR)

**Definition:** Maximum expected loss at given confidence level

**Calculation:** 95% VaR = Daily loss not expected to exceed X in 19 out of 20 days

**Example:** VaR 95% = -5% means daily loss likely to exceed 5% only 5% of the time

**Methods:**
- Historical: Percentile-based (empirical)
- Parametric: Normal distribution assumption
- Cornish-Fisher: Adjusted for skewness/kurtosis

---

### Conditional Value-at-Risk (CVaR) / Expected Shortfall

**Definition:** Average loss given that loss exceeds VaR

**Use Case:** More conservative risk measure than VaR

**Example:** CVaR 95% = -8% means when losses exceed 5%, average loss is -8%

---

### Sharpe Ratio

**Formula:** (Return - Risk-free Rate) / Volatility

**Interpretation:**
- >1.0: Excellent risk-adjusted return
- 0.5-1.0: Good risk-adjusted return
- <0.5: Moderate/poor risk-adjusted return

---

### Sortino Ratio

**Definition:** Like Sharpe but only penalizes downside volatility

**Advantage:** Doesn't penalize positive volatility (upside)

---

### Beta

**Definition:** Stock volatility relative to market

- Beta = 1.0: Moves with market
- Beta < 1.0: Less volatile (defensive)
- Beta > 1.0: More volatile (aggressive)

---

### Maximum Drawdown

**Definition:** Largest peak-to-trough decline in price

**Interpretation:**
- <-10%: Good (low drawdown)
- -10% to -20%: Moderate (acceptable)
- <-20%: High (significant risk)

---

### Calmar Ratio

**Formula:** Annual Return / |Maximum Drawdown|

**Use Case:** Compare risk-adjusted returns considering drawdown

---

## 🏗️ ARCHITECTURE

### Module Structure

```
the-mountain-path/
├── streamlit_app.py          # Main application
├── five_lens_framework.py    # Framework scoring logic
├── risk_metrics.py           # Risk calculation engine
├── data_fetcher.py           # Data retrieval & caching
├── requirements.txt          # Dependencies
└── README.md                 # Documentation
```

### Data Flow

```
User Input
    ↓
Data Fetcher (yfinance with caching)
    ↓
Stock Data Extraction
    ↓
Risk Metrics Calculation
    ├─ Volatility
    ├─ VaR/CVaR
    ├─ Beta
    ├─ Sharpe Ratio
    └─ Drawdown Analysis
    ↓
Five-Lens Framework Evaluation
    ├─ Valuation Lens
    ├─ Quality Lens
    ├─ Growth Lens
    ├─ Financial Health Lens
    └─ Risk & Momentum Lens
    ↓
Scoring & Composite Calculation
    ↓
Visualization & Recommendations
    ↓
User Interface (Streamlit)
```

---

## 📈 KEY TECHNOLOGIES

| Technology | Purpose |
|-----------|---------|
| **Streamlit** | Web application framework |
| **yfinance** | Live market data |
| **Pandas** | Data manipulation |
| **NumPy** | Numerical computing |
| **SciPy** | Statistical analysis |
| **Plotly** | Interactive visualizations |

---

## ⚙️ CONFIGURATION

### Risk-Free Rate
- Default: 6% annually
- Location: `risk_metrics.py` line 20
- Adjust based on current Indian government security yields

### Analysis Period
- Options: 1Y, 2Y, 5Y
- Default: 1 Year
- Adjust for longer/shorter analysis windows

### Stock Registry
- Contains 40+ Nifty 50 stocks
- Location: `data_fetcher.py` - `get_nifty50_registry()`
- Add/remove companies as needed

---

## 🔍 TROUBLESHOOTING

### Issue: "yfinance library not found"
```bash
pip install yfinance
```

### Issue: "No data available"
- Check internet connection
- Verify stock symbol is correct
- Try another time (market hours recommended)

### Issue: Slow data loading
- First run fetches data from internet
- Subsequent runs use 5-minute cache
- Clear cache: Delete `.streamlit` folder

### Issue: Limited financial metrics
- Some metrics only available for large-cap stocks
- Use default values for analysis
- Focus on available metrics

---

## 📚 EDUCATIONAL USE

This platform is designed for:
- MBA Finance courses
- CFA exam preparation
- FRM (Financial Risk Management) studies
- Investment analysis training
- Portfolio management education

---

## 📝 DISCLAIMER

**IMPORTANT:** This tool is for **educational and informational purposes only**. 

- NOT financial or investment advice
- Past performance ≠ Future results
- Always consult qualified financial advisor
- Investment involves risk, including capital loss
- Do your own research (DYOR)

**Use responsibly and at your own risk.**

---

## 👨‍🏫 ABOUT THE AUTHOR

**Prof. V. Ravichandran**

- 28+ Years Corporate Finance & Banking Experience
- 10+ Years Academic Excellence
- Expertise in:
  - Financial Risk Management
  - Derivatives Valuation
  - Fixed Income Analysis
  - Advanced Financial Modeling
  - Python for Finance

---

## 📞 SUPPORT

For issues, suggestions, or improvements:
- GitHub Issues: [Repository]
- Email: [Contact Information]

---

## 📜 LICENSE

[Your License Here]

---

**Happy Analyzing! 🚀**

*"The mountain path of finance is walked one step at a time, with wisdom and patience."*
