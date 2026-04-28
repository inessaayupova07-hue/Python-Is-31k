import csv

rows=[['Name','Age'],['Alice',25],['Bob',30]]
with open('users.csv','w',newline='') as f:
    writer=csv.writer(f)
    writer.writerows(rows)