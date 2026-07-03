import json,os

def createFile(direction, content):
    if not os.path.exists(direction):
        with open(direction, "w") as file:
            json.dump(content, file, indent=4)
    input("A new storage file had been created...\nPress Enter...")
def readFile(direction):
    with open(direction, "r") as file:
        data = json.load(file)
    return data
def writeInFile(direction, data):
    with open(direction, "w", encoding="UTF-8") as file:
        json.dump(data,file, ensure_ascii=False, indent=4)

