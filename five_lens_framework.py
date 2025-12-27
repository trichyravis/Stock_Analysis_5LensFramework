"""
═══════════════════════════════════════════════════════════════════════════════
THE MOUNTAIN PATH - WORLD OF FINANCE
Five-Lens Framework for Stock Analysis
Advanced Scoring Model with Risk Metrics
═══════════════════════════════════════════════════════════════════════════════

Prof. V. Ravichandran
28+ Years Corporate Finance & Banking Experience
10+ Years Academic Excellence
"""

import numpy as np
import pandas as pd
from dataclasses import dataclass
from typing import Dict, Tuple, Optional
import warnings
warnings.filterwarnings('ignore')


@dataclass
class LensScores:
    """Container for five-lens scores"""
    valuation: float
    quality: float
    growth: float
    financial_health: float
    risk_momentum: float
    composite: float
    
    def to_dict(self):
        """Convert to dictionary"""
        return {
            'Valuation Lens': self.valuation,
            'Quality Lens': self.quality,
            'Growth Lens': self.growth,
            'Financial Health Lens': self.financial_health,
            'Risk & Momentum Lens': self.risk_momentum,
            'Composite Score': self.composite
        }


class FiveLensFramework:
    """
    Advanced Five-Lens Framework for stock analysis
    Each lens evaluated on 0-100 scale
    Composite score uses sector-adjusted weighting
    """

    def __init__(self, sector_weights: Optional[Dict] = None):
        """
        Initialize framework with optional custom weights
        
        Default weights: Equal 20% each
        Can be overridden by sector characteristics
        """
        self.default_weights = {
            'valuation': 0.20,
            'quality': 0.25,
            'growth': 0.20,
            'financial_health': 0.20,
            'risk_momentum': 0.15
        }
        
        self.sector_weights = sector_weights or {}
        
    def evaluate_stock(self, stock_data: Dict, financial_metrics: Dict, 
                      risk_metrics: Dict, peer_data: Optional[Dict] = None) -> LensScores:
        """
        Comprehensive stock evaluation using Five-Lens Framework
        
        Parameters:
        -----------
        stock_data : Dict
            Live stock data (price, P/E, P/B, market cap, dividend yield, etc.)
        financial_metrics : Dict
            Financial metrics (D/E, current ratio, ROE, NPM, etc.)
        risk_metrics : Dict
            Risk metrics (beta, volatility, var_95, sharpe_ratio, etc.)
        peer_data : Optional[Dict]
            Peer comparison data for sector benchmarking
            
        Returns:
        --------
        LensScores
            Scores for each lens and composite score
        """
        
        # Evaluate each lens
        valuation_score = self._evaluate_valuation_lens(stock_data, peer_data)
        quality_score = self._evaluate_quality_lens(financial_metrics, peer_data)
        growth_score = self._evaluate_growth_lens(financial_metrics, peer_data)
        health_score = self._evaluate_financial_health_lens(financial_metrics, peer_data)
        risk_score = self._evaluate_risk_momentum_lens(risk_metrics, stock_data)
        
        # Calculate composite score with weighting
        weights = self._get_weights(stock_data.get('sector', 'Default'))
        
        composite = (
            valuation_score * weights['valuation'] +
            quality_score * weights['quality'] +
            growth_score * weights['growth'] +
            health_score * weights['financial_health'] +
            risk_score * weights['risk_momentum']
        )
        
        return LensScores(
            valuation=valuation_score,
            quality=quality_score,
            growth=growth_score,
            financial_health=health_score,
            risk_momentum=risk_score,
            composite=composite
        )

    # ═════════════════════════════════════════════════════════════════════════
    # LENS 1: VALUATION LENS (20%)
    # ═════════════════════════════════════════════════════════════════════════
    
    def _evaluate_valuation_lens(self, stock_data: Dict, peer_data: Optional[Dict] = None) -> float:
        """
        Evaluate valuation metrics
        Lower is better (stocks with lower multiples = cheaper)
        
        Metrics:
        - P/E Ratio (40% weight)
        - P/B Ratio (30% weight)
        - Dividend Yield (20% weight)
        - Price-to-Sales (10% weight) if available
        """
        scores = []
        weights_local = []
        
        # P/E Ratio evaluation (40%)
        pe_ratio = stock_data.get('pe_ratio')
        if pe_ratio and not np.isnan(pe_ratio):
            pe_score = self._evaluate_pe_ratio(pe_ratio, stock_data.get('sector'))
            scores.append(pe_score)
            weights_local.append(0.40)
        
        # P/B Ratio evaluation (30%)
        pb_ratio = stock_data.get('pb_ratio')
        if pb_ratio and not np.isnan(pb_ratio):
            pb_score = self._evaluate_pb_ratio(pb_ratio)
            scores.append(pb_score)
            weights_local.append(0.30)
        
        # Dividend Yield evaluation (20%)
        div_yield = stock_data.get('dividend_yield')
        if div_yield and not np.isnan(div_yield):
            div_score = self._evaluate_dividend_yield(div_yield)
            scores.append(div_score)
            weights_local.append(0.20)
        
        # Price-to-Sales (10%)
        ps_ratio = stock_data.get('ps_ratio')
        if ps_ratio and not np.isnan(ps_ratio):
            ps_score = self._evaluate_ps_ratio(ps_ratio)
            scores.append(ps_score)
            weights_local.append(0.10)
        
        if not scores:
            return 50.0  # Default neutral score
        
        # Normalize weights if not all metrics available
        total_weight = sum(weights_local)
        weights_local = [w / total_weight for w in weights_local]
        
        return np.average(scores, weights=weights_local)

    @staticmethod
    def _evaluate_pe_ratio(pe_ratio: float, sector: Optional[str] = None) -> float:
        """
        Evaluate P/E ratio
        Optimal range: 15-25x (sector-dependent)
        Very cheap: <15x (75-90 points)
        Cheap: 15-20x (85-95 points)
        Fair: 20-25x (80-90 points)
        Expensive: 25-35x (50-80 points)
        Very expensive: >35x (20-50 points)
        """
        if pe_ratio <= 0:
            return 30.0  # Penalize negative or zero P/E
        
        if pe_ratio < 10:
            return 70.0  # Very cheap but possibly distressed
        elif pe_ratio < 15:
            return 85.0  # Excellent valuation
        elif pe_ratio < 20:
            return 90.0  # Very good valuation
        elif pe_ratio < 25:
            return 80.0  # Good valuation
        elif pe_ratio < 30:
            return 70.0  # Moderate valuation
        elif pe_ratio < 40:
            return 50.0  # Expensive
        else:
            return 30.0  # Very expensive

    @staticmethod
    def _evaluate_pb_ratio(pb_ratio: float) -> float:
        """
        Evaluate Price-to-Book ratio
        Optimal range: 1.5-3.0
        """
        if pb_ratio <= 0:
            return 30.0
        
        if pb_ratio < 1.0:
            return 75.0  # Trading below book value
        elif pb_ratio < 1.5:
            return 85.0  # Excellent value
        elif pb_ratio < 3.0:
            return 80.0  # Good value
        elif pb_ratio < 5.0:
            return 60.0  # Fair value
        else:
            return 40.0  # Overvalued

    @staticmethod
    def _evaluate_dividend_yield(div_yield: float) -> float:
        """
        Evaluate dividend yield
        Higher is better for income investors
        Typical range: 0-5%
        """
        div_pct = div_yield * 100  # Convert to percentage
        
        if div_pct < 0:
            return 40.0  # Negative yield (share buyback)
        elif div_pct < 1:
            return 60.0  # Low yield
        elif div_pct < 2:
            return 70.0  # Moderate yield
        elif div_pct < 3:
            return 85.0  # Good yield
        elif div_pct < 5:
            return 80.0  # Very good yield
        else:
            return 50.0  # Unsustainably high yield (risky)

    @staticmethod
    def _evaluate_ps_ratio(ps_ratio: float) -> float:
        """
        Evaluate Price-to-Sales ratio
        Lower is better
        Typical range: 0.5-3.0
        """
        if ps_ratio <= 0:
            return 30.0
        
        if ps_ratio < 1:
            return 90.0  # Excellent
        elif ps_ratio < 2:
            return 80.0  # Good
        elif ps_ratio < 3:
            return 70.0  # Fair
        elif ps_ratio < 5:
            return 50.0  # Expensive
        else:
            return 30.0  # Very expensive

    # ═════════════════════════════════════════════════════════════════════════
    # LENS 2: QUALITY LENS (25%)
    # ═════════════════════════════════════════════════════════════════════════
    
    def _evaluate_quality_lens(self, financial_metrics: Dict, peer_data: Optional[Dict] = None) -> float:
        """
        Evaluate quality of earnings and business
        
        Metrics:
        - ROE (Return on Equity) (35%)
        - Net Profit Margin (30%)
        - ROIC (if available) (20%)
        - Earnings Quality (15%)
        """
        scores = []
        weights_local = []
        
        # ROE evaluation (35%)
        roe = financial_metrics.get('roe')
        if roe and not np.isnan(roe):
            roe_score = self._evaluate_roe(roe)
            scores.append(roe_score)
            weights_local.append(0.35)
        
        # Net Profit Margin (30%)
        npm = financial_metrics.get('npm')
        if npm and not np.isnan(npm):
            npm_score = self._evaluate_npm(npm)
            scores.append(npm_score)
            weights_local.append(0.30)
        
        # ROIC (20%)
        roic = financial_metrics.get('roic')
        if roic and not np.isnan(roic):
            roic_score = self._evaluate_roic(roic)
            scores.append(roic_score)
            weights_local.append(0.20)
        
        # Earnings Quality (15%)
        roa = financial_metrics.get('roa')
        if roa and not np.isnan(roa):
            eq_score = self._evaluate_earnings_quality(roa)
            scores.append(eq_score)
            weights_local.append(0.15)
        
        if not scores:
            return 50.0
        
        total_weight = sum(weights_local)
        weights_local = [w / total_weight for w in weights_local]
        
        return np.average(scores, weights=weights_local)

    @staticmethod
    def _evaluate_roe(roe: float) -> float:
        """
        Evaluate Return on Equity
        Higher is better
        Excellent: >25%
        Good: 15-25%
        Fair: 10-15%
        Poor: <10%
        """
        roe_pct = roe * 100
        
        if roe_pct < 0:
            return 20.0
        elif roe_pct < 5:
            return 40.0
        elif roe_pct < 10:
            return 60.0
        elif roe_pct < 15:
            return 75.0
        elif roe_pct < 20:
            return 85.0
        elif roe_pct < 25:
            return 90.0
        else:
            return 95.0

    @staticmethod
    def _evaluate_npm(npm: float) -> float:
        """
        Evaluate Net Profit Margin
        Higher is better
        Varies by industry
        """
        npm_pct = npm * 100
        
        if npm_pct < 0:
            return 20.0
        elif npm_pct < 2:
            return 50.0
        elif npm_pct < 5:
            return 65.0
        elif npm_pct < 10:
            return 80.0
        elif npm_pct < 15:
            return 85.0
        elif npm_pct < 20:
            return 90.0
        else:
            return 95.0

    @staticmethod
    def _evaluate_roic(roic: float) -> float:
        """
        Evaluate Return on Invested Capital
        Higher is better
        Should exceed WACC (typically 8-12%)
        """
        roic_pct = roic * 100
        
        if roic_pct < 0:
            return 20.0
        elif roic_pct < 5:
            return 40.0
        elif roic_pct < 10:
            return 65.0
        elif roic_pct < 15:
            return 80.0
        elif roic_pct < 20:
            return 90.0
        else:
            return 95.0

    @staticmethod
    def _evaluate_earnings_quality(roa: float) -> float:
        """
        Evaluate Earnings Quality via ROA
        Higher is better
        """
        roa_pct = roa * 100
        
        if roa_pct < 0:
            return 20.0
        elif roa_pct < 2:
            return 50.0
        elif roa_pct < 5:
            return 70.0
        elif roa_pct < 10:
            return 85.0
        else:
            return 95.0

    # ═════════════════════════════════════════════════════════════════════════
    # LENS 3: GROWTH LENS (20%)
    # ═════════════════════════════════════════════════════════════════════════
    
    def _evaluate_growth_lens(self, financial_metrics: Dict, peer_data: Optional[Dict] = None) -> float:
        """
        Evaluate growth prospects
        
        Metrics:
        - Revenue Growth YoY (40%)
        - Earnings Growth YoY (40%)
        - Growth Quality (20%)
        """
        scores = []
        weights_local = []
        
        # Revenue Growth (40%)
        rev_growth = financial_metrics.get('revenue_growth_yoy')
        if rev_growth and not np.isnan(rev_growth):
            rev_score = self._evaluate_revenue_growth(rev_growth)
            scores.append(rev_score)
            weights_local.append(0.40)
        
        # Earnings Growth (40%)
        earnings_growth = financial_metrics.get('earnings_growth_yoy')
        if earnings_growth and not np.isnan(earnings_growth):
            earning_score = self._evaluate_earnings_growth(earnings_growth)
            scores.append(earning_score)
            weights_local.append(0.40)
        
        # PEG Ratio (20%)
        peg = financial_metrics.get('peg_ratio')
        if peg and not np.isnan(peg):
            peg_score = self._evaluate_peg_ratio(peg)
            scores.append(peg_score)
            weights_local.append(0.20)
        
        if not scores:
            return 50.0
        
        total_weight = sum(weights_local)
        weights_local = [w / total_weight for w in weights_local]
        
        return np.average(scores, weights=weights_local)

    @staticmethod
    def _evaluate_revenue_growth(growth: float) -> float:
        """
        Evaluate revenue growth rate
        Positive is better
        """
        growth_pct = growth * 100
        
        if growth_pct < 0:
            return 30.0
        elif growth_pct < 5:
            return 60.0
        elif growth_pct < 10:
            return 75.0
        elif growth_pct < 15:
            return 85.0
        elif growth_pct < 25:
            return 90.0
        else:
            return 85.0  # Very high growth may not be sustainable

    @staticmethod
    def _evaluate_earnings_growth(growth: float) -> float:
        """
        Evaluate earnings growth rate
        Positive is better
        """
        growth_pct = growth * 100
        
        if growth_pct < -10:
            return 20.0
        elif growth_pct < 0:
            return 40.0
        elif growth_pct < 5:
            return 60.0
        elif growth_pct < 15:
            return 80.0
        elif growth_pct < 25:
            return 90.0
        else:
            return 85.0

    @staticmethod
    def _evaluate_peg_ratio(peg: float) -> float:
        """
        Evaluate PEG Ratio (P/E to Growth)
        Optimal: < 1.0
        Fair: 1.0-1.5
        """
        if peg < 0:
            return 30.0
        elif peg < 0.8:
            return 95.0  # Excellent
        elif peg < 1.0:
            return 90.0  # Very good
        elif peg < 1.5:
            return 80.0  # Good
        elif peg < 2.0:
            return 60.0  # Fair
        else:
            return 40.0  # Expensive for growth

    # ═════════════════════════════════════════════════════════════════════════
    # LENS 4: FINANCIAL HEALTH LENS (20%)
    # ═════════════════════════════════════════════════════════════════════════
    
    def _evaluate_financial_health_lens(self, financial_metrics: Dict, peer_data: Optional[Dict] = None) -> float:
        """
        Evaluate financial stability and solvency
        
        Metrics:
        - Debt-to-Equity Ratio (35%)
        - Current Ratio / Liquidity (30%)
        - Interest Coverage (20%)
        - Free Cash Flow (15%)
        """
        scores = []
        weights_local = []
        
        # D/E Ratio (35%)
        de_ratio = financial_metrics.get('debt_to_equity')
        if de_ratio and not np.isnan(de_ratio):
            de_score = self._evaluate_de_ratio(de_ratio)
            scores.append(de_score)
            weights_local.append(0.35)
        
        # Current Ratio (30%)
        curr_ratio = financial_metrics.get('current_ratio')
        if curr_ratio and not np.isnan(curr_ratio):
            cr_score = self._evaluate_current_ratio(curr_ratio)
            scores.append(cr_score)
            weights_local.append(0.30)
        
        # Interest Coverage (20%)
        int_cov = financial_metrics.get('interest_coverage')
        if int_cov and not np.isnan(int_cov):
            ic_score = self._evaluate_interest_coverage(int_cov)
            scores.append(ic_score)
            weights_local.append(0.20)
        
        # Free Cash Flow (15%)
        fcf = financial_metrics.get('free_cash_flow')
        if fcf is not None and not np.isnan(fcf):
            fcf_score = 75.0 if fcf > 0 else 30.0
            scores.append(fcf_score)
            weights_local.append(0.15)
        
        if not scores:
            return 50.0
        
        total_weight = sum(weights_local)
        weights_local = [w / total_weight for w in weights_local]
        
        return np.average(scores, weights=weights_local)

    @staticmethod
    def _evaluate_de_ratio(de_ratio: float) -> float:
        """
        Evaluate Debt-to-Equity Ratio
        Lower is better, but some leverage is healthy
        Optimal range: 0.5-1.5
        """
        if de_ratio < 0:
            return 30.0
        elif de_ratio < 0.5:
            return 85.0  # Conservative
        elif de_ratio < 1.0:
            return 90.0  # Optimal
        elif de_ratio < 1.5:
            return 80.0  # Acceptable
        elif de_ratio < 2.0:
            return 60.0  # Moderately leveraged
        elif de_ratio < 3.0:
            return 40.0  # High leverage
        else:
            return 20.0  # Very high leverage

    @staticmethod
    def _evaluate_current_ratio(curr_ratio: float) -> float:
        """
        Evaluate Current Ratio
        Optimal range: 1.5-2.5
        """
        if curr_ratio < 0.5:
            return 30.0
        elif curr_ratio < 1.0:
            return 50.0
        elif curr_ratio < 1.5:
            return 75.0
        elif curr_ratio < 2.0:
            return 90.0
        elif curr_ratio < 3.0:
            return 85.0
        else:
            return 70.0  # Too high may indicate inefficiency

    @staticmethod
    def _evaluate_interest_coverage(int_cov: float) -> float:
        """
        Evaluate Interest Coverage Ratio
        Higher is better
        Minimum safe: 2.5x
        """
        if int_cov < 0:
            return 20.0
        elif int_cov < 1.5:
            return 30.0
        elif int_cov < 2.5:
            return 60.0
        elif int_cov < 5.0:
            return 80.0
        elif int_cov < 10.0:
            return 90.0
        else:
            return 95.0

    # ═════════════════════════════════════════════════════════════════════════
    # LENS 5: RISK & MOMENTUM LENS (15%)
    # ═════════════════════════════════════════════════════════════════════════
    
    def _evaluate_risk_momentum_lens(self, risk_metrics: Dict, stock_data: Dict) -> float:
        """
        Evaluate risk profile and momentum
        
        Metrics:
        - Beta (35%)
        - Volatility (30%)
        - Sharpe Ratio (20%)
        - Price Momentum (15%)
        """
        scores = []
        weights_local = []
        
        # Beta (35%)
        beta = risk_metrics.get('beta')
        if beta and not np.isnan(beta):
            beta_score = self._evaluate_beta(beta)
            scores.append(beta_score)
            weights_local.append(0.35)
        
        # Volatility (30%)
        volatility = risk_metrics.get('volatility_252d')
        if volatility and not np.isnan(volatility):
            vol_score = self._evaluate_volatility(volatility)
            scores.append(vol_score)
            weights_local.append(0.30)
        
        # Sharpe Ratio (20%)
        sharpe = risk_metrics.get('sharpe_ratio')
        if sharpe and not np.isnan(sharpe):
            sharpe_score = self._evaluate_sharpe_ratio(sharpe)
            scores.append(sharpe_score)
            weights_local.append(0.20)
        
        # Price Momentum (15%)
        momentum = stock_data.get('price_momentum_52w')
        if momentum and not np.isnan(momentum):
            mom_score = self._evaluate_momentum(momentum)
            scores.append(mom_score)
            weights_local.append(0.15)
        
        if not scores:
            return 50.0
        
        total_weight = sum(weights_local)
        weights_local = [w / total_weight for w in weights_local]
        
        return np.average(scores, weights=weights_local)

    @staticmethod
    def _evaluate_beta(beta: float) -> float:
        """
        Evaluate Beta (systematic risk)
        Beta = 1.0 means matches market
        Beta < 1.0 is more stable
        Beta > 1.0 is more volatile
        Optimal for conservative: 0.7-1.0
        """
        if beta < 0:
            return 30.0
        elif beta < 0.7:
            return 85.0  # Low volatility
        elif beta < 1.0:
            return 90.0  # Optimal
        elif beta < 1.3:
            return 75.0  # Moderate volatility
        elif beta < 1.5:
            return 60.0  # Higher volatility
        else:
            return 40.0  # Very volatile

    @staticmethod
    def _evaluate_volatility(volatility: float) -> float:
        """
        Evaluate annualized volatility
        Lower is better
        Optimal: <20%
        """
        vol_pct = volatility * 100
        
        if vol_pct < 15:
            return 90.0
        elif vol_pct < 20:
            return 80.0
        elif vol_pct < 30:
            return 70.0
        elif vol_pct < 40:
            return 50.0
        else:
            return 30.0

    @staticmethod
    def _evaluate_sharpe_ratio(sharpe: float) -> float:
        """
        Evaluate Sharpe Ratio (risk-adjusted return)
        Higher is better
        Excellent: >1.0
        Good: 0.5-1.0
        """
        if sharpe < 0:
            return 30.0
        elif sharpe < 0.25:
            return 50.0
        elif sharpe < 0.5:
            return 70.0
        elif sharpe < 1.0:
            return 85.0
        elif sharpe < 1.5:
            return 95.0
        else:
            return 95.0

    @staticmethod
    def _evaluate_momentum(momentum: float) -> float:
        """
        Evaluate 52-week price momentum
        Positive is better
        Range: -1.0 to +1.0 (as return percentage)
        """
        momentum_pct = momentum * 100
        
        if momentum_pct < -20:
            return 40.0  # Strong downtrend
        elif momentum_pct < -10:
            return 55.0  # Downtrend
        elif momentum_pct < 0:
            return 65.0  # Slightly down
        elif momentum_pct < 10:
            return 70.0  # Slightly up
        elif momentum_pct < 25:
            return 80.0  # Positive momentum
        elif momentum_pct < 50:
            return 85.0  # Strong momentum
        else:
            return 75.0  # Very strong (potential pullback)

    # ═════════════════════════════════════════════════════════════════════════
    # UTILITY METHODS
    # ═════════════════════════════════════════════════════════════════════════
    
    def _get_weights(self, sector: str) -> Dict[str, float]:
        """
        Get sector-specific weights
        Can be customized by sector
        """
        sector_specific = self.sector_weights.get(sector, {})
        
        # Start with defaults
        weights = self.default_weights.copy()
        
        # Override with sector-specific weights
        weights.update(sector_specific)
        
        # Ensure weights sum to 1.0
        total = sum(weights.values())
        return {k: v/total for k, v in weights.items()}
    
    @staticmethod
    def get_signal(score: float) -> Tuple[str, str]:
        """
        Convert composite score to investment signal
        Returns (signal, color)
        """
        if score >= 85:
            return ("🚀 Strong Buy", "green")
        elif score >= 75:
            return ("✅ Buy", "blue")
        elif score >= 65:
            return ("🟡 Hold / Accumulate", "orange")
        elif score >= 50:
            return ("⚠️  Watch", "gray")
        else:
            return ("🔴 Avoid", "red")
    
    def generate_recommendation(self, lens_scores: LensScores, stock_data: Dict) -> str:
        """
        Generate detailed investment recommendation
        """
        composite = lens_scores.composite
        signal, _ = self.get_signal(composite)
        
        strengths = []
        weaknesses = []
        
        # Identify strengths and weaknesses
        if lens_scores.valuation > 75:
            strengths.append("Excellent valuation metrics")
        if lens_scores.quality > 80:
            strengths.append("High-quality business")
        if lens_scores.growth > 75:
            strengths.append("Strong growth prospects")
        if lens_scores.financial_health > 80:
            strengths.append("Solid financial position")
        if lens_scores.risk_momentum > 75:
            strengths.append("Favorable risk-return profile")
        
        if lens_scores.valuation < 50:
            weaknesses.append("Valuation concerns")
        if lens_scores.quality < 60:
            weaknesses.append("Quality issues")
        if lens_scores.growth < 50:
            weaknesses.append("Limited growth prospects")
        if lens_scores.financial_health < 50:
            weaknesses.append("Financial health concerns")
        if lens_scores.risk_momentum < 50:
            weaknesses.append("High risk profile")
        
        recommendation = f"\n**Investment Signal: {signal}**\n\n"
        
        if strengths:
            recommendation += f"**Strengths:**\n"
            for s in strengths:
                recommendation += f"  • {s}\n"
        
        if weaknesses:
            recommendation += f"\n**Weaknesses:**\n"
            for w in weaknesses:
                recommendation += f"  • {w}\n"
        
        return recommendation
