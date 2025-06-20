import streamlit as st
import pandas as pd
st.title("Welcome!")

st.title("Ethical AI Bias Detection Tool")

uploaded_file = st.file_uploader("Upload a CSV dataset", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Dataset preview:")
    st.write(df.head())
    
    sensitive_col = st.selectbox("Select sensitive attribute", df.columns)
    target_col = st.selectbox("Select target label", df.columns)

    if st.button("Analyze Bias"):
        overall_pos_rate = df[target_col].mean()
        groups = df[sensitive_col].unique()
        st.write(f"Overall positive rate: {overall_pos_rate:.2f}")
        for group in groups:
            group_df = df[df[sensitive_col] == group]
            group_pos_rate = group_df[target_col].mean()
            st.write(f"{group}: {group_pos_rate:.2f} (Difference: {group_pos_rate - overall_pos_rate:.2f})")
