import pandas as pd
import numpy as np
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegression
import joblib

def prepare_labels(df, label_columns):
    mlb = MultiLabelBinarizer()
    y = mlb.fit_transform(df[label_columns].values)
    return y, mlb

def train_model(X, y):
    model = LogisticRegression(max_iter=1000)
    model.fit(X, y)
    return model

def evaluate_model(model, X, y, mlb):
    y_pred = model.predict(X)
    print(classification_report(y, y_pred, target_names=mlb.classes_))

def save_model(model, mlb, path='models/trained_model.joblib'):
    joblib.dump({'model': model, 'mlb': mlb}, path)
    print(f"Model saved to {path}")

def load_model(path='models/trained_model.joblib'):
    data = joblib.load(path)
    return data['model'], data['mlb']
