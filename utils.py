import os

mainMenu = ["Browse data","Manage data","Settings","Exit"]
browseMenu = ["Browse by Grade", "Browse by Group", "Serch Student","Exit"]
settingsMenu = ["Config Setts", "Exit"]
manageMenu = ["Edit","Create","Exit"]
editMenu = ["Manage Grade", "Manage Group", "Edit Student","Exit"]
creatmenu = ["Create Grade", "Create Group", "Regist Student", "Exit"]



def menuPrint(message, content):
    separator("=")
    print(message)
    separator("=")
    for index, option in enumerate(content, start=1):
        print(f"{index}: {option}")

def navegationIntputMenu(message, content, max):
    while True:
        clear()
        menuPrint(message, content)
        separator("-")
        try:
            data = int(input("Choose an option: "))
            if 1 <= data <= max:
                return data
            input(f"Please enter a value between 1 and {max}\nPress Enter...")
        except ValueError:
            input("Please enter an numeric value\nPress Enter..")
            continue

def separator(symbol):
    print(symbol*50)
def clear():
    os.system("clear")