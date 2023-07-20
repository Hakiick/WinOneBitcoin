import pandas as pd
from openpyxl import load_workbook
reader = pd.read_excel(r'demo.xlsx')
print(reader)