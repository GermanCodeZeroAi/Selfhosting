from fastapi import FastAPI
from pydantic import BaseModel
from joblib import dump, load
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
MODEL_PATH = Path("/models/intent.joblib")
app = FastAPI(title="GCZA Intent Service")

class TrainItem(BaseModel):
    text: str
    label: str

class ClassifyItem(BaseModel):
    text: str

DATA = []

def build_model():
    return Pipeline([
        ("tfidf", TfidfVectorizer(min_df=2, ngram_range=(1,2))),
        ("clf", LogisticRegression(max_iter=1000))
    ])

@app.post("/train")
def train(item: TrainItem):
    DATA.append((item.text, item.label))
    if len(DATA) < 6:
        return {"status":"queued","need":6-len(DATA)}
    X, y = zip(*DATA)
    model = build_model().fit(list(X), list(y))
    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    dump(model, MODEL_PATH)
    return {"status":"trained","samples":len(DATA)}

@app.post("/classify")
def classify(item: ClassifyItem):
    if MODEL_PATH.exists():
        model = load(MODEL_PATH)
    else:
        model = build_model().fit(
            ["invoice","offer","meeting","spam","support","other"],
            ["finance","sales","schedule","spam","support","other"]
        )
    proba = model.predict_proba([item.text])[0]
    label = model.classes_[proba.argmax()]
    score = float(proba.max())
    return {"intent":label,"score":score}