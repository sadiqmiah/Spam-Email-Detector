from fastapi import FastAPI
from pydantic import BaseModel
import joblib
from preprocess import clean_text

app = FastAPI(title="Spam Email Detector API")

# Load model and vectorizer
model = joblib.load("model/svm_model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

class Email(BaseModel):
    text: str

@app.post("/predict")
def predict(email: Email):
    cleaned = clean_text(email.text)
    vec = vectorizer.transform([cleaned])
    prediction = model.predict(vec)[0]
    return {"prediction": prediction}
