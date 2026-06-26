import json
def createFile(direction, content):
    with open(direction, "w") as file:
        json.dump(content, file, indent=4)
        
def readFile(direction):
    with open(direction, "r") as file:
        data = json.load(file)
    return data
