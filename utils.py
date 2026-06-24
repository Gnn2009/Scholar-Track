import os

mainmenu = ["Brose data","Manage data","Settings","Exit"]

def mainMenuPrint():
    separator("=")
    print("WELCOME TO THE STUDENTS REGIST PROGRAM")
    separator("=")
    for index, option in enumerate(mainmenu, start=1):
        print(f"{index}: {option}")

def navegationIntputMenu(prevfunction,max):
    while True:
        clear()
        prevfunction()
        separator("-")
        try:
            data = int(input("Choose an option: "))
            if 1 < data < max:
                return data
            input(f"Please enter a value between 1 and {max}\nPress Enter...")
        except ValueError:
            input("Please enter an numeric value\nPress Enter..")
            continue

def separator(symbol):
    print(symbol*50)
def clear():
    os.system("clear")