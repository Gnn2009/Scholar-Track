import json,os, re
import config
from utils import clear, neutralMessageInput,configs, storage, navegationIntputMenu, verifyExistentData
from utils import selectConfigMeun

def createFile(direction, content):
    if not os.path.exists(direction):
        with open(direction, "w") as file:
            json.dump(content, file, indent=4)
            clear()
            input("A new storage file had been created...\nPress Enter...")
def readFile(direction):
    with open(direction, "r") as file:
        data = json.load(file)
    return data
def writeInFile(direction, data):
    with open(direction, "w", encoding="UTF-8") as file:
        json_text = json.dumps(data, ensure_ascii=False, indent=4)
        clean_json = re.sub(
            r'\[\s*(.*?)\s*\]', 
            lambda match: '[' + re.sub(r'\s+', ' ', match.group(1)).strip() + ']', 
            json_text, 
            flags=re.DOTALL
        )
        
        file.write(clean_json)

def createGroup(storageData, existSettings):
    configData = readFile(configs)
    confname ="DEF_CONFIG"
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

def createStudent():
    storageData = readFile(storage)
    configsData = readFile(configs)
    for grade in storageData:
        neutralMessageInput(grade, False, "none")
    selectedGrade = verifyExistentData(storageData)
    for group in storageData[selectedGrade]:
        neutralMessageInput(group, False, "none")
    selectedGroup = verifyExistentData(storageData[selectedGrade])
    selectedConfig = configsData[storageData[selectedGrade][selectedGroup]["config"]]
    while True:
        notes = {}
        name = neutralMessageInput("Enter the students name:\n",True, "str")
        for subject in selectedConfig["subjects"]:
            notes[subject]=[]
            for j in range(1,selectedConfig["notes_per_subject"] + 1):
                note = neutralMessageInput(f"Enter the {subject} #{j} note:\n", True, "int")
                notes[subject].append(note)
        storageData[selectedGrade][selectedGroup] = {
            "name": name,
            "notes": notes
        }
        writeInFile(storage, storageData)
        if neutralMessageInput("Press 'q' to quit\nPress enter to regist another one", True, "str") == "q":
            break