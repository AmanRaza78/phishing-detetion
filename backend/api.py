from fastapi import FastAPI
from pydantic import BaseModel
import tldextract
import re
from backend.model import predict_phishing

app = FastAPI()

class URLRequest(BaseModel):
    url: str

# Feature extraction function
def extract_features(url):
    extracted = tldextract.extract(url)
    domain = extracted.domain

    return [
        len(url),                # URL length
        url.count('.'),          # Number of dots
        url.count('/'),          # Number of slashes
        sum(c.isdigit() for c in url),  # Number of digits
        1 if url.startswith("https") else 0  # HTTPS presence
    ]

@app.post("/predict")
def predict(request: URLRequest):
    features = extract_features(request.url)
    prediction = predict_phishing(features)
    return {"phishing": bool(prediction)}

# Run server with:
# uvicorn backend.api:app --reload --port 8000
