import pandas as pd
import plotly.express as px
import streamlit as st
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


def pca_plot(dataframe: pd.DataFrame, n_components: int = 2):
    # Ensure the DataFrame only contains numerical data
    dataframe = dataframe.select_dtypes(include=[float, int])

    # Standardize the data
    scaler = StandardScaler()
    standardized_data = scaler.fit_transform(dataframe)

    # Perform PCA
    pca = PCA(n_components=n_components)
    pca_result = pca.fit_transform(standardized_data)

    # Create a PCA DataFrame for plotting
    pca_df = pd.DataFrame(
        data=pca_result, columns=[f"PC{i+1}" for i in range(n_components)]
    )

    # Plot using Plotly
    fig = px.scatter(
        pca_df,
        x="PC1",
        y="PC2",
        labels={
            "PC1": f"PC1 ({pca.explained_variance_ratio_[0]*100:.2f}% Variance)",
            "PC2": f"PC2 ({pca.explained_variance_ratio_[1]*100:.2f}% Variance)",
        },
        title="PCA Plot",
    )

    # Streamlit display
    st.plotly_chart(fig)

def pcmain():
    # Example usage in Streamlit app
    st.title("PCA Plot Example with Plotly")
    uploaded_file = st.file_uploader("Upload your CSV file", type="csv")

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("Data Preview", df.head())

        # Generate PCA plot
        pca_plot(df)
