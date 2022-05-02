import json

aDict = {"a":54, "b":87}
jsonString = json.dumps(aDict)
jsonFile = open("ejercicio.json", "w")
jsonFile.write(jsonString)
jsonFile.close()