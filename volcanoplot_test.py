import sys
import shutil
from Home import load_data
from helper_functions.volcano_plot import volcano_plot
 
test_filename_list = [
    "mock_data/mock_proteomics_data.csv",
]
 
for filename in test_filename_list:
    data_frame = load_data(filename)
    volcano_plot(data_frame, "Fold_Change", "p_value")
 
sys.exit(0)