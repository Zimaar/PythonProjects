import pandas as pandas
import numpy as numpy

csv_reader = pandas.read_csv('sample_csv.csv', encoding = 'latin1')

excel_writer = pandas.ExcelWriter('converted.xlsx')
csv_reader.to_excel(excel_writer, index = False)

excel_writer.save()
