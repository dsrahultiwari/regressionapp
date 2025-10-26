import os
import streamlit as st
import pandas as pd
from src import state_keys as K
from src.utils_io import read_csv, validate_salary_schema

st.set_page_config(page_title="Load Data", layout="centered")
st.title("📥 Load Data")

# Initialize session state
for k in [K.DF, K.XTRAIN, K.XTEST, K.YTRAIN, K.YTEST, K.MODEL, K.FEATURES, K.TRAIN_SIZE]:
    if k not in st.session_state:
        st.session_state[k] = None
if st.session_state[K.FEATURES] is None:
    st.session_state[K.FEATURES] = ["Experience"]

st.write("Upload your CSV with columns **Experience** and **Salary**. "
         "Alternatively, place a file at `data/Salary_Data.csv` and load it from there.")

tab_upload, tab_local = st.tabs(["Upload CSV", "Load from data/Salary_Data.csv"])

with tab_upload:
    file = st.file_uploader("Choose CSV", type=["csv"])
    if file is not None:
        try:
            df = read_csv(file)
            df = validate_salary_schema(df)
            st.session_state[K.DF] = df
            st.success("Data loaded from uploaded file.")
            st.dataframe(df.head())
        except Exception as e:
            st.error(str(e))

with tab_local:
    if st.button("Load local data/Salary_Data.csv"):
        local_path = os.path.join("data", "Salary_Data.csv")
        if not os.path.exists(local_path):
            st.error("File not found at data/Salary_Data.csv")
        else:
            try:
                df = read_csv(local_path)
                df = validate_salary_schema(df)
                st.session_state[K.DF] = df
                st.success("Data loaded from local file.")
                st.dataframe(df.head())
            except Exception as e:
                st.error(str(e))

# Show basic info
df = st.session_state.get(K.DF)
if df is not None:
    st.info(f"Rows: {len(df)} | Columns: {list(df.columns)}")
else:
    st.warning("No data loaded yet.")
