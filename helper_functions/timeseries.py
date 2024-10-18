import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

def timeseries_plot(df):
    # Streamlit display
    fig = px.scatter(
        df,  # Use 'df' directly
        x='Peptide_Count',  # X-axis set to Peptide_Count
        y='time',  # Y-axis set to time
        title="Spectral_Count",  # Updated title
        labels={
            'Peptide_Count': "Peptide Count",
            'Spectral_Count': "Spectral_Count",  # Label for Y-axis
        },
    )

    st.plotly_chart(fig)

def vpmain():
    # Example usage in Streamlit app
    st.title("Time Series Example with Plotly")
    uploaded_file = st.file_uploader("Upload your CSV file", type="csv")

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("Data Preview", df.head())
        # Generate Volcano plot
        timeseries_plot(df)
