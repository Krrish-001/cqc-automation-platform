from fastapi import FastAPI
from app.model import predict

app = FastAPI(title="CQC Automation Platform")

@app.get("/")
def home():
    return {"message": "CQC Automation Platform Running"}

@app.post("/predict")
def prediction(data: dict):
    result = predict(data["value"])
    return {"prediction": result}
