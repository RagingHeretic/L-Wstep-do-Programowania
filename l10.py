# Hubert Jackowski
import openpyxl as xl, pathlib, xlsxwriter as xlw
from openpyxl.styles import Font
# Zadanie 1
wb = xl.load_workbook(filename=pathlib.Path.cwd() / "pliki_xlsx" / "skoroszyt_produkty.xlsx")
wb.create_sheet("analiza")
for row in wb.worksheets[0]:
    for cell in row:
        wb.worksheets[1][cell.coordinate].value = cell.value
for cell in wb.worksheets[0][1]:
    wb.worksheets[1][cell.coordinate].font = Font(bold=True, size=12)
wb.save(filename=pathlib.Path.cwd() / "pliki_xlsx" / "zakupione_produkty.xlsx")

print(wb.worksheets())
# .write_formula("E12", "=AVG(E2:E10)")
# with open(pathlib.Path.cwd() / "obrazy" / "obraz.jpg", "rb") as image:
#     temp = image.read()
#     wb.worksheets[1]["I13"].value = temp