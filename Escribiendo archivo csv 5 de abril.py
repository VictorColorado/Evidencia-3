import csv

myData = [["First_Name","Second_Name","Grade"],
          ['Jorge','Manuel','C'],
          ['Victor','Gabriel','B']]
myFile = open('example2.csv','w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(myData)

print("Writing complete")