import pickle
from fastapi import FastAPI
from pydantic import BaseModel
import json

# Create FastAPI instance
app = FastAPI()

# Input format
class ModelInput(BaseModel):
    Age: float
    Gender: str
    Tenure: float
    Usage_Frequency: float
    Payment_Delay: float
    Subscription_Type: str
    Contract_Length: str
    Total_Spend: float
    Last_Interaction: float

# Load model
with open("churn_model.pkl", "rb") as f:
    model_data = pickle.load(f)

loaded_model = model_data["model"]
feature_names = model_data["features_names"]

# API endpoint
@app.post('/customer_churn_prediction')
def churn_pred(input_parameters: ModelInput):
    input_data = input_parameters.json()
    input_dict = json.loads(input_data)
    
    input_list = [
        input_dict['Age'],
        input_dict['Gender'],
        input_dict['Tenure'],
        input_dict['Usage_Frequency'],
        input_dict['Payment_Delay'],
        input_dict['Subscription_Type'],
        input_dict['Contract_Length'],
        input_dict['Total_Spend'],
        input_dict['Last_Interaction']
    ]
    
    prediction = loaded_model.predict([input_list])
    
    if prediction[0] == 0:
        return 'Customer will churn out'
    else:
        return 'Customer will not churn out'
