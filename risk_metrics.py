
import numpy as np
import pandas as pd
from typing import Tuple, Optional, Dict

class RiskMetricsCalculator:
    """Calculate comprehensive risk metrics for stocks"""
    
    @staticmethod
    def calculate_beta(stock_prices: pd.Series, market_prices: pd.Series) -> Optional[float]:
        """
        Calculate Beta (stock sensitivity to market movements)
        
        Beta = Covariance(Stock Returns, Market Returns) / Variance(Market Returns)
        
        Interpretation:
        - Beta = 1.0: Stock moves exactly with market
        - Beta > 1.0: Stock more volatile than market (aggressive)
        - Beta < 1.0: Stock less volatile than market (defensive)
        - Beta < 0.0: Stock moves opposite to market (rare)
        
        Args:
            stock_prices: Series of stock prices
            market_prices: Series of market index prices
        
        Returns:
            Beta value or None if insufficient data
        """
        try:
            # Validate inputs
            if market_prices is None or len(market_prices) < 2 or len(stock_prices) < 2:
                return None
            
            # Convert to pandas Series if needed
            if not isinstance(stock_prices, pd.Series):
                stock_prices = pd.Series(stock_prices)
            if not isinstance(market_prices, pd.Series):
                market_prices = pd.Series(market_prices)
            
            # Calculate daily returns (percentage change)
            stock_returns = stock_prices.pct_change().dropna()
            market_returns = market_prices.pct_change().dropna()
            
            # Ensure both series have same length
            min_length = min(len(stock_returns), len(market_returns))
            if min_length < 2:
                return None
            
            stock_returns = stock_returns[-min_length:]
            market_returns = market_returns[-min_length:]
            
            # Calculate covariance between stock and market
            covariance = np.cov(stock_returns, market_returns)[0][1]
            
            # Calculate variance of market
            market_variance = np.var(market_returns, ddof=1)
            
            # Avoid division by zero
            if market_variance <= 0:
                return None
            
            # Calculate beta
            beta = covariance / market_variance
            
            # Validate result
            if np.isnan(beta) or np.isinf(beta):
                return None
            
            return beta
        
        except Exception as e:
            print(f"Error calculating beta: {e}")
            return None
    
    @staticmethod
    def calculate_volatility(prices: pd.Series, periods: int = 252) -> float:
        """
        Calculate annualized volatility (standard deviation of returns)
        
        Args:
            prices: Series of prices
            periods: Trading periods per year (default 252 for daily data)
        
        Returns:
            Annualized volatility
        """
        try:
            if len(prices) < 2:
                return 0.0
            
            # Calculate daily returns
            returns = prices.pct_change().dropna()
            
            if len(returns) < 1:
                return 0.0
            
            # Calculate daily volatility
            daily_volatility = returns.std()
            
            # Annualize volatility
            annualized_volatility = daily_volatility * np.sqrt(periods)
            
            return annualized_volatility
        
        except Exception as e:
            print(f"Error calculating volatility: {e}")
            return 0.0
    
    @staticmethod
    def calculate_sharpe_ratio(prices: pd.Series, risk_free_rate: float = 0.05) -> float:
        """
        Calculate Sharpe Ratio (risk-adjusted returns)
        
        Sharpe Ratio = (Average Return - Risk-Free Rate) / Volatility
        
        Interpretation:
        - Sharpe > 1.0: Good risk-adjusted returns
        - Sharpe > 2.0: Very good risk-adjusted returns
        - Sharpe < 0.0: Returns worse than risk-free rate
        
        Args:
            prices: Series of prices
            risk_free_rate: Annual risk-free rate (default 5%)
        
        Returns:
            Sharpe ratio
        """
        try:
            if len(prices) < 2:
                return 0.0
            
            # Calculate daily returns
            returns = prices.pct_change().dropna()
            
            if len(returns) < 1:
                return 0.0
            
            # Annualize returns
            avg_daily_return = returns.mean()
            annualized_return = avg_daily_return * 252
            
            # Get volatility
            volatility = RiskMetricsCalculator.calculate_volatility(prices)
            
            # Calculate Sharpe ratio
            if volatility <= 0:
                return 0.0
            
            sharpe_ratio = (annualized_return - risk_free_rate) / volatility
            
            return sharpe_ratio
        
        except Exception as e:
            print(f"Error calculating Sharpe ratio: {e}")
            return 0.0
    
    @staticmethod
    def calculate_drawdown(prices: pd.Series) -> Tuple[float, int]:
        """
        Calculate Maximum Drawdown and its duration
        
        Maximum Drawdown = (Trough Value - Peak Value) / Peak Value
        
        Interpretation:
        - 0%: No decline from peak
        - -10%: 10% decline from peak
        - -50%: 50% decline from peak (severe)
        
        Args:
            prices: Series of prices
        
        Returns:
            Tuple of (max_drawdown, drawdown_duration_in_days)
        """
        try:
            if len(prices) < 2:
                return 0.0, 0
            
            # Calculate cumulative maximum (running peak)
            cummax = prices.cummax()
            
            # Calculate drawdown
            drawdown = (prices - cummax) / cummax
            
            # Maximum drawdown
            max_drawdown = drawdown.min()
            
            # Duration of drawdown (in trading days)
            drawdown_duration = 0
            if max_drawdown < 0:
                # Find when maximum drawdown occurred
                max_dd_idx = drawdown.idxmin()
                # Find the peak before this drawdown
                peak_before = cummax[:max_dd_idx].iloc[-1] if len(cummax[:max_dd_idx]) > 0 else prices.iloc[0]
                # Find when price recovered to peak
                prices_after_dd = prices[max_dd_idx:]
                recovery_points = prices_after_dd[prices_after_dd >= peak_before]
                
                if len(recovery_points) > 0:
                    drawdown_duration = len(prices[max_dd_idx:recovery_points.index[0]])
                else:
                    drawdown_duration = len(prices) - prices.index.get_loc(max_dd_idx)
            
            return max_drawdown, drawdown_duration
        
        except Exception as e:
            print(f"Error calculating drawdown: {e}")
            return 0.0, 0
    
    @staticmethod
    def calculate_var(prices: pd.Series, confidence: float = 0.95) -> float:
        """
        Calculate Value at Risk (VaR)
        
        VaR = Quantile of returns at given confidence level
        
        Interpretation:
        - VaR(95%) = -0.05 means 5% chance of losing 5% or more in one day
        
        Args:
            prices: Series of prices
            confidence: Confidence level (0.95 = 95% confidence)
        
        Returns:
            VaR value
        """
        try:
            if len(prices) < 2:
                return 0.0
            
            # Calculate daily returns
            returns = prices.pct_change().dropna()
            
            if len(returns) < 1:
                return 0.0
            
            # Calculate VaR at given confidence level
            alpha = 1 - confidence
            var = returns.quantile(alpha)
            
            return var
        
        except Exception as e:
            print(f"Error calculating VaR: {e}")
            return 0.0
    
    @staticmethod
    def calculate_correlation_matrix(prices_dict: Dict[str, pd.Series]) -> pd.DataFrame:
        """
        Calculate correlation matrix for multiple stocks
        
        Args:
            prices_dict: Dictionary of {stock_name: price_series}
        
        Returns:
            Correlation matrix DataFrame
        """
        try:
            # Prepare data
            returns_dict = {}
            for stock_name, prices in prices_dict.items():
                returns = prices.pct_change().dropna()
                if len(returns) > 0:
                    returns_dict[stock_name] = returns
            
            if len(returns_dict) < 2:
                return pd.DataFrame()
            
            # Create DataFrame
            returns_df = pd.DataFrame(returns_dict)
            
            # Calculate correlation
            correlation = returns_df.corr()
            
            return correlation
        
        except Exception as e:
            print(f"Error calculating correlation matrix: {e}")
            return pd.DataFrame()
    
    @staticmethod
    def calculate_all_risk_metrics(stock_prices: pd.Series, 
                                   market_prices: Optional[pd.Series] = None,
                                   current_price: Optional[float] = None) -> Dict:
        """
        Calculate all risk metrics for a stock
        
        Args:
            stock_prices: Series of stock prices
            market_prices: Series of market index prices (optional)
            current_price: Current stock price (optional)
        
        Returns:
            Dictionary with all risk metrics
        """
        try:
            metrics = {}
            
            # BETA CALCULATION (Only if market data available)
            if market_prices is not None and len(market_prices) > 1:
                beta = RiskMetricsCalculator.calculate_beta(stock_prices, market_prices)
                metrics['beta'] = beta if beta is not None else 1.0
            else:
                # No market data available
                metrics['beta'] = None
            
            # VOLATILITY (252-day annualized)
            volatility = RiskMetricsCalculator.calculate_volatility(stock_prices)
            metrics['volatility_252d'] = volatility
            
            # SHARPE RATIO
            sharpe_ratio = RiskMetricsCalculator.calculate_sharpe_ratio(stock_prices)
            metrics['sharpe_ratio'] = sharpe_ratio
            
            # MAXIMUM DRAWDOWN and Duration
            max_dd, dd_duration = RiskMetricsCalculator.calculate_drawdown(stock_prices)
            metrics['max_drawdown'] = max_dd
            metrics['drawdown_duration'] = dd_duration
            
            # VALUE AT RISK (95% confidence)
            var_95 = RiskMetricsCalculator.calculate_var(stock_prices, confidence=0.95)
            metrics['var_95'] = var_95
            
            # TOTAL RETURN
            try:
                total_return = (stock_prices.iloc[-1] - stock_prices.iloc[0]) / stock_prices.iloc[0]
                metrics['total_return'] = total_return
            except:
                metrics['total_return'] = 0.0
            
            return metrics
        
        except Exception as e:
            print(f"Error calculating all risk metrics: {e}")
            return {
                'beta': None,
                'volatility_252d': 0.0,
                'sharpe_ratio': 0.0,
                'max_drawdown': 0.0,
                'drawdown_duration': 0,
                'var_95': 0.0,
                'total_return': 0.0,
            }
    
    @staticmethod
    def risk_profile_summary(risk_metrics: Dict) -> str:
        """
        Generate a summary of the risk profile
        
        Args:
            risk_metrics: Dictionary of risk metrics
        
        Returns:
            HTML/markdown formatted risk summary
        """
        try:
            beta = risk_metrics.get('beta')
            volatility = risk_metrics.get('volatility_252d', 0.0)
            sharpe = risk_metrics.get('sharpe_ratio', 0.0)
            max_dd = risk_metrics.get('max_drawdown', 0.0)
            var_95 = risk_metrics.get('var_95', 0.0)
            total_return = risk_metrics.get('total_return', 0.0)
            
            # Determine risk profile
            if beta is None:
                beta_text = "Market data unavailable"
            elif beta > 1.2:
                beta_text = f"{beta:.2f}x - High sensitivity to market movements"
            elif beta > 0.8:
                beta_text = f"{beta:.2f}x - Moderate sensitivity to market movements"
            else:
                beta_text = f"{beta:.2f}x - Low sensitivity to market movements (Defensive)"
            
            if volatility > 0.30:
                vol_text = f"{volatility*100:.1f}% - High volatility (Risky)"
            elif volatility > 0.20:
                vol_text = f"{volatility*100:.1f}% - Moderate volatility"
            else:
                vol_text = f"{volatility*100:.1f}% - Low volatility (Stable)"
            
            if sharpe > 1.0:
                sharpe_text = f"{sharpe:.2f} - Good risk-adjusted returns"
            elif sharpe > 0.0:
                sharpe_text = f"{sharpe:.2f} - Moderate risk-adjusted returns"
            else:
                sharpe_text = f"{sharpe:.2f} - Poor risk-adjusted returns"
            
            summary = f"""
**Risk Profile Analysis:**

- **Beta**: {beta_text}
- **Volatility (252d)**: {vol_text}
- **Sharpe Ratio**: {sharpe_text}
- **Maximum Drawdown**: {max_dd*100:.1f}%
- **Value at Risk (95%)**: {var_95*100:.1f}%
- **Total Return**: {total_return*100:.1f}%

**Risk Assessment:**
"""
            
            if beta is None or beta == 1.0:
                summary += "⚠️ Market correlation data unavailable. Beta may not reflect true market sensitivity.\n"
            
            if volatility > 0.25:
                summary += "⚠️ High volatility - stock price fluctuates significantly.\n"
            elif volatility < 0.15:
                summary += "✅ Low volatility - stable stock price.\n"
            
            if max_dd < -0.30:
                summary += "⚠️ Severe drawdowns observed - significant downside risk.\n"
            elif max_dd < -0.15:
                summary += "⚠️ Moderate drawdowns observed.\n"
            else:
                summary += "✅ Drawdowns relatively contained.\n"
            
            if sharpe > 1.0:
                summary += "✅ Good risk-adjusted returns for the risk taken.\n"
            elif sharpe < 0:
                summary += "⚠️ Returns not compensating for risk taken.\n"
            
            return summary.strip()
        
        except Exception as e:
            print(f"Error generating risk summary: {e}")
            return "Unable to generate risk profile summary."
