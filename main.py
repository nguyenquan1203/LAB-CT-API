from transformers import pipeline
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException

app = FastAPI()

MODEL_NAME = (
    "distilbert/distilbert-base-uncased-finetuned-sst-2-english"
)

try:
    classifier = pipeline(
        task="text-classification",
        model=MODEL_NAME,
        device=-1,
    )
except Exception as error:
    print("Cannot load model:", error)
    classifier = None


class PredictInput(BaseModel):
    text: str


@app.get("/")
def home():
    return {
        "message": "English Text Sentiment Analysis API",
        "model": MODEL_NAME,
    }


@app.get("/health")
def health():
    if classifier is None:
        raise HTTPException(status_code=503, detail="Model is not ready")

    return {"status": "ok", "model_loaded": True}


@app.post("/predict")
def predict(data: PredictInput):
    text = data.text.strip()

    if not text:
        raise HTTPException(status_code=400, detail="Text cannot be empty")

    if len(text) > 2000:
        raise HTTPException(status_code=400, detail="Text is too long")

    if classifier is None:
        raise HTTPException(status_code=503, detail="Model is not ready")

    try:
        result = classifier(text, truncation=True, max_length=512)[0]

        return {
            "text": text,
            "label": result["label"],
            "score": float(result["score"]),
        }

    except Exception as error:
        print("Prediction error:", error)
        raise HTTPException(
            status_code=500,
            detail="Cannot analyze text",
        ) from None
