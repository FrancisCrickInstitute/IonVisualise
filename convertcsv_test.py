"""Module providing a function to exit early"""
 
import sys
import shutil
from Home import convert_csv
 
test_filename_list = [
    "mock_data/mock_proteomics_data.csv",
    "mock_data/mock_proteomics_data.txt",
]
 
test_file_list = []
for filename in test_filename_list:
    shutil.copyfile(filename, filename.split("/")[-1])
    file = open(filename.split("/")[-1], "r", encoding="utf-8")
    test_file_list.append(file)
 
print("::debug::Testing convert_csv")
 
test_filename_converted_list = convert_csv(test_file_list)
 
print("::notice::Success convert_csv")
 
for file in test_file_list:
    file.close()
 
original_file = open(test_filename_list[0], "r", encoding="utf-8")
original_file_content = original_file.read()
original_file.close()
 
print("::debug::Checking convert_csv output was correct")
 
for filename in test_filename_converted_list:
    file = open(filename, "r", encoding="utf-8")
    file_content = file.read()
 
    if file_content != original_file_content:
        print("::error::Success convert_csv output was incorrect")
        sys.exit(1)
 
    file.close()
 
print("::notice::Success convert_csv output was correct")
 
sys.exit(0)
 
 