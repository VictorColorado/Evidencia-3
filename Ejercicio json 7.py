import json

fileObject = open("traduccion.json", "r")
jsonContent = fileObject.read()
aList = json.loads(jsonContent)
print(aList)
print(aList['a'])
print(aList['b'])
print(aList['c'])