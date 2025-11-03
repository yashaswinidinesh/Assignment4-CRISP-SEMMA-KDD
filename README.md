# Assignment 4 — CRISP-DM, SEMMA, and KDD

**Due:** Your LMS deadline.  
**This repo contains three independent projects**, each using a different data mining methodology:

- `crisp_dm_project/` — CRISP-DM on *Walmart Sales Forecasting* (Kaggle).  
- `semma_project/` — SEMMA on *Student Performance* (Kaggle).  
- `kdd_project/` — KDD on *Credit Card Fraud Detection* (Kaggle).  

Each subproject contains:
- A Colab-ready notebook implementing all phases of the methodology.
- An `src/` folder with helper code and a minimal FastAPI demo for deployment.
- A `reports/` folder with exports and a Medium article draft.
- A `prompts/` folder with critique prompts (Claude / GPT-5 persona) to iterate on each phase.

> ⚠️ **Datasets are not committed** to keep the repo light. The notebooks include a Kaggle API cell to download data.

## Quick Start (Cursor / VS Code)
1. Clone the repo and open the folder in Cursor.  
2. (Optional) Use the included Dev Container for a consistent environment.
3. Open a project notebook from `*/notebooks/` and run cells top-to-bottom.

## Colab
Each notebook has a **"Open in Colab"** badge near the top. After you push this repo to GitHub, the badge will point to your copy automatically.

## Datasets (add your Kaggle token first)
- Walmart sales forecasting: https://www.kaggle.com/datasets/aslanahmedov/walmart-sales-forecast  
- Student performance: https://www.kaggle.com/datasets/bhuvaneshwarisa/student-performance-dataset  
- Credit card fraud: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

> Configure Kaggle in Colab/local: upload `kaggle.json` to `~/.kaggle/` and `chmod 600 ~/.kaggle/kaggle.json`.

## Suggested Tools
- IBM SPSS Modeler (CRISP-DM reports)
- SAS (SEMMA flow) or SAS OnDemand
- Open Interpreter & MetaGPT to orchestrate long runs

---

_Repo bootstrap generated on 2025-11-02._
