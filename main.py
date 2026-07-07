import config
import storage
from utils import separator, clear, navegationIntputMenu, neutralMessageInput, configs, storage
from utils import mainMenu, browseMenu, manageMenu, editMenu, creatmenu, settingsMenu, setcConfigsMenu, createSetting
from storage import createFile, readFile, writeInFile
from config import DEF_CONFIG

def main():
    while True:
        createFile(storage,{})
        createFile(configs,{})
        storageData  = readFile(storage)
        option = navegationIntputMenu("WELCOME TO THE STUDENTS REGIST PROGRAM",mainMenu,len(mainMenu))
        match option:
            case 1:
                while True:
                    if not storageData:
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
                        option = navegationIntputMenu("CREATE MENU", creatmenu, len(creatmenu))
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
                                        input("There are no grades where create an group\nPress Enter...")
                                        break
                                    configData = readFile(configs)
                                    if configData == {}:
                                        option = navegationIntputMenu("SET CONFIG", setcConfigsMenu, len(setcConfigsMenu))
                                        print(option)
                                        if option == 2:
                                            configName =createSetting()
                                        else:
                                            configData["default"] = DEF_CONFIG
                                            writeInFile(configs, configData)
                                            configName = "default"
                                            break
                                        for grade in storageData:
                                            neutralMessageInput(grade, False, "none")
                                        posibleGrade = neutralMessageInput("Where should the group be created?", False, "str")
                                        if posibleGrade in storageData:
                                            setgrade = posibleGrade
                                            nameGroup = neutralMessageInput("Enter the Group name:\n", True,"str")
                                            basicGroup = {
                                                "config": configName
                                            }
                                            storageData[setgrade][nameGroup] = basicGroup
                                            writeInFile(storage, storageData)
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