import sys
import shutil
from Home import load_data
from helper_functions.scatterplot import scatter_with_smooth_lines
 
test_filename_list = [
    "mock_data/mock_proteomics_data.csv",
]
 
for filename in test_filename_list:
    data_frame = load_data(filename)
    x_axis = "Fold_Change"
    y_axis = "Peptide_Count"
    scatter_with_smooth_lines(data_frame, x_axis, y_axis)
 
sys.exit(0)
 
 