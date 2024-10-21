
# IonVisualise

Welcome to the **IonVisualise**! This app is designed to help you visualize and analyze data from various sources, including PCA plots, scatter plots, volcano plots, and time series. The app provides a simple interface for uploading data files and generating intuitive and interactive visualizations.

## Features

- **PCA (Principal Component Analysis) Plot:** Visualize data using PCA, helping you understand variance and relationships in high-dimensional datasets.
- **Scatter Plot with Smooth Lines:** Generate scatter plots with LOWESS smoothing lines to capture trends in your data.
- **Volcano Plot:** Perform differential expression analysis with volcano plots, marking significant data points.
- **Time Series Plot:** Track changes in data over time with interactive time series plots.
- **Team Introduction Page:** Meet the team behind the app on the "Meet the Team" page.

## Project Directory Structure

```plaintext
./
├── helper_functions
│   ├── __init__.py              # Helper functions initializer
│   ├── file_operations.py       # File operation functions (e.g., removing old files)
│   ├── pca.py                   # PCA plot generation functions
│   ├── scatterplot.py           # Scatter plot generation functions
│   ├── timeseries.py            # Time series plot generation functions
│   └── volcano_plot.py          # Volcano plot generation functions
├── pages
│   └── Meet_The_Team.py         # Introduction of the team
├── environment.yaml             # Conda environment configuration
└── Home.py                      # Main script to run the app
```

## Installation Instructions

This app runs in a Conda environment. Follow the steps below to set it up on your local machine.

### 1. Install Anaconda (if you don't have it already)

Download and install Anaconda from [https://www.anaconda.com/products/individual](https://www.anaconda.com/products/individual).

### 2. Clone the Repository

```bash
git clone git@github.com:IonVisualisation/IonVisualise.git
cd IonVisualise
```

### 3. Create the Conda Environment

To set up the environment, use the `environment.yaml` file provided. This will create a Conda environment with all the required dependencies for the app.

```bash
conda env create -f environment.yaml
```

This will create an environment named `data_visualisation` with Python 3.12 and all the necessary packages.

### 4. Activate the Environment

Once the environment is created, activate it using:

```bash
conda activate data_visualisation
```

### 5. Run the App

With the environment activated, you can now run the Streamlit app using the following command:

```bash
streamlit run Home.py
```

The app should open in your web browser. If it doesn't, navigate to `http://localhost:8501` in your browser.

### 6. Usage

- **Upload Data:** Upload `.csv`, `.txt`, or `.xls` files to visualize.
- **Navigate Pages:** Use the navigation buttons at the top of the app to explore different visualizations (PCA, Volcano Plot, Scatter Plot, Time Series).
- **Meet the Team:** Visit the "Meet The Team" page to learn more about the app creators.

## Troubleshooting

- If you encounter an issue with missing packages, make sure the Conda environment is activated (`conda activate data_visualisation`).
- For issues with specific visualizations, ensure the uploaded data files are formatted correctly (e.g., proper column headers for Volcano and PCA plots).

## Contributing

If you'd like to contribute to the project, feel free to submit pull requests or open issues. We welcome all contributions that improve the functionality, design, or performance of the app.

Please ensure all commits follow the [conventional commits standard](https://www.conventionalcommits.org/en/v1.0.0/) and that all pull requests to main pass all tests in the `.github/workflows/test.yml` folder.

## Contacts

For any issues with the repository please contact:
- Eschal Najmi [Github](https://github.com/eschalnajmi) [Email](eschal.najmi@gmail.com)

For any issues with the web application itself please contact:
- Eschal Najmi [Github](https://github.com/eschalnajmi) [Email](eschal.najmi@gmail.com)
- Yew Mun Yip [Github](https://github.com/yipy0005) [Email](yewmun.yip@crick.ac.uk)

For any issues with data visualisation within the web app please contact:
- Yew Mun Yip [Github](https://github.com/yipy0005) [Email](yewmun.yip@crick.ac.uk)
- Georgia Whitton [Github](https://github.com/gwhittonx) [Email](georgia.whitton@crick.ac.uk)
- Sara Patti [Github](https://github.com/spatts14) [Email](sara.patti@crick.ac.uk)
- Spencer Duvwiama [Github](https://github.com/spencerejd) [Linkedin](https://www.linkedin.com/in/spencerduvwiama/)
## License

This project is licensed under the MIT License.

---

Thank you for using the **IonVisualise**! We hope this tool helps streamline your data analysis workflows.
