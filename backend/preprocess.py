import re
import nltk
from nltk.corpus import stopwords

try:
    stopwords.words("english")
except LookupError:
    nltk.download("stopwords")

STOPWORDS = set(stopwords.words("english"))

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    tokens = text.split()
    tokens = [t for t in tokens if t not in STOPWORDS]
    return " ".join(tokens)