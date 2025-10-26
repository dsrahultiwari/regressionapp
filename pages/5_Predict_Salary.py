import os
import streamlit as st
from src import state_keys as K
from src.utils_model import predict_single
from src.utils_io import load_pickle, load_json

st.set_page_config(page_title="Predict Salary", layout="centered")
st.title("🔮 Predict Salary")

model = st.session_state.get(K.MODEL)
features = st.session_state.get(K.FEATURES)

# Fallback: load from artifacts if not in memory
if model is None:
    if os.path.exists("artifacts/model.pkl") and os.path.exists("artifacts/feature_list.json"):
        model = load_pickle("artifacts/model.pkl")
        features = load_json("artifacts/feature_list.json")
        st.session_state[K.MODEL] = model
        st.session_state[K.FEATURES] = features

if model is None:
    st.warning("No trained model found. Train it in **4_🧠_Train_Model**.")
    st.stop()

exp = st.number_input("Experience (years)", min_value=0.0, max_value=60.0, value=3.0, step=0.1)
if st.button("Predict"):
    pred = predict_single(model, exp)
    st.success(f"Predicted Salary: **{pred:,.2f}**")
