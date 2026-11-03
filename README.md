# Sentiment Analysis API

- **Student:** Nguyễn Anh Quân
- **Student ID:** 25127123

## Overview

This project provides a FastAPI service that analyzes English text. It returns a sentiment label (POSITIVE or NEGATIVE) and a confidence score in JSON format.

## Model Used

[DistilBERT base uncased finetuned SST-2](https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english)

## Setup

Create a virtual environment and install the dependencies:

```powershell
python -m venv venv
.\venv\Scripts\python.exe -m pip install -r requirements.txt
```

## Start the API

```powershell
uvicorn main:app --reload
```

Open the interactive API documentation at:
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

Available endpoints:

- `GET /` — View basic API information.
- `GET /health` — Check whether the model is ready.
- `POST /predict` — Submit text for sentiment analysis.

## Test the API

Keep the server running and execute this command in another terminal:

```powershell
.\venv\Scripts\Activate.ps1
python test.py
```

The script tests positive and negative sentences, along with invalid inputs.

Example request to `POST /predict`:

```json
{"text": "I love this movie. It was fantastic!"}
```

Example response:

```json
{
  "text": "I love this movie. It was fantastic!",
  "label": "POSITIVE",
  "score": 0.9998760223388672
}
```

## Demo Video

[VIDEO](https://youtu.be/V29WymzeFE4)