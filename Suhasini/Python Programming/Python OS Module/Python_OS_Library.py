import os

#Get current working directory path:
print(os.getcwd())

# /Users/suhasini/Documents/PythonFiles/.venv/bin/python /Users/suhasini/Documents/PythonFiles/GTM_PS_Batch08/Suhasini/Python Programming/Python OS Module/Python_OS_Library.py
# /Users/suhasini/Documents/PythonFiles/GTM_PS_Batch08/Suhasini/Python Programming/Python OS Module

# Change working directory path:
# os.chdir()     # Doubt

# It will create new file in new path we have set.
"""
with open("test_data.txt", "w") as file:
    file.write("Good Morning")
"""

# create new folder
"""
os.mkdir("GTM_Batch08")
os.chdir(r"E:\Trainings\GTM_PS_Batch08_6Jan25\GTM_PS_Batch08\Deepesh\PythonProgramming\Python_OS_module")
os.mkdir("GTM_Batch08")
"""

# Remove Directory

