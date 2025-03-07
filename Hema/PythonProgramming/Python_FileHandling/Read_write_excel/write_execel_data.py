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

#write_excel_file("test_data.xlsx", "Sheet1", "A1", "Bangalore")
#write_excel_file("test_data.xlsx", "Kartik", "A1", "Bangalore")

# This function will create new excel sheet with default Sheet, and add value to first cell.
def create_excel_file(file_path, sheet_name, cell_name, new_value):
    wb = openpyxl.Workbook()
    sheet = wb[sheet_name]
    cell = sheet[cell_name]
    cell.value = new_value
    wb.save(file_path)


create_excel_file("new_excel2.xlsx", "Sheet", "A1", "India")
