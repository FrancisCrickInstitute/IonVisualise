import os
import time
from pathlib import Path
import pandas as pd
import streamlit as st
from helper_functions import pca
from helper_functions import scatterplot as sc
from helper_functions import volcano_plot as vp

st.set_page_config(initial_sidebar_state="expanded")
wholepage = st.container()

# Initialize session state for data, navigation, and file paths if they do not exist
if "uploaded_data" not in st.session_state:
    st.session_state.uploaded_data = []

if "nav_state" not in st.session_state:
    st.session_state.nav_state = "Home"  # Default to Home page

if "file_paths" not in st.session_state:
    st.session_state.file_paths = []  # To store local file paths


def save_uploaded_file(uploaded_file):
    """Save uploaded file to a temporary directory and return the path."""
    temp_dir = "temp_files"
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    file_path = os.path.join(temp_dir, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return file_path


def stream_data(text):
    for word in text.split(" "):
        yield word + " "
        time.sleep(0.02)

def convert_csv(uploaded_files):
        new_files = []
        for file in uploaded_files:
            if file.name.endswith(".csv"):
                new_files.append(file)
                continue

            if file.name.endswith(".xls"):
                df = pd.read_excel(file)
                
            if file.name.endswith(".txt"):
                df = pd.read_csv(file, delimiter='\t')
            
            csv_file = f"temp_files/{Path(file.name).stem}.csv"
            
            df.to_csv(csv_file, index=False)
            new_files.append(csv_file)
        return new_files

def reset_app():
    """Reset session state and rerun the app."""
    st.session_state.uploaded_data = []
    st.session_state.file_paths = []
    st.rerun()  # This will reset the app


def homePage():
    wholepage.title("_Ion_:red[_Visualise_]")
    description = """
        An advanced interface designed for the visualization of mass spectrometry proteomics data, providing a 
        variety of analytical tools including :blue[Principal Component Analysis] (PCA), :blue[volcano plots] for differential 
        expression analysis, :blue[scatter plots] for data distribution, and :blue[time series] plots for tracking changes over 
        time. This interface allows researchers to explore and interpret complex proteomic datasets through intuitive 
        and interactive visual representations, enhancing the ability to identify trends, outliers, and key biological 
        insights.
        """
    wholepage.write_stream(stream_data(description))
    
    # If no files are uploaded, show the file uploader
    if not st.session_state.uploaded_data:
        uploaded_files = wholepage.file_uploader(
            "Upload data",
            type=["csv", "txt", "xls"],
            accept_multiple_files=True,
        )

        if uploaded_files:
            # Save files locally and store paths
            st.session_state.uploaded_data = uploaded_files
            st.session_state.file_paths = [
                save_uploaded_file(file) for file in uploaded_files
            ]
            
            uploaded_files = convert_csv(uploaded_files)

    # If files are uploaded, display them with an option to remove
    if st.session_state.uploaded_data:
        wholepage.success("Files uploaded:")
        for i, uploaded_file in enumerate(st.session_state.uploaded_data):
            col1, col2 = wholepage.columns([8, 1])
            col1.write(uploaded_file.name)
            # Add an "X" button to remove the file and reset the app
            if col2.button("X", key=f"remove_file_{i}"):
                st.session_state.uploaded_data.pop(i)
                st.session_state.file_paths.pop(i)
                st.rerun()
                # reset_app()  # Reset the app if a file is removed

def load_data(file_path):
    """Load data from the saved local file."""
    if file_path.endswith(".csv"):
        return pd.read_csv(file_path)
    elif file_path.endswith(".xls"):
        return pd.read_excel(file_path)
    else:
        return pd.read_csv(
            file_path, delimiter="\t"
        )  # Assuming txt is tab-delimited


def PCAPage(file_paths):
    wholepage.title("_PCA_")

    for file_path in file_paths:
        wholepage.write(f":blue[{os.path.basename(file_path)}]")
        df = load_data(file_path)

    proteins = df.iloc[:, 0].to_numpy()
    with wholepage:
        with st.sidebar:
            selected_protein = st.selectbox("Select protein", proteins)
            st.write(f"Selected protein: {selected_protein}")

    pca.pca_plot(df)


def volcanoPage(file_paths):
    wholepage.title("_Volcano plot_")

    for file_path in file_paths:
        wholepage.write(f":blue[{os.path.basename(file_path)}]")
        df = load_data(file_path)

    proteins = df.iloc[:, 0].to_numpy()
    with wholepage:
        with st.sidebar:
            selected_protein = st.selectbox("Select protein", proteins)
            st.write(f"Selected protein: {selected_protein}")

    vp.volcano_plot(df, "Fold_Change", "p_value")


def scatterPage(file_paths):
    wholepage.title("_Scatter plot_")

    for file_path in file_paths:
        wholepage.write(f":blue[{os.path.basename(file_path)}]")
        df = load_data(file_path)

    # Get all column names from the dataframe for selection
    column_options = df.select_dtypes(include=[float, int]).columns.tolist()

    with wholepage:
        with st.sidebar:
            # Let the user select the X and Y axes from the dataframe columns
            x_axis = st.selectbox("Select X-axis", column_options, index=column_options.index("Spectral_Count") if "Spectral_Count" in column_options else 0)
            y_axis = st.selectbox("Select Y-axis", column_options, index=column_options.index("Peptide_Count") if "Peptide_Count" in column_options else 1)
            selected_protein = st.selectbox("Select protein", df.iloc[:, 0].to_numpy())
            st.write(f"Selected protein: {selected_protein}")

    # Use selected columns for the scatter plot
    sc.scatter_with_smooth_lines(df, x_axis, y_axis)


def timeseriesPage(file_paths):
    wholepage.title("_Timeseries plot_")

    for file_path in file_paths:
        wholepage.write(f":blue[{os.path.basename(file_path)}]")
        df = load_data(file_path)

    proteins = df.iloc[:, 0].to_numpy()
    with wholepage:
        with st.sidebar:
            selected_protein = st.selectbox("Select protein", proteins)
            st.write(f"Selected protein: {selected_protein}")

    # sc.scatter_with_smooth_lines(df, df.iloc[:,0], df.iloc[:,4])

def main():
    nav1, nav2, nav3, nav4, nav5 = wholepage.columns(5)

    # Check which button is pressed and update session state
    if nav1.button("Home", use_container_width=True):
        st.session_state.nav_state = "Home"
    if nav2.button("PCA", use_container_width=True):
        st.session_state.nav_state = "PCA"
    if nav3.button("Volcano", use_container_width=True):
        st.session_state.nav_state = "Volcano"
    if nav4.button("Scatter", use_container_width=True):
        st.session_state.nav_state = "Scatter"
    if nav5.button("TimeSeries", use_container_width=True):
        st.session_state.nav_state = "TimeSeries"

    # If there are no files in session state and user tries to access another page
    if (st.session_state.nav_state in ["PCA", "Volcano", "Scatter", "TimeSeries"]) and len(
        st.session_state.file_paths
    ) == 0:
        wholepage.warning("Please upload data to proceed")
        st.session_state.nav_state = "Home"

    # Navigate to the selected page based on session state
    if st.session_state.nav_state == "Home":
        homePage()
    elif st.session_state.nav_state == "PCA":
        PCAPage(st.session_state.file_paths)
    elif st.session_state.nav_state == "Volcano":
        volcanoPage(st.session_state.file_paths)
    elif st.session_state.nav_state == "Scatter":
        scatterPage(st.session_state.file_paths)
    elif st.session_state.nav_state == "TimeSeries":
        timeseriesPage(st.session_state.file_paths)


main()
