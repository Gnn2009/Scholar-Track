import json,os
import config
from utils import neutralMessageInput,configs, storage, navegationIntputMenu
from utils import selectConfigMeun

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

def createGroup(storageData, existSettings):
    configData = readFile(configs)
    confname ="DEF"
    for grade in storageData:
        neutralMessageInput(grade, True, "none")
    while True:
        posibleGrade = neutralMessageInput("Where should the group be created?:\n", False, "str")
        if posibleGrade in storageData:
            setgrade = posibleGrade
            nameGroup = neutralMessageInput("Enter the Group name:\n", True,"str")
            break
        else:
            input("That grade doesnt exist")
            continue
    if existSettings == True:
            option = navegationIntputMenu("SETINGS",selectConfigMeun,)
            match option:
                case 1:
                    confname = createSetting()
                case 2:
                    for name in configData:
                        neutralMessageInput(name,False, "none")
                    while True:
                        option = neutralMessageInput("OPTIONS", False, "str")
                        if option in configData:
                            confname = option
                            break
                        else:
                            continue
    else:
        confname = createSetting()
    basicGroup = {
        "config": confname
    }
    storageData[setgrade][nameGroup] = basicGroup
    writeInFile(storage, storageData)

def createSetting():
    configData = readFile(configs)
    while True:
        nameOption = neutralMessageInput("Enter the config sett name:\n", True, "str")
        if not nameOption in configData:
            configName = nameOption
            break
        else:
            continue
    max_note = neutralMessageInput("Enter the max note possible:\n", True, "int")
    min_note = neutralMessageInput("Enter the min note possible:\n", True, "int")
    notes_per_subject = neutralMessageInput("Enter how many notes will be per subject:\n", True, "int")
    subjects =[]
    while True:
        subjectName = input("Enter the name of one subject\nEnter 'f' to finish:\n").lower()
        if subjectName == "f":
            break
        else:
            subjects.append(subjectName)
            continue
    configData[configName] ={
        "max_note": max_note,
        "min_note": min_note,
        "notes_per_subject": notes_per_subject,
        "subjects": subjects
    }
    writeInFile(configs, configData)
    return configName