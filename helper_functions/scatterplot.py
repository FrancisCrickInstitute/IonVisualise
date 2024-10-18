import pandas as pd
import plotly.graph_objs as go
import statsmodels.api as sm
import streamlit as st


def scatter_with_smooth_lines(
    dataframe: pd.DataFrame, x_col: str, y_col: str, frac: float = 0.3
):
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

def scmain():
    # Example usage in Streamlit app
    st.title("Scatter Plot with Smooth Lines Example with Plotly")
    uploaded_file = st.file_uploader("Upload your CSV file", type="csv")

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("Data Preview", df.head())

        # Ask for column names for x and y axes
        x_col = st.text_input("Enter the column name for the x-axis", value="x")
        y_col = st.text_input("Enter the column name for the y-axis", value="y")

        # Generate scatter plot with smooth lines
        scatter_with_smooth_lines(df, x_col, y_col)
