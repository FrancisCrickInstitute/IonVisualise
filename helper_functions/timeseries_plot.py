import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

import plotly.express as px
import streamlit as st


def timeseries_plot(df, selected_protein):
    # Filter the DataFrame for the selected protein
    protein_df = df[df['Protein_ID'] == selected_protein]

    if protein_df.empty:
        st.warning("No data available for the selected protein.")
        return

    # Plotly line plot with different colors for Virus_Type
    fig = px.line(
        protein_df,
        x='time',
        y='Peptide_Count',
        color='Virus_Type',
        title=f"Peptide Count Over Time for {selected_protein}",
        labels={
            'time': "Time",
            'Peptide_Count': "Peptide Count",
            'Virus_Type': "Virus Type"
        },
    )

    # Add markers to the line plot
    fig.update_traces(mode="lines+markers")

    # Display the plot with Streamlit
    st.plotly_chart(fig)


def tsmain():
    # Example usage in Streamlit app
    st.title("Time Series Example with Plotly")
    uploaded_file = st.file_uploader("Upload your CSV file", type="csv")

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("Data Preview", df.head())
        # Time Series
        timeseries_plot(df)
