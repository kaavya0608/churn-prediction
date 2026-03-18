import joblib
import pandas as pd
import numpy as np

model = joblib.load("models/churn_model.pkl")
scaler = joblib.load("models/scaler.pkl")

def get_risk_level(probability: float) -> str:
    if probability >= 0.7:
        return "high"
    elif probability >= 0.4:
        return "medium"
    else:
        return "low"

def predict_churn(customer_data: dict) -> float:
    df = pd.DataFrame([customer_data])

    cat_cols = ['multiple_lines', 'internet_service', 'online_security',
                'online_backup', 'device_protection', 'tech_support',
                'streaming_tv', 'streaming_movies', 'contract', 'payment_method']

    df = pd.get_dummies(df, columns=cat_cols, drop_first=True)

    df = df.rename(columns={
        'tenure': 'tenure',
        'monthly_charges': 'MonthlyCharges',
        'total_charges': 'TotalCharges'
    })

    numeric_cols = ['tenure', 'MonthlyCharges', 'TotalCharges']
    df[numeric_cols] = scaler.transform(df[numeric_cols])

    expected_cols = model.feature_names_in_
    for col in expected_cols:
        if col not in df.columns:
            df[col] = 0
    df = df[expected_cols]

    probability = model.predict_proba(df)[0][1]
    return round(float(probability), 4)