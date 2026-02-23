"""Base Portfolio Optimizer class."""

import pandas as pd
import numpy as np
from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Tuple


class PortfolioOptimizer(ABC):
    """Base class for portfolio optimization strategies.
    
    This abstract base class defines the interface for all portfolio
    optimization engines, including Markowitz, risk-parity, and smart-beta
    strategies.
    """
    
    def __init__(
        self,
        model: str = 'markowitz',
        universe: Optional[str] = None,
        constraints: Optional[Dict] = None,
        data_source: str = 'yfinance'
    ):
        """Initialize the portfolio optimizer.
        
        Args:
            model: Optimization model ('markowitz', 'risk_parity', 'smart_beta')
            universe: Universe configuration name or path
            constraints: Dictionary of constraints (e.g., max_weight, min_weight)
            data_source: Data source ('yfinance', 'local', etc.)
        """
        self.model = model
        self.universe = universe
        self.constraints = constraints or {}
        self.data_source = data_source
        self.weights = None
        self.metrics = {}
    
    @abstractmethod
    def optimize(
        self,
        expected_returns: pd.Series,
        cov_matrix: pd.DataFrame,
        **kwargs
    ) -> np.ndarray:
        """Optimize portfolio weights.
        
        Args:
            expected_returns: Expected returns for each asset
            cov_matrix: Covariance matrix of asset returns
            **kwargs: Model-specific parameters
            
        Returns:
            Optimal portfolio weights
        """
        pass
    
    @abstractmethod
    def backtest(
        self,
        returns: pd.DataFrame,
        rebalance_freq: str = 'monthly',
        **kwargs
    ) -> Dict:
        """Run walk-forward backtest.
        
        Args:
            returns: Historical returns (N x M: time x assets)
            rebalance_freq: Rebalancing frequency
            **kwargs: Backtest parameters
            
        Returns:
            Dictionary with backtest results and metrics
        """
        pass
    
    def _apply_constraints(self, weights: np.ndarray) -> np.ndarray:
        """Apply portfolio constraints to weights.
        
        Args:
            weights: Initial weights
            
        Returns:
            Constrained weights
        """
        if 'min_weight' in self.constraints:
            weights = np.maximum(weights, self.constraints['min_weight'])
        
        if 'max_weight' in self.constraints:
            weights = np.minimum(weights, self.constraints['max_weight'])
        
        if 'sum_to_one' in self.constraints and self.constraints['sum_to_one']:
            weights /= weights.sum()
        
        return weights
    
    def get_metrics(self) -> Dict:
        """Return optimization metrics."""
        return self.metrics
