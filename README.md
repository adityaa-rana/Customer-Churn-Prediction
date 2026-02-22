# 🚀 Customer Churn Prediction System (Production-Ready)

A full-stack, production-style **Customer Churn Prediction** web application built using Machine Learning and Flask.
The system predicts churn probability, segments customers into risk tiers, and provides explainable AI insights.

---

## 🎯 Project Highlights

✅ End-to-end ML pipeline
✅ SMOTE for class imbalance
✅ Hyperparameter tuning with GridSearchCV
✅ Explainable AI using SHAP
✅ Dynamic threshold slider (business control)
✅ Real-time prediction simulator
✅ Flask production deployment
✅ Interactive professional UI

---

## 🧠 Problem Statement

Customer churn is a critical business problem in subscription-based companies.
This project predicts the probability that a customer will churn and provides actionable insights for retention teams.

---

## 🏗️ Project Architecture

```
ML Projects/
│
├── templates/
│   └── index.html          # Frontend UI (HTML + CSS + JS)
│
├── utils/
│   └── predict.py          # Prediction pipeline + SHAP explanations
│
├── app.py                  # Flask backend server
├── main.py                 # (optional) local testing script
│
├── churn_model.pkl         # Trained ML pipeline
├── feature_names.pkl       # Feature names after preprocessing
├── config.json             # Threshold configuration
│
└── README.md               # Project documentation
```

---

## ⚙️ Tech Stack

**Machine Learning**

* Logistic Regression
* Random Forest
* SMOTE (imbalanced-learn)
* GridSearchCV
* Scikit-learn Pipeline

**Explainable AI**

* SHAP (global + local explanations)

**Backend**

* Flask (REST API)

**Frontend**

* HTML5
* CSS3 (glassmorphism UI)
* Vanilla JavaScript
* Fetch API (real-time inference)

---

## 🔄 ML Pipeline Flow

```
Raw Customer Data
      ↓
Preprocessing (ColumnTransformer)
      ↓
SMOTE (class balancing)
      ↓
Model Training (Logistic Regression / RF)
      ↓
Probability Output
      ↓
Dynamic Risk Segmentation
      ↓
SHAP Explainability
```

---

## 🎚️ Dynamic Threshold System (Advanced Feature)

Unlike basic churn models, this system includes a **business-controlled threshold slider**.

### 🔹 What it does

* Model outputs probability (fixed)
* Business teams adjust risk sensitivity
* No retraining required

### 🔹 Why it matters

In real companies:

* Retention budget changes
* Campaign capacity changes
* Risk appetite changes

This feature makes the system **production realistic**.

---

## 🔍 Explainable AI (SHAP)

The system provides:

* Global feature importance
* Local customer-level explanations
* Top 5 churn drivers per prediction

This improves model transparency and business trust.

---

## 🚀 How to Run Locally

### 1️⃣ Clone repository

```bash
git clone <your-repo-link>
cd ML Projects
```

---

### 2️⃣ Create virtual environment

```bash
python -m venv .venv
```

Activate:

**Windows**

```bash
.venv\Scripts\activate
```

**Mac/Linux**

```bash
source .venv/bin/activate
```

---

### 3️⃣ Install dependencies

```bash
pip install flask pandas numpy scikit-learn imbalanced-learn shap
```

---

### 4️⃣ Run the Flask app

```bash
python app.py
```

Open browser:

```
http://127.0.0.1:5000
```

---

## 📊 Current Features

* ✅ Churn probability prediction
* ✅ Risk segmentation (Low / Medium / High)
* ✅ Real-time simulator
* ✅ Threshold slider
* ✅ SHAP top drivers
* ✅ Professional UI

---

## 🚀 Upcoming Enhancements

* 📈 Churn probability distribution dashboard
* 🧾 Top risk customers table
* 🌍 Global feature importance chart
* 📉 Model performance dashboard
* ☁️ Cloud deployment (Render/AWS)

---

## 👨‍💻 Author

**Aditya Rana**

If you found this project helpful, feel free to ⭐ the repo.

---

## 🧠 Interview Talking Points

This project demonstrates:

* End-to-end ML deployment
* Handling class imbalance
* Production ML pipeline design
* Explainable AI integration
* Business-aware threshold tuning
* Full-stack ML system building

<img width="1077" height="987" alt="image" src="https://github.com/user-attachments/assets/0ae5862b-b560-44d5-84da-1eaa1553affa" />

<img width="1181" height="881" alt="image" src="https://github.com/user-attachments/assets/b42f92f1-e320-47e1-90ff-f71ca0a5e369" />


