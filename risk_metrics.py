"""
═══════════════════════════════════════════════════════════════════════════════
THE MOUNTAIN PATH - WORLD OF FINANCE
Advanced Risk Metrics Module
Value-at-Risk (VaR), Conditional Value-at-Risk (CVaR), and Risk Analysis
═══════════════════════════════════════════════════════════════════════════════

Prof. V. Ravichandran - Financial Risk Management
"""

import numpy as np
import pandas as pd
from scipy import stats
from typing import Dict, Tuple, Optional
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')


class RiskMetricsCalculator:
    """
    Advanced risk metrics calculator
    Includes VaR, CVaR, Sharpe Ratio, Beta, Volatility, Drawdown Analysis
    """
    
    # Risk-free rate (approximate current)
    RISK_FREE_RATE = 0.06  # 6% annual
    
    # Confidence levels for VaR
    CONFIDENCE_95 = 0.95
    CONFIDENCE_99 = 0.99

    @staticmethod
    def calculate_all_risk_metrics(price_history: pd.Series, 
                                   market_data: Optional[pd.Series] = None,
                                   current_price: Optional[float] = None) -> Dict:
        """
        Calculate comprehensive risk metrics
        
        Parameters:
        -----------
        price_history : pd.Series
            Historical price data
        market_data : Optional[pd.Series]
            Market index data (for beta calculation)
        current_price : Optional[float]
            Current stock price
            
        Returns:
        --------
        Dict : All risk metrics
        """
        
        if len(price_history) < 2:
            return RiskMetricsCalculator._get_default_metrics()
        
        metrics = {}
        
        # Basic metrics
        metrics['volatility_252d'] = RiskMetricsCalculator.calculate_volatility(
            price_history, periods=252
        )
        metrics['volatility_60d'] = RiskMetricsCalculator.calculate_volatility(
            price_history, periods=60
        )
        
        # VaR and CVaR
        returns = RiskMetricsCalculator.calculate_returns(price_history)
        metrics['var_95'] = RiskMetricsCalculator.calculate_var(returns, confidence=0.95)
        metrics['var_99'] = RiskMetricsCalculator.calculate_var(returns, confidence=0.99)
        metrics['cvar_95'] = RiskMetricsCalculator.calculate_cvar(returns, confidence=0.95)
        
        # Sharpe Ratio
        metrics['sharpe_ratio'] = RiskMetricsCalculator.calculate_sharpe_ratio(
            returns, risk_free_rate=RiskMetricsCalculator.RISK_FREE_RATE
        )
        
        # Drawdown metrics
        max_dd, avg_dd = RiskMetricsCalculator.calculate_drawdown(price_history)
        metrics['max_drawdown'] = max_dd
        metrics['avg_drawdown'] = avg_dd
        
        # Beta (if market data available)
        if market_data is not None and len(market_data) >= len(price_history) * 0.5:
            metrics['beta'] = RiskMetricsCalculator.calculate_beta(
                price_history, market_data
            )
        else:
            metrics['beta'] = 1.0  # Default
        
        # Sortino Ratio
        metrics['sortino_ratio'] = RiskMetricsCalculator.calculate_sortino_ratio(
            returns, risk_free_rate=RiskMetricsCalculator.RISK_FREE_RATE
        )
        
        # Skewness and Kurtosis
        metrics['skewness'] = float(stats.skew(returns))
        metrics['kurtosis'] = float(stats.kurtosis(returns))
        
        # Calmar Ratio
        metrics['calmar_ratio'] = RiskMetricsCalculator.calculate_calmar_ratio(
            returns, max_dd
        )
        
        # Information Ratio (if benchmark available)
        metrics['information_ratio'] = 0.0  # Placeholder
        
        return metrics

    @staticmethod
    def calculate_volatility(price_history: pd.Series, periods: int = 252) -> float:
        """
        Calculate annualized volatility (standard deviation of returns)
        
        Parameters:
        -----------
        price_history : pd.Series
            Historical prices
        periods : int
            Annual periods (252 for daily, 52 for weekly, 12 for monthly)
            
        Returns:
        --------
        float : Annualized volatility
        """
        if len(price_history) < 2:
            return 0.0
        
        returns = price_history.pct_change().dropna()
        
        if len(returns) == 0:
            return 0.0
        
        # Daily volatility * sqrt(252)
        daily_vol = returns.std()
        annualized_vol = daily_vol * np.sqrt(periods)
        
        return float(annualized_vol)

    @staticmethod
    def calculate_returns(price_history: pd.Series, method: str = 'log') -> np.ndarray:
        """
        Calculate returns from price history
        
        Parameters:
        -----------
        price_history : pd.Series
            Historical prices
        method : str
            'simple' or 'log' returns
            
        Returns:
        --------
        np.ndarray : Returns
        """
        if len(price_history) < 2:
            return np.array([])
        
        if method == 'log':
            returns = np.log(price_history / price_history.shift(1)).dropna()
        else:
            returns = price_history.pct_change().dropna()
        
        return returns.values

    @staticmethod
    def calculate_var(returns: np.ndarray, confidence: float = 0.95, 
                      method: str = 'historical') -> float:
        """
        Calculate Value-at-Risk (VaR)
        
        Parameters:
        -----------
        returns : np.ndarray
            Historical returns
        confidence : float
            Confidence level (0.95 = 95%)
        method : str
            'historical', 'parametric', or 'cornish-fisher'
            
        Returns:
        --------
        float : VaR as decimal (e.g., -0.05 for 5% loss)
        """
        if len(returns) < 10:
            return -0.05  # Default
        
        if method == 'historical':
            var = np.percentile(returns, (1 - confidence) * 100)
        
        elif method == 'parametric':
            # Assume normal distribution
            mean = np.mean(returns)
            std = np.std(returns)
            z_score = stats.norm.ppf(1 - confidence)
            var = mean + z_score * std
        
        elif method == 'cornish-fisher':
            # Modified VaR accounting for skewness and kurtosis
            mean = np.mean(returns)
            std = np.std(returns)
            skew = stats.skew(returns)
            kurt = stats.kurtosis(returns)
            
            z = stats.norm.ppf(1 - confidence)
            z_cf = (z + (z**2 - 1) * skew / 6 + 
                   (z**3 - 3*z) * kurt / 24 - 
                   (2*z**3 - 5*z) * skew**2 / 36)
            
            var = mean + z_cf * std
        
        else:
            var = np.percentile(returns, (1 - confidence) * 100)
        
        return float(var)

    @staticmethod
    def calculate_cvar(returns: np.ndarray, confidence: float = 0.95) -> float:
        """
        Calculate Conditional Value-at-Risk (CVaR) / Expected Shortfall
        Average loss given that loss exceeds VaR
        
        Parameters:
        -----------
        returns : np.ndarray
            Historical returns
        confidence : float
            Confidence level
            
        Returns:
        --------
        float : CVaR as decimal
        """
        if len(returns) < 10:
            return -0.08  # Default
        
        var = RiskMetricsCalculator.calculate_var(returns, confidence)
        cvar = returns[returns <= var].mean()
        
        if np.isnan(cvar):
            cvar = var
        
        return float(cvar)

    @staticmethod
    def calculate_sharpe_ratio(returns: np.ndarray, risk_free_rate: float = 0.06,
                               periods: int = 252) -> float:
        """
        Calculate Sharpe Ratio (risk-adjusted return)
        Higher is better
        
        Parameters:
        -----------
        returns : np.ndarray
            Daily returns
        risk_free_rate : float
            Annual risk-free rate
        periods : int
            Annual periods (252 for daily)
            
        Returns:
        --------
        float : Sharpe Ratio
        """
        if len(returns) < 2:
            return 0.0
        
        annual_return = np.mean(returns) * periods
        annual_vol = np.std(returns) * np.sqrt(periods)
        
        if annual_vol == 0:
            return 0.0
        
        sharpe = (annual_return - risk_free_rate) / annual_vol
        
        return float(sharpe)

    @staticmethod
    def calculate_sortino_ratio(returns: np.ndarray, risk_free_rate: float = 0.06,
                                periods: int = 252) -> float:
        """
        Calculate Sortino Ratio (downside risk-adjusted return)
        Like Sharpe but only penalizes downside volatility
        
        Parameters:
        -----------
        returns : np.ndarray
            Daily returns
        risk_free_rate : float
            Annual risk-free rate
        periods : int
            Annual periods
            
        Returns:
        --------
        float : Sortino Ratio
        """
        if len(returns) < 2:
            return 0.0
        
        annual_return = np.mean(returns) * periods
        
        # Downside volatility (only negative returns)
        downside_returns = returns[returns < 0]
        if len(downside_returns) == 0:
            downside_vol = 0.0
        else:
            downside_vol = np.std(downside_returns) * np.sqrt(periods)
        
        if downside_vol == 0:
            return 0.0
        
        sortino = (annual_return - risk_free_rate) / downside_vol
        
        return float(sortino)

    @staticmethod
    def calculate_drawdown(price_history: pd.Series) -> Tuple[float, float]:
        """
        Calculate maximum and average drawdown
        
        Parameters:
        -----------
        price_history : pd.Series
            Historical prices
            
        Returns:
        --------
        Tuple[float, float] : (max_drawdown, avg_drawdown)
        """
        if len(price_history) < 2:
            return 0.0, 0.0
        
        # Calculate cumulative maximum
        cum_max = price_history.expanding().max()
        
        # Calculate drawdown as % from peak
        drawdown = (price_history - cum_max) / cum_max
        
        max_dd = float(drawdown.min())
        avg_dd = float(drawdown[drawdown < 0].mean()) if len(drawdown[drawdown < 0]) > 0 else 0.0
        
        return max_dd, avg_dd

    @staticmethod
    def calculate_beta(stock_prices: pd.Series, market_prices: pd.Series) -> float:
        """
        Calculate Beta (systematic risk)
        Measures stock volatility relative to market
        
        Parameters:
        -----------
        stock_prices : pd.Series
            Stock price history
        market_prices : pd.Series
            Market index price history
            
        Returns:
        --------
        float : Beta
        """
        if len(stock_prices) < 20 or len(market_prices) < 20:
            return 1.0
        
        # Align data
        min_len = min(len(stock_prices), len(market_prices))
        stock_prices = stock_prices.iloc[-min_len:]
        market_prices = market_prices.iloc[-min_len:]
        
        # Calculate returns
        stock_returns = stock_prices.pct_change().dropna()
        market_returns = market_prices.pct_change().dropna()
        
        # Align returns
        min_ret_len = min(len(stock_returns), len(market_returns))
        stock_returns = stock_returns.iloc[-min_ret_len:].values
        market_returns = market_returns.iloc[-min_ret_len:].values
        
        if len(stock_returns) < 2 or len(market_returns) < 2:
            return 1.0
        
        # Calculate beta
        covariance = np.cov(stock_returns, market_returns)[0, 1]
        market_variance = np.var(market_returns)
        
        if market_variance == 0:
            return 1.0
        
        beta = covariance / market_variance
        
        return float(beta)

    @staticmethod
    def calculate_calmar_ratio(returns: np.ndarray, max_drawdown: float,
                               periods: int = 252) -> float:
        """
        Calculate Calmar Ratio
        Annual return / Maximum drawdown (absolute value)
        
        Parameters:
        -----------
        returns : np.ndarray
            Daily returns
        max_drawdown : float
            Maximum drawdown (as decimal)
        periods : int
            Annual periods
            
        Returns:
        --------
        float : Calmar Ratio
        """
        if len(returns) < 2 or max_drawdown == 0:
            return 0.0
        
        annual_return = np.mean(returns) * periods
        
        # Use absolute value of max_drawdown
        calmar = annual_return / abs(max_drawdown)
        
        return float(calmar)

    @staticmethod
    def calculate_rolling_volatility(price_history: pd.Series, window: int = 60) -> pd.Series:
        """
        Calculate rolling volatility
        
        Parameters:
        -----------
        price_history : pd.Series
            Historical prices
        window : int
            Rolling window size
            
        Returns:
        --------
        pd.Series : Rolling volatility
        """
        returns = price_history.pct_change()
        rolling_vol = returns.rolling(window=window).std() * np.sqrt(252)
        
        return rolling_vol

    @staticmethod
    def calculate_correlation_matrix(price_histories: Dict[str, pd.Series]) -> pd.DataFrame:
        """
        Calculate correlation matrix between multiple stocks
        
        Parameters:
        -----------
        price_histories : Dict[str, pd.Series]
            Dictionary of stock name -> price history
            
        Returns:
        --------
        pd.DataFrame : Correlation matrix
        """
        # Calculate returns for all stocks
        returns = {}
        for name, prices in price_histories.items():
            ret = prices.pct_change().dropna()
            returns[name] = ret
        
        # Create DataFrame
        returns_df = pd.DataFrame(returns)
        
        # Calculate correlation
        correlation = returns_df.corr()
        
        return correlation

    @staticmethod
    def _get_default_metrics() -> Dict:
        """Get default metrics when insufficient data"""
        return {
            'volatility_252d': 0.25,
            'volatility_60d': 0.25,
            'var_95': -0.05,
            'var_99': -0.08,
            'cvar_95': -0.08,
            'sharpe_ratio': 0.5,
            'max_drawdown': -0.20,
            'avg_drawdown': -0.10,
            'beta': 1.0,
            'sortino_ratio': 0.7,
            'skewness': 0.0,
            'kurtosis': 0.0,
            'calmar_ratio': 1.0,
            'information_ratio': 0.0
        }

    @staticmethod
    def risk_profile_summary(risk_metrics: Dict) -> str:
        """
        Generate risk profile summary
        
        Parameters:
        -----------
        risk_metrics : Dict
            Risk metrics
            
        Returns:
        --------
        str : Risk profile summary
        """
        vol = risk_metrics.get('volatility_252d', 0.25) * 100
        beta = risk_metrics.get('beta', 1.0)
        sharpe = risk_metrics.get('sharpe_ratio', 0.5)
        max_dd = risk_metrics.get('max_drawdown', -0.20) * 100
        var_95 = risk_metrics.get('var_95', -0.05) * 100
        
        # Determine risk profile
        if vol < 15:
            vol_profile = "Low Volatility"
        elif vol < 25:
            vol_profile = "Moderate Volatility"
        else:
            vol_profile = "High Volatility"
        
        if beta < 0.8:
            beta_profile = "Defensive"
        elif beta > 1.2:
            beta_profile = "Aggressive"
        else:
            beta_profile = "Market-Aligned"
        
        summary = f"""
**RISK PROFILE SUMMARY**

Volatility (252-day):  {vol:.2f}% → {vol_profile}
Beta:                  {beta:.2f}x → {beta_profile}
Sharpe Ratio:          {sharpe:.2f} → {'Excellent' if sharpe > 1 else 'Good' if sharpe > 0.5 else 'Fair'}
Max Drawdown:          {max_dd:.2f}%
Value-at-Risk (95%):   {var_95:.2f}% daily loss possible
"""
        return summary
