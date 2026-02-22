from flask import Flask, render_template, request
from utils.predict import predict_customer

app = Flask(__name__)


# ---------------- HOME PAGE ---------------- #

@app.route("/")
def home():
    return render_template("index.html")


# ---------------- SAFE FORM HELPER ---------------- #

def get_form_value(name, cast_type=str, default=None):
    # default cast type is str, can be overwritten
    # default value is not entered is None
    value = request.form.get(name, default)
    try:
        return cast_type(value)
    except (ValueError, TypeError):
        return default


# ---------------- PREDICTION ROUTE ---------------- #

@app.route("/predict", methods=["POST"])
def predict():

    # Build input dictionary EXACTLY matching training columns
    input_dict = {
        "gender": get_form_value("gender"),
        "SeniorCitizen": get_form_value("SeniorCitizen", int, 0),
        "Partner": get_form_value("Partner"),
        "Dependents": get_form_value("Dependents"),
        "tenure": get_form_value("tenure", float, 0),
        "PhoneService": get_form_value("PhoneService"),
        "MultipleLines": get_form_value("MultipleLines"),
        "InternetService": get_form_value("InternetService"),
        "OnlineSecurity": get_form_value("OnlineSecurity"),
        "OnlineBackup": get_form_value("OnlineBackup"),
        "DeviceProtection": get_form_value("DeviceProtection"),
        "TechSupport": get_form_value("TechSupport"),
        "StreamingTV": get_form_value("StreamingTV"),
        "StreamingMovies": get_form_value("StreamingMovies"),
        "Contract": get_form_value("Contract"),
        "PaperlessBilling": get_form_value("PaperlessBilling"),
        "PaymentMethod": get_form_value("PaymentMethod"),
        "MonthlyCharges": get_form_value("MonthlyCharges", float, 0),
        "TotalCharges": get_form_value("TotalCharges", float, 0),
    }

    # Run prediction
    result = predict_customer(input_dict)

    return render_template("index.html", result=result)


# ---------------- RUN APP ---------------- #
@app.route("/predict_api", methods=["POST"])
def predict_api():
    data = request.get_json()

    result = predict_customer(data)

    return result
if __name__ == "__main__":
    app.run(debug=True)