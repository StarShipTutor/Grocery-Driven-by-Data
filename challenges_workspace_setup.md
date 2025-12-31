# Grocery – Driven by Data: Workspace Setup

**Purpose:** This document defines the folder structure and setup instructions for the Kaggle challenge execution workspace. Use this to bootstrap a new AI session.

---

## Project Overview

This workspace is for **executing** the Grocery – Driven by Data challenge series (C01–C03). Each challenge produces two deliverables:

1. **Jupyter Notebook** — The analysis and code
2. **Slide Deck (NSDD Format)** — The 15-slide narrative presentation

---

## Folder Structure

```
grocery-driven-by-data/
├── DOE/                          # AI context bootstrapping
│   ├── directives/               # How to do things
│   └── orchestration/            # Session context
│
├── data/
│   ├── raw/                      # Original CSVs from Kaggle (NEVER modify)
│   ├── processed/                # Cleaned/transformed outputs
│   └── external/                 # Reference data (holidays, weather, etc.)
│
├── challenge_01/                 # Spaghetti → Schema
│   ├── notebooks/
│   │   ├── 01_eda.ipynb
│   │   ├── 02_schema_design.ipynb
│   │   ├── 03_etl.ipynb
│   │   └── 04_baseline_model.ipynb
│   ├── sql/
│   │   ├── ddl.sql               # CREATE TABLE statements
│   │   └── indexes.sql
│   ├── deck/
│   │   ├── challenge_01_deck.pptx
│   │   └── deck_notes.md         # NSDD structure notes
│   └── docs/
│       ├── architecture.md       # ERD, design decisions
│       └── data_dictionary.md
│
├── challenge_02/                 # Errors → Integrity
│   ├── notebooks/
│   │   ├── 01_data_audit.ipynb
│   │   ├── 02_imputation.ipynb
│   │   └── 03_validation.ipynb
│   ├── deck/
│   └── docs/
│
├── challenge_03/                 # Data → Signal
│   ├── notebooks/
│   │   ├── 01_trend_analysis.ipynb
│   │   ├── 02_forecasting.ipynb
│   │   └── 03_model_eval.ipynb
│   ├── deck/
│   └── docs/
│
├── shared/
│   ├── utils/                    # Reusable Python modules
│   │   ├── db.py                 # Postgres connection helpers
│   │   ├── etl.py                # Common transforms
│   │   └── viz.py                # Standard chart styles
│   └── config/
│       └── settings.yaml         # DB credentials, paths
│
├── outputs/
│   ├── figures/                  # Exported charts for decks
│   └── reports/                  # Executive summaries (PDF)
│
├── .env                          # Secrets (DB password, etc.) — NOT IN GIT
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Design Principles

1. **Each challenge is self-contained** — All notebooks and outputs live in the challenge folder
2. **Data flows forward** — `data/raw/` → C01 → `data/processed/` → C02 → ... → C03 → `outputs/`
3. **SQL stays with C01** — The schema is built once, used by all subsequent challenges
4. **Two deliverables per challenge** — `notebooks/` and `deck/`
5. **Shared utilities** — Common code in `shared/utils/` to avoid duplication
6. **DOE at root** — AI can be bootstrapped with directives from any session

---

## NSDD Deck Structure (15 Slides)

| Slide | Purpose |
|-------|---------|
| 1 | Title |
| 2 | Intro / Context / Problem Statement |
| 3-5 | **Block 1** (Beginning) |
| 6-8 | **Block 2** (Middle) |
| 9-11 | **Block 3** (End) |
| 12 | Conclusions |
| 13 | Recommendations |
| 14 | Actions (CTA) |
| 15 | References |

Every deck follows this structure. See `deck_notes.md` for challenge-specific mapping.

---

## Dependency Flow

```
Kaggle Data
    ↓
data/raw/
    ↓
challenge_01/ → Creates schema, loads to Postgres → data/processed/
    ↓
challenge_02/ → Audits, fixes, validates → data/processed/ (cleaned)
    ↓
challenge_03/ → Forecasting, trends → outputs/figures/, outputs/reports/
```

---

## Acceptance Criteria

### Challenge 01: Spaghetti → Schema
- [ ] ERD documented in `docs/architecture.md`
- [ ] DDL creates schema cleanly
- [ ] ETL loads ≥ 95% of rows
- [ ] Referential integrity holds
- [ ] Baseline model reports MAE/MAPE
- [ ] Deck follows NSDD format

### Challenge 02: Errors → Integrity
- [ ] Data audit notebook profiles all issues
- [ ] Imputation methods documented with rationale
- [ ] Post-clean validation passes
- [ ] No suspicious metric inflation on re-trained baseline
- [ ] Deck follows NSDD format

### Challenge 03: Data → Signal
- [ ] Trend analysis with seasonality decomposition
- [ ] Forecasting model with holdout validation
- [ ] Comparison to naive baseline
- [ ] Feature importance documented
- [ ] Deck follows NSDD format

---

## Setup Instructions

1. **Create the folder structure** (AI can do this)
2. **Download data from Kaggle** → place in `data/raw/`
3. **Set up Postgres** (local or cloud) → add credentials to `.env`
4. **Install dependencies:** `pip install -r requirements.txt`
5. **Start with C01 notebook 01_eda.ipynb**

---

## AI Collaboration Notes

- Use **Coder mode** for notebooks and SQL
- Use **Agent mode** for file operations and ETL execution
- Each challenge has detailed requirements in the Research Projects workspace:
  - `research/data_science/grocery_driven_by_data/challenge_01.md`
  - `research/data_science/grocery_driven_by_data/challenge_02.md`
  - `research/data_science/grocery_driven_by_data/challenge_03.md`

Cross-reference those files for task lists, deliverables, and acceptance criteria.

---

## Related Resources

- **Research Workspace:** Contains background, sources, and collateral
- **Substack:** [CarrierWave](https://starshiptutor.substack.com) for public communications
- **GitHub Wiki:** Challenge specifications and work plans
