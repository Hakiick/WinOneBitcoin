import pandas as pd
from openpyxl import load_workbook
# new dataframe with same columns
df = pd.DataFrame({'TimeStamp': ['E','F','G','H'],
                   'Age': [99,70,40,60]})
writer = pd.ExcelWriter('demo.xlsx', engine='openpyxl', mode='a', if_sheet_exists='overlay')
# try to open an existing workbook
writer.book = load_workbook('demo.xlsx')
# copy existing sheets
writer.sheets = dict((ws.title, ws) for ws in writer.book.worksheets)
# read existing file
reader = pd.read_excel(r'demo.xlsx')
# write out the new sheet
df.to_excel(writer,index=False,header=False,startrow=len(reader)+1)

writer.close()