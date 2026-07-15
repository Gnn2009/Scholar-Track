from utils import separator, clear, navegationIntputMenu, neutralMessageInput, configs, storage
from utils import mainMenu, creatmenu
from storage import createFile, readFile, writeInFile, createGroup, createStudent
from config import DEF_CONFIG

def main():
    while True:
        createFile(storage,{})
        createFile(configs,{})
        storageData  = readFile(storage)      
        writeInFile(configs,DEF_CONFIG)
        option = navegationIntputMenu("WELCOME TO THE STUDENTS REGIST PROGRAM",mainMenu,)
        match option:
            case 1:
                while True:
                    if option == 1:
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
                            case 3:
                                if any(isinstance(contenido, dict) and contenido for contenido in storageData.values()):
                                    createStudent()
                                else:
                                    input("There are no groups where the students can be registred\nPress enter...")
                                    break
                    else:
                        break
            case 2:
                clear()
                separator("=")
                print("SEE YOU LATTER")                
                separator("=")
                break

if __name__ == "__main__":
    main()