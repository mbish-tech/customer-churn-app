import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load model pipeline
model = joblib.load("churn_model.pkl")

st.title("Customer Churn Prediction")

# Collect full input
age = st.slider("Age", 18, 80, 30)
monthly_fee = st.slider("Monthly Fee ($)", 0, 500, 50)
total_watch_hours = st.slider("Total Watch Hours", 0, 10000, 100)
last_login = st.slider("Last Login (days ago)", 0, 60, 10)
support_tickets = st.slider("Support Tickets", 0, 20, 1)
watch_hours_per_day = st.slider("Watch Hours Per Day", 0.0, 24.0, 2.0)
heavy_user = st.selectbox("Heavy User?", ["Yes", "No"])
recent_login = st.selectbox("Recent Login?", ["Yes", "No"])
support_watch_interaction = st.slider("Support Watch Interaction Score", 0.0, 1.0, 0.5)
gender = st.selectbox("Gender", ["Male", "Female"])
subscription_plan = st.selectbox("Subscription Plan", ["Premium", "Standard", "Basic"])
payment_method = st.selectbox("Payment Method", ["Mobile Money", "PayPal", "Credit Card"])
login_bucket = st.selectbox("Login Bucket", ["8-14", "15-30", "0-15", "30+"])

# Process categorical into one-hot encoding
gender_male = 1 if gender == "Male" else 0
subscription_premium = 1 if subscription_plan == "Premium" else 0
subscription_standard = 1 if subscription_plan == "Standard" else 0
payment_mobile = 1 if payment_method == "Mobile Money" else 0
payment_paypal = 1 if payment_method == "PayPal" else 0
login_8_14 = 1 if login_bucket == "8-14" else 0
login_15_30 = 1 if login_bucket == "15-30" else 0

# Create full input dataframe
input_data = pd.DataFrame([{
    'Age': age,
    'MonthlyFee': monthly_fee,
    'TotalWatchHours': total_watch_hours,
    'LastLogin': last_login,
    'SupportTickets': support_tickets,
    'WatchHoursPerDay': watch_hours_per_day,
    'HeavyUser': heavy_user == "Yes",
    'RecentLogin': recent_login == "Yes",
    'Support_Watch_Interaction': support_watch_interaction,
    'Gender_Male': gender_male,
    'SubscriptionPlan_Premium': subscription_premium,
    'SubscriptionPlan_Standard': subscription_standard,
    'PaymentMethod_Mobile Money': payment_mobile,
    'PaymentMethod_PayPal': payment_paypal,
    'LoginBucket_8-14': login_8_14,
    'LoginBucket_15-30': login_15_30
}])

# Prediction
if st.button("Predict Churn"):
    pred = model.predict(input_data)[0]
    proba = model.predict_proba(input_data)[0][1]
    st.write(f"Prediction: {'Churn' if pred == 1 else 'No Churn'}")
    st.write(f"Churn Probability: {proba:.2f}")
