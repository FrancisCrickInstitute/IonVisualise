import sys
import shutil
from Home import load_data
from helper_functions.pca import pca_plot
 
test_filename_list = [
    "mock_data/mock_proteomics_data_time.csv",
]
 
for filename in test_filename_list:
    data_frame = load_data(filename)
    pca_plot(data_frame)
 
sys.exit(0)