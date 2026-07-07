from storage import readFile, writeInFile
import os
storage = "data/storage.json"
configs = "data/config.json"

mainMenu = ["Browse data","Manage data","Settings","Exit"]
browseMenu = ["Browse by Grade", "Browse by Group", "Serch Student","Exit"]
settingsMenu = ["Config Setts", "Exit"]
manageMenu = ["Edit","Create","Exit"]
editMenu = ["Manage Grade", "Manage Group", "Edit Student","Exit"]
creatmenu = ["Create Grade", "Create Group", "Regist Student", "Exit"]
setcConfigsMenu =["Default", "Create new ones"]

def navegationIntputMenu(message, content, max):
    while True:
        clear()
        separator("=")
        print(message)
        separator("=")
        for index, option in enumerate(content, start=1):
            print(f"{index}: {option}")
        separator("-")
        try:
            data = int(input("Choose an option: "))
            if 1 <= data <= max:
                return data
            input(f"Please enter a value between 1 and {max}\nPress Enter...")
        except ValueError:
            input("Please enter an numeric value\nPress Enter..")
            continue

def neutralMessageInput(message,clearQ,type):
    if clearQ == True:
        clear()
    separator("-")
    if type == "str":
        data = input(message)
        while not data.strip():
            data = input(f"Please entar a value\n{message}")
        return data
    elif type == "int":
        while True:
            data = input(message)
            try:
                intaData = int(data)
                return intaData
            except(ValueError):
                clear()
                print("Enter a numeric value")
    elif type == "none":
        print(message)
    else:
        print(message)

def createSetting():
    configData = readFile(storage)
    configName = neutralMessageInput("Enter the config sett name:\n", True, "str")
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
    writeInFile(storage, configData)
    return configName

def separator(symbol):
    print(symbol*50)
def clear():
    os.system("clear")