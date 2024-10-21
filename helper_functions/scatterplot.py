import pandas as pd
import plotly.graph_objs as go
import statsmodels.api as sm
import streamlit as st


def scatter_with_smooth_lines(
    dataframe: pd.DataFrame, x_col: str, y_col: str, frac: float = 0.3
):
    '''
    Draw a scatter plot with smooth lines using Plotly.
    :param dataframe: The DataFrame containing the data.
    :param x_col: The column for the x-axis.
    :param y_col: The column for the y-axis.
    :param frac: The fraction of the data used when estimating each y-value.
    '''
    # Ensure the DataFrame contains the specified columns
    if x_col not in dataframe.columns or y_col not in dataframe.columns:
        st.error(
            f"Please ensure your dataframe contains '{x_col}' and '{y_col}' columns."
        )
        return

    # Extract x and y values
    x = dataframe[x_col]
    y = dataframe[y_col]

    # Fit a smooth line using LOWESS (Locally Weighted Scatterplot Smoothing)
    lowess = sm.nonparametric.lowess(y, x, frac=frac)

    # Create scatter plot with Plotly
    scatter_trace = go.Scatter(
        x=x,
        y=y,
        mode="markers",
        name="Data",
        marker=dict(color="grey", opacity=0.6),
    )
    smooth_trace = go.Scatter(
        x=lowess[:, 0],
        y=lowess[:, 1],
        mode="lines",
        name="Smooth Line (LOWESS)",
        line=dict(color="red", width=2),
    )

    fig = go.Figure(data=[scatter_trace, smooth_trace])
    fig.update_layout(
        title=f"Scatter Plot with Smooth Line ({x_col} vs {y_col})",
        xaxis_title=x_col,
        yaxis_title=y_col,
    )

    # Streamlit display
    st.plotly_chart(fig)