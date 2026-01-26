from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
from preprocess import clean_text

app = FastAPI(title="Spam Email Detector API")

# ✅ CORS FIX
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # OK for demo/portfolio
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add a root route so visiting "/" doesn’t 404
@app.get("/")
def root():
    return {"message": "Spam Email Detector API is running!"}

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
