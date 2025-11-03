# FA25 · CMPE-255 · Assignment 4 — CRISP-DM, KDD, and SEMMA (Consolidated)

End-to-end, principled data mining projects implemented three ways — **CRISP-DM**, **KDD**, and **SEMMA** — each with theory, phase-by-phase steps, code, and embedded outputs (figures/metrics).

> **Submission note:** This README links to the three Medium write-ups and summarizes how to reproduce the work locally or in Colab. Notebooks and artifacts live in the subfolders.

---

## 🔗 Medium Articles (Live)

- **CRISP-DM Case Study — Titanic Survival**  
  https://medium.com/@yashaswini.dinesh/crisp-dm-case-study-titanic-survival-8b72c8348c31

- **KDD Case Study — Customer Segmentation with RFM**  
  https://medium.com/@yashaswini.dinesh/kdd-case-study-customer-segmentation-with-rfm-58c0129e568c

- **SEMMA Case Study — Credit Card Fraud Detection**  
  https://medium.com/@yashaswini.dinesh/semma-case-study-credit-card-fraud-detection-1701e1167ddd

---

## 📦 Contents (root)

- `CRISP-DM.ipynb` — Cross‑Industry Standard Process for Data Mining (6 phases)
- `SEMMA.ipynb` — Sample, Explore, Modify, Model, Assess (5 steps)
- `KDD.ipynb` — Knowledge Discovery in Databases (5 steps)
- `crisp-dm_video_demo.mp4` (short walkthrough)
- `semma_video_demo.mp4` (short walkthrough)
- `KDD_video_demo.mp4` (short walkthrough)

> Colab tip: **Edit → Notebook settings →** uncheck *“Omit code cell output when saving”* so outputs are preserved.

---

## 📁 Repository Structure

```
assignment-4/
├─ crisp_dm/                # CRISP-DM project (Titanic)
│  ├─ notebook.ipynb
│  ├─ model/                # saved models/pipelines
│  ├─ app/                  # optional FastAPI service
│  └─ README.md
├─ kdd/                     # KDD project (RFM segmentation)
│  ├─ notebook.ipynb
│  └─ README.md
├─ semma/                   # SEMMA project (fraud detection)
│  ├─ notebook.ipynb
│  └─ README.md
└─ docs/
   └─ images/               # diagrams & result figures used in README/Medium
      ├─ crisp_dm_diagram.png
      ├─ kdd_diagram.png
      └─ semma_diagram.png
```

> Place exported plots (ROC/PR curves, confusion matrix, feature importance, elbow/silhouette, etc.) under `docs/images/` and reference them in the READMEs/Medium posts.

---

## 🚀 How to Run (Colab or Local)

**Colab (recommended):**
1. Open a notebook → **Open in Colab** (or upload the file).  
2. (Optional) **GPU** for models that benefit: Runtime → Change runtime type → GPU.  
3. **Run all**. Each notebook installs its own dependencies if needed.

**Local:**
```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
pip install pandas numpy scikit-learn matplotlib gradio
jupyter lab  # or jupyter notebook
```

> Data sources: (examples) Kaggle Titanic, UCI Online Retail, Kaggle Credit Card Fraud. Download and place under each subproject’s `data/` folder; update notebook paths if needed.

---

## 🗂 Methodology Summaries

### CRISP-DM (Titanic)
**Phases:** Business Understanding → Data Understanding → Data Preparation → Modeling → Evaluation → Deployment

**Highlights**
- Reproducible preprocessing (`ColumnTransformer` for impute/encode/scale)
- Baselines (LogReg) vs tree-based models; CV with ROC‑AUC
- Test ROC‑AUC, confusion matrix, fairness checks
- Optional FastAPI + Docker for serving

**Figures (examples)**
![CRISP-DM Diagram](docs/images/crisp_dm_diagram.png)

---

### KDD (Customer Segmentation with RFM)
**Phases:** Selection → Preprocessing → Transformation → Data Mining → Interpretation/Evaluation

**Highlights**
- RFM feature engineering per customer
- K‑Means/GMM with elbow & silhouette
- Segment profiling and actionable narratives

**Figures (examples)**
![KDD Diagram](docs/images/kdd_diagram.png)

---

### SEMMA (Credit Card Fraud)
**Phases:** Sample → Explore → Modify → Model → Assess

**Highlights**
- Class imbalance handling (class weights/SMOTE)
- PR‑AUC and cost-sensitive evaluation
- Feature importance & threshold optimization

**Figures (examples)**
![SEMMA Diagram](docs/images/semma_diagram.png)

---

## 🧠 Why Three Methodologies?

- **CRISP‑DM** is **business‑driven** and deployment‑oriented (cyclic 6 phases).  
- **SEMMA** emphasizes **modeling speed** and systematic assessment (linear 5 steps).  
- **KDD** is **data‑centric**, highlighting discovery and transformation (linear 5 steps).

Use whichever best fits your constraints; all three produce reproducible pipelines, fair model comparisons, and clear evaluations.

---

## 🧭 Quick Links

- 🔬 **Notebooks**: `crisp_dm/notebook.ipynb`, `kdd/notebook.ipynb`, `semma/notebook.ipynb`  
- 📰 **Articles**: see **Medium Articles** above  
- 🎥 **Walkthrough videos (optional)**: add YouTube links here

---

## 🧑‍⚖️ Critic Persona Prompt (Use with GPT‑5/Claude)

Paste this at the top of each section for rigorous reviews:

```
You are a world-renowned authority and keynote speaker on data mining methodologies (CRISP-DM, KDD, SEMMA),
and you have authored award-winning books. Review the section with extreme rigor.
Return: (1) rubric-based scores (0–5) per subtask; (2) gaps/risks (incl. leakage);
(3) concrete improvements and stronger baselines; (4) evidence requested (numbers, plots, ablations);
(5) a brief revised draft if needed.
```

---

## ✅ Submission Checklist

- [x] Three separate subdirectories clearly labeled: `crisp_dm/`, `kdd/`, `semma/`
- [x] Notebooks execute end‑to‑end with outputs kept
- [x] Each notebook shows a final metric and brief comparison/leaderboard
- [x] Seeds fixed where applicable for reproducibility
- [x] README links (Medium) and any video demos are accessible
- [x] All artifacts in GitHub (notebooks, diagrams, model files as appropriate)

---

## 📄 License

This work is for academic use as part of **FA25 CMPE‑255** coursework. See `LICENSE` if included.
