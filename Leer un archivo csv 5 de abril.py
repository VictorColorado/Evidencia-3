import csv

with open('example4.csv') as File:
    reader = csv.reader(File,delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        print(row)