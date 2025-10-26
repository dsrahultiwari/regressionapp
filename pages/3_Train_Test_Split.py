import streamlit as st
from sklearn.model_selection import train_test_split
from src import state_keys as K

st.set_page_config(page_title="Train/Test Split", layout="centered")
st.title("✂️ Train/Test Split")

df = st.session_state.get(K.DF)
if df is None:
    st.warning("Please load data first in **1_📥_Load_Data**.")
    st.stop()

train_pct = st.slider("Train size (%)", min_value=60, max_value=95, value=80, step=1)

if st.button("Create Split"):
    X = df[["Experience"]].values
    y = df["Salary"].values
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, train_size=train_pct / 100.0, random_state=42
    )

    st.session_state[K.XTRAIN] = X_train
    st.session_state[K.XTEST] = X_test
    st.session_state[K.YTRAIN] = y_train
    st.session_state[K.YTEST] = y_test
    st.session_state[K.TRAIN_SIZE] = train_pct / 100.0
    st.session_state[K.FEATURES] = ["Experience"]

    st.success(f"Split created → Train: {len(X_train)}, Test: {len(X_test)}")
