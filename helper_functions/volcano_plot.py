import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st


def volcano_plot(
    dataframe: pd.DataFrame,
    fold_change_col: str,
    p_value_col: str,
    threshold_fc: float = 1.0,
    threshold_pval: float = 0.05,
):
    '''
    Plot a Volcano plot using Plotly.
    :param dataframe: The DataFrame containing the data.
    :param fold_change_col: The column name for fold change.
    :param p_value_col: The column name for p-values.
    :param threshold_fc: The threshold for fold change to consider a gene differentially expressed.
    :param threshold_pval: The threshold for p-value to consider a gene differentially expressed.
    '''
    # Ensure the DataFrame contains the specified columns
    if (
        fold_change_col not in dataframe.columns
        or p_value_col not in dataframe.columns
    ):
        st.error(
            f"Please ensure your dataframe contains '{fold_change_col}' and '{p_value_col}' columns."
        )
        return

    # Convert p-values to -log10(p-value)
    dataframe["-log10(p-value)"] = -np.log10(dataframe[p_value_col])

    # Label significance
    dataframe["Significance"] = "Not Significant"
    dataframe.loc[
        (dataframe[fold_change_col] >= threshold_fc)
        & (dataframe[p_value_col] < threshold_pval),
        "Significance",
    ] = "Upregulated"
    dataframe.loc[
        (dataframe[fold_change_col] <= -threshold_fc)
        & (dataframe[p_value_col] < threshold_pval),
        "Significance",
    ] = "Downregulated"

    # Plot using Plotly
    fig = px.scatter(
        dataframe,
        x=fold_change_col,
        y="-log10(p-value)",
        color="Significance",
        title="Volcano Plot",
        labels={
            fold_change_col: "Log2 Fold Change",
            "-log10(p-value)": "-Log10(P-value)",
        },
        color_discrete_map={
            "Upregulated": "red",
            "Downregulated": "blue",
            "Not Significant": "grey",
        },
    )

    # Streamlit display
    st.plotly_chart(fig)
