import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from datetime import datetime

class AutoML:

    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100)

    def train(self, df):

        X = df[[
            "bos", "sweep", "vwap_dist",
            "atr", "volume", "fvg"
        ]]

        y = df["target"]  # 1 = win, 0 = loss

        self.model.fit(X, y)

        joblib.dump(self.model, "model.pkl")

    def load(self):
        self.model = joblib.load("model.pkl")

    def predict(self, features):
        return self.model.predict_proba([features])[0][1]

  import schedule
import time

def retrain():
    df = load_trade_history()
    model.train(df)

schedule.every().saturday.at("18:00").do(retrain)

while True:
    schedule.run_pending()
    time.sleep(60)
