FROM python:3.11-slim

RUN apt-get update && apt-get install -y git build-essential && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir     jupyterlab ipykernel pandas numpy scikit-learn matplotlib seaborn     xgboost lightgbm imbalanced-learn fastapi uvicorn[standard]     kaggle gradio

# Make sure a kernel exists
RUN python -m ipykernel install --name python3 --display-name "Python 3"
