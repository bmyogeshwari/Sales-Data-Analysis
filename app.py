import streamlit as st
import pandas as pd

st.set_page_config(page_title="Sales Data Analysis", layout="wide")

st.title("📊 Sales Data Analysis App")

# Upload file
uploaded_file = st.file_uploader(
    "Upload your sales dataset (CSV or Excel)",
    type=["csv", "xlsx"]
)

if uploaded_file is not None:

    # Load dataset safely
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file, encoding="latin1")
    else:
        df = pd.read_excel(uploaded_file)

    st.success("✅ File loaded successfully!")

    # Show raw data
    st.subheader("🔍 Dataset Preview")
    st.dataframe(df.head())

    # Show column names (VERY IMPORTANT)
    st.subheader("📌 Column Names in Your Dataset")
    st.write(list(df.columns))

    # Select columns dynamically (prevents KeyError)
    st.subheader("⚙️ Select Columns")

    date_col = st.selectbox("Select Date column", df.columns)
    sales_col = st.selectbox("Select Sales column", df.columns)

    # Convert types safely
    df[date_col] = pd.to_datetime(df[date_col], errors="coerce")
    df[sales_col] = pd.to_numeric(df[sales_col], errors="coerce")

    df.dropna(subset=[date_col, sales_col], inplace=True)

    # Group by date
    sales_over_time = df.groupby(date_col)[sales_col].sum()

    st.subheader("📈 Sales Over Time")
    st.line_chart(sales_over_time)

else:
    st.info("⬆️ Please upload a dataset to begin")