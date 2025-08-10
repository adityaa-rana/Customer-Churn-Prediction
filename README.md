# 📊 Customer Churn Prediction – End-to-End ML Pipeline with Deployment

## 📌 Project Overview
The **Customer Churn Prediction** project focuses on predicting whether a customer is likely to leave a business based on historical data.  
While the churn prediction problem itself is quite common, my goal was to **implement an industry-ready, end-to-end ML solution** — from raw data to a fully deployable model API.

---

## 🎯 Key Highlights
- **Complete EDA & Feature Engineering** – handled missing values, categorical encoding, outlier detection, and scaling.  
- **Automated ML Pipelining** – streamlined preprocessing, model training, and evaluation into a reproducible workflow.  
- **Multiple Model Implementations** – compared Logistic Regression, Random Forest, XGBoost, and others to find the optimal model.  
- **High Accuracy** – achieved up to **99% accuracy** on the test set.  
- **Deployment via FastAPI** – served the model as an API endpoint for real-world integration.



---

## 🛠️ Tech Stack
- **Language:** Python  
- **Libraries:** Pandas, NumPy, Scikit-learn, XGBoost, Matplotlib, Seaborn  
- **Deployment:** FastAPI, Uvicorn  
- **Other Tools:** Joblib/Pickle for model serialization

---

## 🔍 Workflow
1. **Data Collection & EDA**
   - Loaded dataset
   - Analyzed distributions, correlations, and class imbalance
   - Visualized insights with Matplotlib & Seaborn  

2. **Feature Engineering**
   - Encoded categorical variables
   - Scaled numerical features
   - Created derived features to improve model performance  

3. **Model Training & Evaluation**
   - Implemented ML pipeline with preprocessing and training steps
   - Compared multiple algorithms
   - Selected best model based on accuracy & recall  

4. **Deployment**
   - Exported final model using Joblib
   - Created FastAPI app to serve predictions via REST API
   - Tested endpoints locally using Postman

---

## 🚀 How to Run Locally

### 1️⃣ Clone Repository
```bash
git clone https://github.com/yourusername/customer_churn_prediction.git
cd customer_churn_prediction

  
