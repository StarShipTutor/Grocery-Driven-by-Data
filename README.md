# Grocery – Driven by Data

**Kaggle Challenge Execution Workspace**

This workspace houses the work for a three-challenge series focused on grocery sales data analysis and forecasting.

## Challenges

| Challenge | Title | Focus |
|-----------|-------|-------|
| C01 | Spaghetti → Schema | Data modeling, ETL, baseline model |
| C02 | Errors → Integrity | Data quality, imputation, validation |
| C03 | Data → Signal | Trend analysis, forecasting |

## Quick Start

1. Place Kaggle data in `data/raw/`
2. Configure `.env` with database credentials
3. Install dependencies: `pip install -r requirements.txt`
4. Start with Challenge 01: `challenge_01/notebooks/01_eda.ipynb`

## Structure

- `DOE/` — AI context bootstrapping (directives, orchestration)
- `data/` — Raw, processed, and external data
- `challenge_0X/` — Challenge-specific notebooks, SQL, decks, and docs
- `shared/` — Reusable utilities and config
- `outputs/` — Generated figures and reports

## Deliverables (Per Challenge)

1. **Jupyter Notebooks** — Analysis and code
2. **Slide Deck (NSDD Format)** — 15-slide narrative presentation

---

See `challenges_workspace_setup.md` for detailed setup instructions.
