import pickle
import json
import numpy as np
import pandas as pd
import shap

# ---------------- LOAD ARTIFACTS ---------------- #

with open("churn_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("feature_names.pkl", "rb") as f:
    feature_names = pickle.load(f)

with open("config.json", "r") as f:
    config = json.load(f)

threshold = config["threshold"]
low_risk_max = config["low_risk_max"]
medium_risk_max = config["medium_risk_max"]

# Extract trained parts
preprocessor = model.named_steps["preprocess"]
clf = model.named_steps["model"]

# SHAP explainer (safe background)
explainer = shap.LinearExplainer(clf, np.zeros((1, len(feature_names))))

# ---------------- RISK BUCKET FUNCTION ---------------- #

def get_risk_bucket(prob):
    if prob < low_risk_max:
        return "Low Risk"
    elif prob < medium_risk_max:
        return "Medium Risk"
    else:
        return "High Risk"


# ---------------- MAIN PREDICT FUNCTION ---------------- #

def predict_customer(input_dict):
    """
    input_dict: dictionary from form
    returns: prediction, probability, risk segment, shap values
    """

    # ✅ Step 1 — convert to dataframe
    input_df = pd.DataFrame([input_dict])

    # ✅ Step 2 — enforce training column order
    input_df = input_df[model.feature_names_in_]

    # ✅ Step 3 — numeric casting (ONLY true numeric cols)
    numeric_like = ["tenure", "MonthlyCharges", "TotalCharges"]

    for col in numeric_like:
        if col in input_df.columns:
            input_df[col] = pd.to_numeric(input_df[col], errors="coerce")

    # ✅ Step 4 — FORCE categorical to string (CRITICAL FIX)
    for col in input_df.columns:
        if col not in numeric_like:
            input_df[col] = input_df[col].astype(str)
    # ✅ Step 4 — predict
    prob = model.predict_proba(input_df)[0, 1]
    risk = get_risk_bucket(prob)

    # ✅ Step 5 — SHAP explanation
    processed = preprocessor.transform(input_df)
    shap_vals = explainer.shap_values(processed)[0]

    shap_df = pd.DataFrame({
        "feature": feature_names,
        "shap_value": shap_vals
    }).sort_values(by="shap_value", key=abs, ascending=False).head(5)

    return {
        "churn_probability": float(prob),
        "risk_segment": risk,
        "top_factors": shap_df.to_dict(orient="records")
    }