from utils import separator, clear, navegationIntputMenu
from utils import mainMenu, browseMenu, manageMenu, editMenu, creatmenu, settingsMenu
from storage import createFile, readFile
import os
storage = "data/storage.json"
configs = "data/config.json"

def main():
    while True:
        option = navegationIntputMenu("WELCOME TO THE STUDENTS REGIST PROGRAM",mainMenu,len(mainMenu))
        match option:
            case 1:
                while True:
                    if not os.path.exists("data/storage.json"):
                        createFile(storage,{})
                        input("There is no data registred\nPress Enter...")
                        break
                    data = readFile(storage)
                    if not data:
                        input("There is no data registred\nPress Enter...")
                        break
                    option = navegationIntputMenu("BROWSE MENU", browseMenu, len(browseMenu))
                    match option:
                        case 4:
                            break
            case 2:
                while True:
                    option  = navegationIntputMenu("MANAGE MENU", manageMenu ,len(manageMenu))
                    if option == 1:
                        option = navegationIntputMenu("EDIT MENU", editMenu, len(editMenu))
                    if option == 2:
                        option == navegationIntputMenu("CREATE MENU", creatmenu, len(creatmenu))
                    else:
                        break
            case 3:
                while True:
                    option = navegationIntputMenu("SETTING MENU", settingsMenu,len(settingsMenu))
            case 4:
                clear()
                separator("=")
                print("SEE YOU LATTER")                
                separator("=")
                break


if __name__ == "__main__":
    main()