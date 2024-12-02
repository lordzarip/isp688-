import streamlit as st
import numpy as np
import joblib

# Load the trained model and scaler
model = joblib.load('ckd_prediction_model.pkl')
scaler = joblib.load('feature_scaler.pkl')

# App title
st.title("Chronic Kidney Disease (CKD) Prediction App")

# Input fields
st.header("Enter Patient Data")
age = st.number_input("Age", min_value=1, max_value=120, value=25)
bp = st.number_input("Blood Pressure (BP)", min_value=0, max_value=200, value=80)
sg = st.slider("Specific Gravity (SG)", min_value=1.005, max_value=1.025, step=0.005)
al = st.number_input("Albumin", min_value=0, max_value=5, value=1)
su = st.number_input("Sugar", min_value=0, max_value=5, value=0)
rbc = st.selectbox("Red Blood Cells (RBC)", ["Normal", "Abnormal"])
pc = st.selectbox("Pus Cell (PC)", ["Normal", "Abnormal"])
pcc = st.selectbox("Pus Cell Clumps (PCC)", ["Not Present", "Present"])
ba = st.selectbox("Bacteria", ["Not Present", "Present"])
bgr = st.number_input("Blood Glucose Random (BGR)", min_value=0.0, max_value=500.0, value=120.0)
bu = st.number_input("Blood Urea (BU)", min_value=0.0, max_value=200.0, value=40.0)
sc = st.number_input("Serum Creatinine (SC)", min_value=0.0, max_value=15.0, value=1.0)
sod = st.number_input("Sodium (SOD)", min_value=0.0, max_value=200.0, value=135.0)
pot = st.number_input("Potassium (POT)", min_value=0.0, max_value=10.0, value=4.5)
hemo = st.number_input("Hemoglobin (Hemo)", min_value=0.0, max_value=20.0, value=12.0)
wc = st.number_input("White Blood Cell Count (WC)", min_value=0.0, max_value=20000.0, value=8000.0)
rc = st.number_input("Red Blood Cell Count (RC)", min_value=0.0, max_value=10.0, value=5.0)
htn = st.selectbox("Hypertension (HTN)", ["No", "Yes"])
dm = st.selectbox("Diabetes Mellitus (DM)", ["No", "Yes"])
cad = st.selectbox("Coronary Artery Disease (CAD)", ["No", "Yes"])
appet = st.selectbox("Appetite", ["Good", "Poor"])
pe = st.selectbox("Pedal Edema (PE)", ["No", "Yes"])
ane = st.selectbox("Anemia (ANE)", ["No", "Yes"])

# Map inputs to numerical values
input_data = [
    age, bp, sg, al, su,
    0 if rbc == "Normal" else 1,
    0 if pc == "Normal" else 1,
    0 if pcc == "Not Present" else 1,
    0 if ba == "Not Present" else 1,
    bgr, bu, sc, sod, pot, hemo, wc, rc,
    0 if htn == "No" else 1,
    0 if dm == "No" else 1,
    0 if cad == "No" else 1,
    0 if appet == "Good" else 1,
    0 if pe == "No" else 1,
    0 if ane == "No" else 1,
]

# Predict button
if st.button("Predict"):
    # Scale input data
    scaled_data = scaler.transform([input_data])
    prediction = model.predict(scaled_data)[0]
    
    # Display result
    if prediction == 1:
        st.error("The patient is likely to have Chronic Kidney Disease.")
    else:
        st.success("The patient is unlikely to have Chronic Kidney Disease.")
