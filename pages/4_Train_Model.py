import os
import streamlit as st
from src import state_keys as K
from src.utils_model import train_linear_regression, evaluate
from src.utils_io import save_pickle, save_json

st.set_page_config(page_title="Train Model", layout="centered")
st.title("🧠 Train Model")

if st.session_state.get(K.XTRAIN) is None:
    st.warning("Please create a split first in **3_✂️_Train_Test_Split**.")
    st.stop()

if st.button("Train Linear Regression"):
    X_train = st.session_state[K.XTRAIN]
    y_train = st.session_state[K.YTRAIN]
    X_test = st.session_state[K.XTEST]
    y_test = st.session_state[K.YTEST]

    model = train_linear_regression(X_train, y_train)
    st.session_state[K.MODEL] = model

    # Metrics
    m_train = evaluate(model, X_train, y_train)
    m_test  = evaluate(model, X_test,  y_test)

    st.success("Model trained.")
    st.write(f"**Intercept:** {model.intercept_:.2f}")
    st.write(f"**Coefficient (per year):** {model.coef_[0]:.2f}")
    st.write(f"**R² (train):** {m_train['r2']:.4f}")
    st.write(f"**R² (test):** {m_test['r2']:.4f}")

    # Save artifacts
    save_pickle(model, "artifacts/model.pkl")
    save_json(st.session_state[K.FEATURES], "artifacts/feature_list.json")
    st.caption("Saved: `artifacts/model.pkl` and `artifacts/feature_list.json`")
else:
    st.info("Click the button above to train the model.")
