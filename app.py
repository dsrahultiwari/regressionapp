import streamlit as st

st.set_page_config(page_title="Salary Regressor", layout="centered")

st.title("💼 Salary Regressor — End-to-End")
st.write(
    """
This app predicts **Salary** from **Experience** with a clean, step-by-step flow.

**Pages (left sidebar):**
1) Load your CSV  
2) Quick EDA  
3) Train/Test Split  
4) Train Model  
5) Predict Salary

**Tip:** Keep your file named `Salary_Data.csv` with columns: `Experience`, `Salary`.  
"""
)
st.info("Use the sidebar to open page **1_📥_Load_Data** and upload your CSV.")
