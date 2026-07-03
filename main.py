from utils import separator, clear, navegationIntputMenu, neutralMessageInput
from utils import mainMenu, browseMenu, manageMenu, editMenu, creatmenu, settingsMenu
from storage import createFile, readFile, writeInFile
import os
storage = "data/storage.json"
configs = "data/config.json"

def main():
    while True:
        option = navegationIntputMenu("WELCOME TO THE STUDENTS REGIST PROGRAM",mainMenu,len(mainMenu))
        match option:
            case 1:
                while True:
                    createFile(storage,{})
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
                    createFile(storage,{})
                    data  = readFile(storage)
                    if data == {}:
                        input("There is no data to edit\nPress Enter..")
                        break
                    option  = navegationIntputMenu("MANAGE MENU", manageMenu ,len(manageMenu))
                    if option == 1:
                        option = navegationIntputMenu("EDIT MENU", editMenu, len(editMenu))
                    if option == 2:
                        option = navegationIntputMenu("CREATE MENU", creatmenu, len(creatmenu))
                        match option:
                            case 1:
                                nameGarde = neutralMessageInput("Enter the Grade name:\n", True, True)
                                data[nameGarde] = {}
                                writeInFile(storage, data)
                                break
                            case 2:
                                while True:
                                    if data == {}:
                                        print("There are no grades where create an group")
                                    for grade in data:
                                        neutralMessageInput(grade, False, False)
                                    posibleGrade = neutralMessageInput("Where should the group be created?", True, False)
                                    if posibleGrade in data:
                                        setgrade = posibleGrade
                                        nameGroup = neutralMessageInput("Enter the Group name:\n", True,True)    
                                        data[setgrade][nameGroup] = {}
                                        writeInFile(storage, data)
                                        break
                                    else:
                                        input("That grade doesnt exist")
                                        continue
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