import streamlit as st
from src import state_keys as K
from src.utils_plots import scatter_with_trend

st.set_page_config(page_title="EDA", layout="centered")
st.title("📊 Quick EDA")

df = st.session_state.get(K.DF)
if df is None:
    st.warning("Please load data first in **1_📥_Load_Data**.")
    st.stop()

c1, c2 = st.columns(2)
with c1:
    st.subheader("Summary")
    st.write(df.describe())

    st.subheader("Correlation")
    st.write(df[["Experience", "Salary"]].corr())

with c2:
    st.subheader("Scatter & Trend")
    fig = scatter_with_trend(df)
    st.pyplot(fig)
