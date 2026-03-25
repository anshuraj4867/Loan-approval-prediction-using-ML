# Loan-approval-prediction-using-ML
This project is an end-to-end Loan Approval Prediction System built using Machine Learning and Web Technologies. It automates the process of determining whether a loan application should be approved or rejected based on applicant details.

###Overview

Traditional loan approval processes are manual, time-consuming, and prone to human bias. This project provides a data-driven solution by using machine learning models to predict loan approval with high accuracy.

The system is designed as a web-based application, where users can enter their details and receive instant predictions.
###Features
1.Machine Learning-based prediction system
2.Interactive web interface (HTML, CSS, JavaScript)
3.Flask backend API for real-time predictions
4.Instant loan approval results (Approved / Rejected)
5.Probability score for better decision understanding
6.High accuracy using XGBoost model

###Project Architecture
User Input (Frontend)
        ↓
JavaScript API Call
        ↓
Flask Backend (API)
        ↓
Data Preprocessing (Encoding + Scaling)
        ↓
Machine Learning Model (XGBoost)
        ↓
Prediction Output (Frontend Display)

###Project Structure
├── app.py              # Flask backend
├── loan_model.pkl      # Trained ML model
├── scaler.pkl          # Scaler for preprocessing
├── label_encoders.pkl  # Encoders for categorical data
├── index.html          # Frontend UI
├── styles.css          # Styling
├── script.js           # Frontend logic
└── loan3.ipynb         # Model training notebook
