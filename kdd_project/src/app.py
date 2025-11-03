from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI(title="Demo Model API")

class InputRow(BaseModel):
    features: list

@app.on_event("startup")
def load_model():
    global model
    model = joblib.load("models/model.joblib")

@app.post("/predict")
def predict(row: InputRow):
    X = np.array(row.features).reshape(1, -1)
    y = model.predict(X).tolist()
    return {"prediction": y}
