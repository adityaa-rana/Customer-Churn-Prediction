
import json
import requests

url = 'http://127.0.0.1:8000/customer_churn_prediction'

input_data_for_model = {
    'Age': 35.0,
    'Gender': 'Male',               # Example: 0 = Female, 1 = Male
    'Tenure': 12.0,
    'Usage_Frequency': 4.5,
    'Payment_Delay': 1.0,
    'Subscription_Type': 'Standard',    # Example: 0 = Basic, 1 = Standard, 2 = Premium
    'Contract_Length': 'Monthly',      # Example: 0 = Monthly, 1 = Quarterly, 2 = Yearly
    'Total_Spend': 2500.75,
    'Last_Interaction': 15.0
}

input_json=json.dumps(input_data_for_model)
response = requests.post(url, data=input_json)
print(response.text)
