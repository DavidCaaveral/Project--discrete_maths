import os
from colorama import init, Fore, Back, Style
import inquirer
#submenus logicgates
def clearTerm() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

init()



optionssubMenu = [
    inquirer.List(
        "submenu",
        message="Seleccione una opcion",
        choices=[
            "1. compuerta AND",
            "2. compuerta OR",
            "3. compuerta NOT",
            "4. compuerta XOR",
            "5. compuerta NAND",
            "6. compuerta NOR",
            "7. compuerta XNOR",
            "8. compuerta IF",
            "9. Volver al menú principal",
            "0. limpiar terminal"
        ]
    )
]

print(f"\n{Fore.YELLOW}{"="*12}{Style.RESET_ALL}{Fore.MAGENTA} > COMPUERTAS LÓGICAS < {Style.RESET_ALL}{Fore.YELLOW}{"="*12}{Style.RESET_ALL}\n")
answersubMenu = inquirer.prompt(optionssubMenu) 
print(answersubMenu["submenu"])
print(f"="*66+'\n')

if answersubMenu["submenu"] == "1. compuerta AND":
        print ("\n----------------------------COMPUERTA AND----------------------------\n")
elif answersubMenu["submenu"] == "2. compuerta OR":
        print ("\n----------------------------COMPUERTA OR----------------------------\n")
elif answersubMenu["submenu"] == "3. compuerta NOT":
        print ("\n----------------------------COMPUERTA NOT----------------------------\n")
elif answersubMenu["submenu"] == "4. compuerta XOR":
        print ("\n----------------------------COMPUERTA XOR----------------------------\n")
elif answersubMenu["submenu"] == "5. compuerta NAND":
        print ("\n----------------------------COMPUERTA NAND----------------------------\n")
elif answersubMenu["submenu"] == "6. compuerta NOR":
        print ("\n----------------------------COMPUERTA NOR----------------------------\n")
elif answersubMenu["submenu"] == "7. compuerta XNOR":
    print ("\n----------------------------COMPUERTA XNOR----------------------------\n")
elif answersubMenu["submenu"] == "8. compuerta IF":
    print ("\n----------------------------COMPUERTA IF----------------------------\n")
elif answersubMenu["submenu"] == "9. Volver al menú principal":
    print ("\n Volviendo al menú principal...\n")
elif answersubMenu["submenu"] == "0. limpiar terminal":
    print ("\n Limpiando terminal...\n")
    clearTerm()
else:
    print("\n Esa opción digitada no esta definida en el submenu de compuertas lógicas\n") 
