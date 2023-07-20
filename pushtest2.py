import  pandas  as pd
import os
#data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
def append_data_to_excel(excel_name, sheet_name, data):
    with pd.ExcelWriter(excel_name) as writer:
        columns = []
        for k, v in data.items():
            columns.append(k)
        df = pd.DataFrame(data, index= None)
        df_source = None
        if os.path.exists(excel_name):
            df_source = pd.DataFrame(pd.read_excel(excel_name, sheet_name=sheet_name))
        if df_source is not None:
            df_dest = df_source.append(df)
        else:
            df_dest = df
        df_dest.to_excel(writer, sheet_name=sheet_name, index = False, columns=columns)
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42],'City':['wuhan','chongqin','beijing','shanghai']}
append_data_to_excel('test.xlsx', 'person',data)
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[29,34,29,42]}
append_data_to_excel('test.xlsx', 'person',data)
append_data_to_excel('test.xlsx', 'person',data)