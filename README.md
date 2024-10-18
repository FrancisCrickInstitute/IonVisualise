
# Data Visualization App

This repository contains a data visualization app built using Streamlit. It provides interactive tools for visualizing data, including PCA plots, scatter plots with smooth lines, and volcano plots. The app is modular, with each visualization function located in a separate Python file under the `helper_functions` directory.

## Directory Structure

```
└── ./
    ├── helper_functions
    │   ├── __init__.py           # Initialization for helper functions package
    │   ├── pca.py                # PCA plot functionality
    │   ├── scatterplot.py        # Scatter plot with smooth line functionality
    │   └── volcano_plot.py       # Volcano plot functionality
    └── Home.py                   # Main Streamlit app entry point
```

### Files Description

#### 1. `/helper_functions/__init__.py`
This file initializes the `helper_functions` module, which contains all the data visualization tools.

#### 2. `/helper_functions/pca.py`
This module provides a function to generate a Principal Component Analysis (PCA) plot from a given CSV file.

- **Function:** `pca_plot(dataframe: pd.DataFrame, n_components: int = 2)`
  - **Input:** Pandas DataFrame with numerical data, number of principal components to calculate.
  - **Output:** PCA scatter plot showing the first two principal components.
  
#### 3. `/helper_functions/scatterplot.py`
This module provides a function to generate a scatter plot with smooth lines using LOWESS smoothing.

- **Function:** `scatter_with_smooth_lines(dataframe: pd.DataFrame, x_col: str, y_col: str, frac: float = 0.3)`
  - **Input:** Pandas DataFrame, column names for x and y axes, and the smoothing fraction for LOWESS.
  - **Output:** Scatter plot with a smooth line fitted to the data.

#### 4. `/helper_functions/volcano_plot.py`
This module provides a function to generate a volcano plot, a common visualization in bioinformatics.

- **Function:** `volcano_plot(dataframe: pd.DataFrame, fold_change_col: str, p_value_col: str, threshold_fc: float = 1.0, threshold_pval: float = 0.05)`
  - **Input:** Pandas DataFrame with fold change and p-value columns, thresholds for fold change and p-value.
  - **Output:** Volcano plot highlighting upregulated and downregulated genes or proteins.

#### 5. `/Home.py`
This is the main entry point for the Streamlit app. It integrates the helper functions from the `helper_functions` module to create an interactive web-based application.

- **Usage:** Users can upload CSV files for visualizing data through PCA plots, scatter plots, or volcano plots. The app automatically generates the corresponding plot after the file upload and required inputs.

## Setup Instructions

### 1. Install the required dependencies:
You can use `conda` to create an isolated environment for this project.

1. **Create a new conda environment:**

   ```bash
   conda env create -f environment.yaml
   ```

2. **Activate the environment:**

   ```bash
   conda activate data_visualisation
   ```

### 2. Run the Streamlit App:
   To launch the app, navigate to the project directory and run:

   ```bash
   streamlit run Home.py
   ```

### 3. Upload your data:
   - PCA Plot: Upload a CSV, txt or xls file containing numerical data.
   - Scatter Plot: Upload a CSV, txt or xls file and specify the columns for x and y axes.
   - Volcano Plot: Upload a CSV, txt or xls file and specify columns for fold change and p-values.

### 4. Explore your plots:
   Once the file is uploaded, you can interact with the plots and visualize your data in various ways.

## Contributing
Contributions are welcome! If you have any suggestions or would like to add new visualizations, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License.

---

Enjoy exploring your data with this easy-to-use visualization app!
