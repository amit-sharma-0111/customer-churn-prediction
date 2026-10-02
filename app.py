import streamlit as st
import numpy as np
import joblib
import pandas as pd

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Customer Churn Predictor",
    page_icon="📊",
    layout="centered"
)

# ---------------- LOAD MODEL (CACHED) ----------------
@st.cache_resource
def load_model():
    try:
        model = joblib.load("models/churn_model.pkl")
        return model, None
    except FileNotFoundError:
        return None, "❌ Model file not found!"
    except Exception as e:
        return None, f"❌ Model load error: {str(e)}"

model, error = load_model()

# ---------------- TITLE ----------------
st.title("📊 Customer Churn Prediction Dashboard")
st.write("Predict whether a customer will churn based on behavior data.")

if error:
    st.error(error)
    st.stop()
else:
    st.success("✅ Model Loaded Successfully")

st.divider()

# ---------------- INPUT SECTION ----------------
st.header("👤 Customer Information")

col1, col2 = st.columns(2)

with col1:
    age = st.slider("Age", 18, 80, 30)
    gender = st.selectbox("Gender", ["Male", "Female"])
    tenure = st.slider("Tenure (Months)", 0, 72, 12)

with col2:
    usage_frequency = st.slider("Usage Frequency", 0, 50, 10)
    support_calls = st.slider("Support Calls", 0, 20, 2)
    payment_delay = st.slider("Payment Delay (Days)", 0, 30, 5)

st.divider()

# ---------------- SUBSCRIPTION ----------------
st.header("📦 Subscription Details")

subscription_type = st.selectbox(
    "Subscription Type",
    ["Basic", "Standard", "Premium"]
)

contract_length = st.slider("Contract Length (Months)", 0, 24, 12)
total_spend = st.number_input("Total Spend", 0, 10000, 1000)
last_interaction = st.slider("Days Since Last Interaction", 0, 60, 10)

# ---------------- INPUT VALIDATION ----------------
def validate_inputs():
    warnings = []
    if support_calls > 15:
        warnings.append("⚠️ Very high support calls — likely churn risk!")
    if payment_delay > 20:
        warnings.append("⚠️ High payment delay detected!")
    if tenure < 3 and total_spend < 100:
        warnings.append("⚠️ New customer with very low spend!")
    return warnings

validation_warnings = validate_inputs()
if validation_warnings:
    for w in validation_warnings:
        st.warning(w)

# ---------------- ENCODING ----------------
gender_map = {"Male": 1, "Female": 0}
sub_map = {"Basic": 0, "Standard": 1, "Premium": 2}

gender_encoded = gender_map[gender]
subscription_encoded = sub_map[subscription_type]

# ---------------- FEATURE ORDER ----------------
input_data = np.array([[
    age,
    gender_encoded,
    tenure,
    usage_frequency,
    support_calls,
    payment_delay,
    subscription_encoded,
    contract_length,
    total_spend,
    last_interaction
]])

# ---------------- PREDICTION ----------------
st.divider()

col_predict, col_reset = st.columns([3, 1])

with col_predict:
    predict_btn = st.button("🚀 Predict Churn", use_container_width=True)

with col_reset:
    reset_btn = st.button("🔄 Reset", use_container_width=True)

if reset_btn:
    st.rerun()

if predict_btn:
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]
    risk_pct = probability * 100

    st.divider()
    st.subheader("📈 Prediction Result")

    if prediction == 1:
        st.error(f"⚠️ Customer Likely to CHURN — Risk: {risk_pct:.2f}%")
    else:
        st.success(f"✅ Customer Likely to STAY — Churn Risk: {risk_pct:.2f}%")

    st.markdown("#### 🎯 Churn Risk Meter")
    st.progress(int(risk_pct))

    if risk_pct < 30:
        st.info("🟢 Low Risk")
    elif risk_pct < 60:
        st.warning("🟡 Medium Risk")
    else:
        st.error("🔴 High Risk")

    if "history" not in st.session_state:
        st.session_state.history = []

    st.session_state.history.append({
        "Age": age,
        "Gender": gender,
        "Tenure": tenure,
        "Subscription": subscription_type,
        "Support Calls": support_calls,
        "Payment Delay": payment_delay,
        "Total Spend": total_spend,
        "Risk %": f"{risk_pct:.2f}%",
        "Result": "Churn ⚠️" if prediction == 1 else "Stay ✅"
    })

# ---------------- HISTORY ----------------
if "history" in st.session_state and len(st.session_state.history) > 0:
    st.divider()
    st.subheader("🕐 Prediction History")
    df_history = pd.DataFrame(st.session_state.history)
    st.dataframe(df_history, use_container_width=True)

    if st.button("🗑️ Clear History"):
        st.session_state.history = []
        st.rerun()