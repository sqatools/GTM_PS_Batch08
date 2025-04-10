"""

Command to install library:
--> pip install openpyxl

Command to check list of installed Python packages:
--> pip list

"""

import openpyxl

# This function will update current value of a cell with new value
def write_excel_file(filepath, sheet_name, cell_name, new_value):
    wb = openpyxl.load_workbook(filepath)
    sheet = wb[sheet_name]
    cell = sheet[cell_name]
    cell.value = new_value
    wb.save(filepath)

write_excel_file()