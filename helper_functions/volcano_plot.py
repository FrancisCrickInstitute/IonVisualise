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

def vpmain():
    # Example usage in Streamlit app
    st.title("Volcano Plot Example with Plotly")
    uploaded_file = st.file_uploader("Upload your CSV file", type="csv")

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("Data Preview", df.head())

        # Ask for column names for fold change and p-value
        fold_change_col = st.text_input(
            "Enter the column name for fold change (e.g., 'log2FoldChange')",
            value="log2FoldChange",
        )
        p_value_col = st.text_input(
            "Enter the column name for p-values (e.g., 'pvalue')", value="pvalue"
        )

        # Generate Volcano plot
        volcano_plot(df, fold_change_col, p_value_col)
