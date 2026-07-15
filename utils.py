import os
storage = "data/storage.json"
configs = "data/config.json"

mainMenu = ["Manage data","Reports","Exit"]
creatmenu = ["Create Grade", "Create Group", "Regist Student", "Exit"]
setConfigsMenu =["Default", "Create new ones"]
selectConfigMeun = ["Create", "Select", "Default"]


def navegationIntputMenu(message, content):
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
            if 1 <= data <= len(content):
                return data
            input(f"Please enter a value between 1 and {len(content)}\nPress Enter...")
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

def separator(symbol):
    print(symbol*50)
def clear():
    os.system("clear")

def verifyExistentData(file):
    while True:
        var = neutralMessageInput("Chose one grade:\n", False, "str")
        if var in file:
            return var