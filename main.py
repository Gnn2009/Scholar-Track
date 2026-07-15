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
                print("GRADES")
                separator("=")
                storageData = readFile(storage)
                for grade in storageData:
                    print(grade)
                while True:
                    option = neutralMessageInput("Choose one grade:\n", False, "str")
                    if option in storageData:
                        selectedGrade = option
                        break
                for group in storageData[selectedGrade]:
                    print(group)
                while True:
                    option = neutralMessageInput("Choose one group:\n", False, "str")
                    if option in storageData[selectedGrade]:
                        selectedGroup = option
                        break
                bests = {}
                students_in_group = storageData[selectedGrade][selectedGroup]  
                for student, data in students_in_group.items():
                    # Filtramos para procesar solo a los alumnos (diccionarios con la clave 'averages')
                    if isinstance(data, dict) and "averages" in data:
                        for signature, average in data["averages"].items():
                            if signature not in bests:
                                bests[signature] = {
                                    "students": [student],
                                    "average": average
                                }
                            elif average > bests[signature]["average"]: 
                                bests[signature] = {
                                    "students": [student],
                                    "average": average
                                }
                            elif average == bests[signature]["average"]: 
                                if student not in bests[signature]["students"]:
                                    bests[signature]["students"].append(student)
                clear()
                separator("=")
                print(f"MEJORES PROMEDIOS - {selectedGrade} {selectedGroup}")
                separator("=")
                if not bests:
                    print("No hay calificaciones registradas en este grupo.")
                else:
                    for signature, info in bests.items():
                        students_str = ", ".join(info["students"])
                        # Redondeamos al mostrar para que los decimales largos no rompan la vista
                        print(f"📚 {signature}: {students_str} con {round(info['average'], 2)}")
                
                separator("=")
                # 🔥 LA CLAVE: Esta pausa evita que el código vuelva al menú principal de golpe
                input("\nPresiona Enter para volver al menú principal...")
            case 3:
                clear()
                separator("=")
                print("SEE YOU LATTER")
                separator("=")
                break

if __name__ == "__main__":
    main()