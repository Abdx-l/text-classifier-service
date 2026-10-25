import os,joblib
from functools import lru_cache
from fastapi import FastAPI,Response
from pydantic import BaseModel,Field
from prometheus_client import Counter,generate_latest,CONTENT_TYPE_LATEST
app=FastAPI();predictions=Counter("classifier_predictions_total","Classified documents")
@lru_cache
def artifact():return joblib.load(os.getenv("MODEL_PATH","model.joblib"))
class Input(BaseModel):text:str=Field(min_length=1,max_length=50000)
@app.post("/predict")
def predict(body:Input):
 a=artifact();probabilities=a["model"].predict_proba([body.text])[0];predictions.inc()
 return {"predictions":[{"label":a["labels"][int(a["model"].classes_[i])],"probability":float(probabilities[i])} for i in probabilities.argsort()[-3:][::-1]]}
@app.get("/health")
def health():return {"model_available":os.path.isfile(os.getenv("MODEL_PATH","model.joblib"))}
@app.get("/metrics")
def metrics():return Response(generate_latest(),media_type=CONTENT_TYPE_LATEST)
