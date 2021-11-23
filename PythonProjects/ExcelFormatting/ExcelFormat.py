import os,glob,xlsxwriter # os and glob to read files in directory, xlsxwriter for writing to excel

workbook = xlsxwriter.Workbook('data.xlsx') #creating blank excel file
worksheet = workbook.add_worksheet()

#using row and column variables
row = 1
col = 0

#creating formatting to make titles bold
cell_bold =  workbook.add_format()
cell_bold.set_bold()

#getting current directory and adding/sorting all txt files to list
folder = os.getcwd()
filename = sorted([os.path.basename(f) for f in glob.glob(os.path.join(folder,'*.txt'))])

#iterating over the list to create titles in bold in excel
for string in filename:
    string = string[:-4]
    worksheet.write(row, col, string, cell_bold)
    row = row + 2

#creating a list of stats
table_list = ['Threads', 'Average', 'StDev','Max', ' ', 'Total Data', 'Total Req', 'Req/Sec', 'Transfer/Sec']
row_1 = 1
col_1 = 1

#iterating over stats to create data titles
for title in table_list:
    worksheet.write(row_1, col_1, title) 
    col_1 = col_1 + 1 

workbook.close()
