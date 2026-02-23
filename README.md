# Smart Portfolio Optimizer

> **Quantitative Portfolio Optimization Platform for EM & Global Assets**

Advanced allocation engine combining multiple optimization strategies, macro-aware asset selection, and walk-forward backtesting. Built for econometricians and quant investors analyzing EM, Brazil (B3), and global markets.

## ✨ Key Features

### 1. **Multi-Strategy Allocation Engines**
- **Markowitz (Mean-Variance)**: Classical efficient frontier with constraints
- **Risk Parity**: Equal risk contribution across assets
- **Risk Budgeting**: Target-volatility portfolios with custom risk allocation
- **Smart-Beta / Factor Allocation**: Value, momentum, quality, low-volatility sleeves
- **Regime-Switching**: Macro-conditioned portfolio rotation
- **Robust Optimization**: Shrinkage covariance, max-drawdown variants

### 2. **Macro & Economics Integration**
- Plug in macro variables (inflation, term spread, FX, commodities) to estimate conditional expected returns
- Simple stress-testing framework (rates, FX, commodity shocks)
- Country/sector constraints for mandates and tilts
- EM-aware universe with LATAM focus

### 3. **Multi-Region Data Adapters**
- **B3 Equities**: Brazilian stocks from Yahoo Finance
- **Global ETFs**: Cross-asset exposure (stocks, bonds, commodities)
- **Benchmarks**: IBOV, IBrX, S&P 500, MSCI EM, custom indices
- YAML/JSON universe definitions for easy configuration

### 4. **Walk-Forward Backtesting**
- Rebalancing frequency control
- Transaction costs & slippage modeling
- Performance metrics: Sharpe, Sortino, Calmar, max drawdown, turnover
- Rolling factor exposures & beta analysis
- Cumulative returns vs. benchmark plots

### 5. **Production-Ready API**
```python
from smart_portfolio import PortfolioOptimizer

opt = PortfolioOptimizer(
    model='markowitz',              # or 'risk_parity', 'smart_beta'
    universe='br_global_etf',       # YAML config
    constraints={'max_pos': 0.15},
    data_source='yfinance'
)

weights = opt.optimize(expected_returns, cov_matrix)
results = opt.backtest(rebalance_freq='monthly', transaction_cost=0.001)
```

## 📁 Project Structure

```
Smart-Portfolio-Optimizer/
├── smart_portfolio/
│   ├── __init__.py
│   ├── base.py                   # Base PortfolioOptimizer class
│   ├── optimizers/
│   │   ├── __init__.py
│   │   ├── markowitz.py         # Mean-variance optimizer
│   │   ├── risk_parity.py       # Risk-parity allocation
│   │   ├── smart_beta.py        # Factor-based allocation
│   │   └── robust.py            # Robust optimization methods
│   ├── macro/
│   │   ├── __init__.py
│   │   ├── regime_models.py     # Macro regime detection
│   │   └── returns_forecast.py  # Conditional returns estimation
│   ├── data/
│   │   ├── __init__.py
│   │   ├── adapters.py          # Data source adapters (yfinance, B3)
│   │   ├── universes/           # YAML/JSON universe configs
│   │   │   ├── br_global_etf.yaml
│   │   │   ├── global_60_40.yaml
│   │   │   └── latam_tilt.yaml
│   │   └── preprocessing.py     # Data cleaning & alignment
│   ├── backtest/
│   │   ├── __init__.py
│   │   ├── engine.py            # Walk-forward backtest engine
│   │   ├── metrics.py           # Performance metrics
│   │   └── plots.py             # Visualization tools
│   └── utils/
│       ├── config.py            # Config management
│       └── helpers.py           # Utility functions
├── notebooks/
│   ├── 01_data_and_universe.ipynb
│   ├── 02_core_strategies.ipynb
│   ├── 03_macro_regime_allocation.ipynb
│   └── 04_backtest_and_evaluation.ipynb
├── tests/
│   ├── test_optimizers.py
│   ├── test_backtest.py
│   └── test_data.py
├── requirements.txt
├── setup.py
└── README.md
```

## 🚀 Quick Start

### Installation

```bash
git clone https://github.com/yourusername/Smart-Portfolio-Optimizer
cd Smart-Portfolio-Optimizer
pip install -e .
```

### Example: Markowitz Optimization

```python
import numpy as np
from smart_portfolio.optimizers import MarkowitzOptimizer

# Load your data
returns = pd.read_csv('returns.csv', index_col=0)
expected_returns = returns.mean() * 252
cov_matrix = returns.cov() * 252

# Optimize
opt = MarkowitzOptimizer(
    risk_free_rate=0.04,
    constraints={'min_weight': 0, 'max_weight': 0.2, 'sum_to_one': True}
)
weights = opt.optimize(expected_returns, cov_matrix, objective='max_sharpe')

print(f"Optimal Weights:\n{weights}")
print(f"Sharpe Ratio: {opt.sharpe_ratio(weights, cov_matrix):.2f}")
```

### Example: Brazil + Global ETF Portfolio

```python
from smart_portfolio import PortfolioOptimizer
from smart_portfolio.data import UniverseLoader

# Load pre-configured universe
loader = UniverseLoader('br_global_etf.yaml')
data = loader.fetch_data(start_date='2020-01-01')

# Build portfolio
port = PortfolioOptimizer(
    universe=loader,
    model='risk_parity',
    data_source='yfinance'
)

weights = port.optimize(expected_returns=data['returns'].mean() * 252)

# Backtest
results = port.backtest(
    weights=weights,
    rebalance_freq='quarterly',
    transaction_cost=0.001,
    slippage=0.0005
)

print(results.metrics())
results.plot_cumulative_returns()
```

## 📊 Design Philosophy

**Why This Repository?**

This project bridges quant finance and macroeconomics by combining:
- **Econometric foundations**: Macro variables, regime-switching, factor models
- **Portfolio science**: Modern & robust optimization, risk-aware allocation
- **EM/Brazil expertise**: Native B3 support, LATAM-specific universes
- **Production quality**: Clean API, extensive backtesting, modularity

Perfect for:
- Economics students exploring quant strategies
- Asset managers building EM portfolios
- Researchers testing multi-strategy frameworks
- Interns in quant/macro finance roles

## 📚 Example Notebooks

See the `notebooks/` directory:

1. **01_data_and_universe.ipynb** - Loading B3 + global data, universe configuration
2. **02_core_strategies.ipynb** - Running Markowitz, risk-parity, smart-beta allocators
3. **03_macro_regime_allocation.ipynb** - Building macro-conditioned portfolios
4. **04_backtest_and_evaluation.ipynb** - Full workflow with visualization

## 🔧 Requirements

```
python>=3.9
pandas>=1.3
numpy>=1.20
scipy>=1.7
scikit-learn>=1.0
scikit-optimize>=0.9
skfolio>=0.2
yfinance>=0.1.70
matplotlib>=3.4
seaborn>=0.11
pyyaml>=5.4
```

## 📈 Roadmap

- [x] Core optimization engines (Markowitz, risk-parity)
- [x] B3 + global data adapters
- [ ] Macro regime-switching models
- [ ] ML-enhanced return forecasting
- [ ] Advanced risk models (factor-based covariance)
- [ ] Interactive dashboard (Streamlit)
- [ ] GitHub Actions CI/CD
- [ ] PyPI package release

## 🤝 Contributing

Contributions welcome! Please fork, create a feature branch, and submit a PR.

## 📝 License

MIT License - see LICENSE file

## 📞 Contact

For questions or collaboration:
- GitHub: [@lorenlorenloren](https://github.com/lorenlorenloren)
- Email: your.email@example.com

---

**Built for econometricians and quant investors worldwide.** 🌍
