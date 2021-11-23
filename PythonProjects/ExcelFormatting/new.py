import os,glob,xlsxwriter
import pandas as pd

df = pd.read_table('TCBM1-req-per-sec-1st.txt')
writer = pd.ExcelWriter('pandas_table.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1', startrow=1, header=False, index=False)

workbook = writer.book
worksheet = writer.sheets['Sheet1']

(max_row, max_col) = df.shape

column_settings = [{'header': column} for column in df.columns]

worksheet.add_table(0,0,max_row,max_col - 1, {'columns': column_settings})

worksheet.set_column(0, max_col - 1, 12)

writer.save()
