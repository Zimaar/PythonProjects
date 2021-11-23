import csv

with open('TCBM1-req-per-sec-1st.txt', 'r') as in_file, open('1.csv', 'w') as out_file:
    reader = csv.reader(in_file, delimiter=" ").rstrip() 
    writer = csv.writer(out_file, lineterminator='\n')
    writer.writerows(reader)






