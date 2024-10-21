import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

import plotly.express as px
import streamlit as st


def timeseries_plot(df, selected_protein):
    '''
    Plot a line plot of Peptide Count over time for the selected protein.
    :param df: The DataFrame containing the data.
    :param selected_protein: The selected protein to plot.
    '''
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

