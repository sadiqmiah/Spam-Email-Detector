import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib
from preprocess import clean_text

print("Loading dataset...")
df = pd.read_csv("spam.csv", encoding="latin-1")

# Check columns
print("Columns in CSV:", df.columns)

X = df["v2"].apply(clean_text)
y = df["v1"]

# Vectorize
vectorizer = CountVectorizer()
X_vec = vectorizer.fit_transform(X)

# Train model
model = MultinomialNB()
model.fit(X_vec, y)

# Save model
joblib.dump(model, "model/svm_model.pkl")
joblib.dump(vectorizer, "model/vectorizer.pkl")
print("Models saved successfully.")