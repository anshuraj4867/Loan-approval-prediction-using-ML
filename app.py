from flask import Flask, request, jsonify
import pickle
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load saved objects
with open("loan_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

with open("label_encoders.pkl", "rb") as f:
    label_encoders = pickle.load(f)

@app.route("/")
def home():
    return "Loan Prediction API is Running!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json

        input_df = pd.DataFrame([{
            'person_age': float(data["person_age"]),
            'person_gender': label_encoders['person_gender'].transform(
                [data["person_gender"].strip().lower()]
            )[0],
            'person_education': label_encoders['person_education'].transform(
                [data["person_education"].strip().title()]
            )[0],
            'person_income': float(data["person_income"]),
            'person_emp_exp': int(data["person_emp_exp"]),
            'person_home_ownership': label_encoders['person_home_ownership'].transform(
                [data["person_home_ownership"].strip().upper()]
            )[0],
            'loan_amnt': float(data["loan_amnt"]),
            'loan_intent': label_encoders['loan_intent'].transform(
                [data["loan_intent"].strip().upper()]
            )[0],
            'loan_int_rate': float(data["loan_int_rate"]),
            'loan_percent_income': float(data["loan_percent_income"]),
            'cb_person_cred_hist_length': float(data["cb_person_cred_hist_length"]),
            'credit_score': int(data["credit_score"]),
            'previous_loan_defaults_on_file': label_encoders['previous_loan_defaults_on_file'].transform(
                [data["previous_loan_defaults_on_file"].strip().capitalize()]
            )[0]
        }])

        # Scale input
        input_scaled = scaler.transform(input_df)

        # Prediction + Probability
        prediction = model.predict(input_scaled)[0]
        prob = model.predict_proba(input_scaled)[0][1]  # Probability of approval

        result = "Approved" if prediction == 1 else "Rejected"

        return jsonify({
            "prediction": result,
            "probability": round(float(prob) * 100, 2)
        })

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
