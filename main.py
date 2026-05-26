# 1. Importaciones de librerías
import os
import time
from colorama import init, Fore, Back, Style
from librerias.compuertas import *
from librerias.interfaces import *

# 2. Definición de constantes globales
statementObj = { # Inicialización de keys de objeto
    'A': -1,
    'B': -1,
    'C': -1,
    'D': -1
}

# 3. Definición de funciones

def clearTerm() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

# 4. Definición de clases (opcional)

# 5. Bloque principal de ejecución
def main():
    while True:
        electedOption = mainMenu()["menu"]
        match electedOption:
            
            case "var-bool":
                print(f"="*66+'\n')
                print(f"\n{"="*8}> {Fore.CYAN} Ingreso de variables booleanas {Style.RESET_ALL} <{"="*8} \n")
                for key in statementObj:
                    questionBool = [
                        inquirer.List(
                            "value",
                            message=f"Ingrese valor para {key}",
                            choices=[0, 1]
                        )
                    ] 

                    answerObj = inquirer.prompt(questionBool)

                    statementObj[key] = answerObj["value"]
                print("Cargando...".center(76))
                time.sleep(2)
                print(f"\nVariables asignadas con exito {" - -"*5} A:{statementObj['A']}, B:{statementObj['B']}, C:{statementObj['C']}, D:{statementObj['D']}\n \n")
                print("Redirigiendo...".center(76), "\n")
                time.sleep(2)
                
            case "submenu1":
                print(f"="*66+'\n')
                print(f"\n{"="*21}> {Fore.CYAN} Compuertas Logicas {Style.RESET_ALL} <{"="*21} \n")
                while True:
                    submenuOption1= subMenu1(statementObj)["submenu"]
                    
                
        

# 6. Punto de entrada
if __name__ == "__main__":
    main()
    
