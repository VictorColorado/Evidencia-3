import csv

results = []
with open ('example4.csv') as File:
    reader = csv.DictReader(File)
    for row in reader:
        results.append(row)
    print (results)