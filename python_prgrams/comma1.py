import xlrd
import csv
with open ("ann.xlsx", "r") as mak:
    output = []
    for col in mak:
        output.append(col.strip())
    print ','.join(output)
