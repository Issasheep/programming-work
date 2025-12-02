import json 


with open ("setup.json", "r") as f:
    setup = json.load(f)
x = setup([0])

print (x)


