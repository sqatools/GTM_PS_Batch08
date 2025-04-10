"""
command to install library
 -> pip install openpyxl
# command to check list of installed python packages
 -> pip list

"""
import openpyxl

# This function will update existing file cell with new value.
def write_excel_file(file_path, sheet_name, cell_name, new_value):
    wb = openpyxl.load_workbook(file_path)
    sheet = wb[sheet_name]
    cell = sheet[cell_name]
    cell.value = new_value
    wb.save(file_path)

write_excel_file("file_example_XLS_10.xlsx", "Sheet1", "A1", "City")