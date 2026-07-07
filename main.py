from utils import separator, clear, navegationIntputMenu, neutralMessageInput, configs, storage
from utils import mainMenu, browseMenu, manageMenu, editMenu, creatmenu, settingsMenu, setConfigsMenu
from storage import createFile, readFile, writeInFile, createSetting, createGroup
from config import DEF_CONFIG

def main():
    while True:
        createFile(storage,{})
        createFile(configs,{})
        storageData  = readFile(storage)
        option = navegationIntputMenu("WELCOME TO THE STUDENTS REGIST PROGRAM",mainMenu,)
        match option:
            case 1:
                while True:
                    if not storageData:
                        input("There is no data registred\nPress Enter...")
                        break
                    option = navegationIntputMenu("BROWSE MENU", browseMenu,)
                    match option:
                        case 4:
                            break
            case 2:
                while True:
                    option  = navegationIntputMenu("MANAGE MENU", manageMenu)
                    if option == 1:
                        option = navegationIntputMenu("EDIT MENU", editMenu)
                    if option == 2:
                        option = navegationIntputMenu("CREATE MENU", creatmenu,)
                        match option:
                            case 1:
                                nameGarde = neutralMessageInput("Enter the Grade name:\n", True, "str")
                                if nameGarde not in storageData:
                                    storageData[nameGarde] = {}
                                    writeInFile(storage, storageData)
                                break
                            case 2:
                                while True:
                                    if storageData == {}:
                                        createGroup(storageData, False)
                                        break
                                    else:
                                        createGroup(storageData, True)
                                        break
                    else:
                        break
            case 3:
                while True:
                    option = navegationIntputMenu("SETTING MENU", settingsMenu)
            case 4:
                clear()
                separator("=")
                print("SEE YOU LATTER")                
                separator("=")
                break

if __name__ == "__main__":
    main()