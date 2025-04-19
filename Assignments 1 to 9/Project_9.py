# Build a Python Website With Streamlit

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("My First Streamlit App")
 

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    st.write("File uploaded successfully!")
    df = pd.read_csv(uploaded_file)

    st.subheader("Data Summary")
    st.write(df.describe())
    
    st.subheader("Filter Data")
    columns = df.columns.tolist()
    selecterd_column = st.selectbox("Select a column to filter", columns)
    unique_values = df[selecterd_column].unique()
    selected_value = st.selectbox("Select a value to filter", unique_values)

    filtered_df = df[df[selecterd_column] == selected_value]
    st.write(filtered_df)

    st.subheader("Plot Data")
    x_column = st.selectbox("Select x-axis column", columns)
    y_column = st.selectbox("Select y-axis column", columns)

    if st.button("Generate Plot"):
       st.line_chart(filtered_df.set_index(x_column)[y_column]) 
    else:
        st.write("Please upload a CSV file.")

    st.subheader("Download Data")
    csv = df.to_csv(index=False)
    st.download_button("Download CSV", csv, "data.csv", "text/csv")