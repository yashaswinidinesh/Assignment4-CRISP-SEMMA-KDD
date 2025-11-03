# Assignment 4 — CRISP‑DM, SEMMA, and KDD

This repository contains **three end‑to‑end notebooks** demonstrating classic data‑mining methodologies. Each notebook is self‑contained and runs on Google Colab or locally with Python 3.9+.

> Tip: In Colab, keep outputs: **Edit → Notebook settings →** uncheck *“Omit code cell output when saving”*.

---

## 📦 Contents (root)

- `CRISP-DM.ipynb` — Cross‑Industry Standard Process for Data Mining (6 phases)
- `SEMMA.ipynb` — Sample, Explore, Modify, Model, Assess (5 steps)
- `KDD.ipynb` — Knowledge Discovery in Databases (5 steps)
- `crisp-dm_video_demo.mp4` (short walkthrough)
- `semma_video_demo.mp4` (short walkthrough)
- `KDD_video_demo.mp4` (short walkthrough)

---

## 🚀 How to Run (Colab or Local)

**Colab (recommended):**
1) Open a notebook → **Open in Colab** (or upload the file).  
2) (Optional) **GPU** for models that benefit: Runtime → Change runtime type → GPU.  
3) **Run all**. Each notebook installs its own dependencies if needed.

**Local:**
```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
pip install pandas numpy scikit-learn matplotlib gradio
jupyter lab  # or jupyter notebook
```

---

## 📚 What Each Notebook Covers

### 1) CRISP‑DM (`CRISP-DM.ipynb`)
**Goal:** show the full **6‑phase** cycle: *Business Understanding → Data Understanding → Data Preparation → Modeling → Evaluation → Deployment* (demo).  
**Highlights:**
- Reproducible preprocessing pipeline (impute/encode/scale)
- Multiple baseline + ensemble models under time limits
- **ROC‑AUC** (classification) or **RMSE/R²** (regression), depending on dataset
- Optional probability calibration & thresholding
- Simple **Gradio UI** demo for “deployment”

### 2) SEMMA (`SEMMA.ipynb`)
**Goal:** follow **Sample → Explore → Modify → Model → Assess**.  
**Highlights:**
- Stratified sampling for speed and balance
- Lightweight EDA (target balance, missingness, quick visuals)
- Feature engineering (ratios, bins, date parts as applicable)
- Model comparison with cross‑validation
- Final test‑set report + permutation feature importance

### 3) KDD (`KDD.ipynb`)
**Goal:** demonstrate **Selection → Preprocessing → Transformation → Data Mining → Interpretation/Evaluation**.  
**Highlights:**
- Clean schema/types, remove identifiers, split train/test
- Encoders/standardization as needed; optional PCA/feature select
- Compact model portfolio (strong baselines + 1 ensemble)
- Clear evaluation on the held‑out test set
- Saved pipeline for reuse

---

## 🧠 Why Three Methodologies?

- **CRISP‑DM** is **business‑driven** and deployment‑oriented (cyclic 6 phases).  
- **SEMMA** emphasizes **modeling speed** and systematic assessment (linear 5 steps).  
- **KDD** is **data‑centric**, highlighting discovery and transformation (linear 5 steps).

Use whichever best fits your project constraints; all three produce a reproducible pipeline, fair model comparison, and a clear final evaluation.

---

## 🗂️ Suggested Repo Structure

```
.
├─ CRISP-DM.ipynb
├─ SEMMA.ipynb
├─ KDD.ipynb
├─ crisp-dm_video_demo.mp4
├─ semma_video_demo.mp4
├─ KDD_video_demo.mp4
└─ README.md
```

---

## ✅ Submission Checklist

- [ ] Notebooks execute end‑to‑end with outputs kept.  
- [ ] Each notebook shows a **final metric** and brief comparison/leaderboard.  
- [ ] Any random seeds/session IDs are fixed for reproducibility.  
- [ ] README links and video demos are accessible.

---

## 📄 Notes

- Datasets and any external assets remain under their respective licenses.  
- The notebooks can be extended with additional metrics, plots, or error analysis as needed.