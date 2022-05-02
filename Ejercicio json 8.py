import json

jsonStr='[{"a":1, "b":2}, {"c":3,"d":4}]'
aList = json.loads(jsonStr)
print(aList[0]['b'])