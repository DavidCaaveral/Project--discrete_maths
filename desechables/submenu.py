import os
from colorama import init, Fore, Back, Style
import inquirer

init()
def clearTerm() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
# Limpiar teminal 
#lector compuerta logica 
#circuito logico, integrado al menu principal.
userOption=-1 
onSubMenuGates = True

while onSubMenuGates:

    print(f"\n{Fore.YELLOW}{"="*12}{Style.RESET_ALL}{Fore.MAGENTA} > COMPUERTAS LÓGICAS < {Style.RESET_ALL}{Fore.YELLOW}{"="*12}{Style.RESET_ALL}\n")
    print("En este submenu podrá elegir entre las siguientes compuertas lógicas para evaluar su funcionamiento con las variables booleanas ingresadas en el menú principal\n")
    print ("1. compuerta AND")
    print ("2. compuerta OR")
    print ("3. compuerta NOT")
    print ("4. compuerta XOR")
    print ("5. compuerta NAND")
    print ("6. compuerta NOR")
    print ("7. compuerta XNOR")
    print ("8. compuerta IF")
    print ("9. Volver al menú principal")
    print ("0. limpiar terminal\n")

    userOption = int(input("Ingrese una opcion: "))
    if userOption == 1: 
        print (f"\n{Fore.YELLOW}{"="*12}{Style.RESET_ALL}{Fore.GREEN} COMPUERTA AND {Fore.YELLOW}{"="*12}{Style.RESET_ALL}\n")
    elif userOption == 2:
        print (f"\n{Fore.YELLOW}{"="*12}{Style.RESET_ALL}{Fore.GREEN} COMPUERTA OR {Fore.YELLOW}{"="*12}{Style.RESET_ALL}\n")
    elif userOption == 3:
        print (f"\n{Fore.YELLOW}{"="*12}{Style.RESET_ALL}{Fore.GREEN} COMPUERTA NOT {Fore.YELLOW}{"="*12}{Style.RESET_ALL}\n")
    elif userOption == 4:
        print (f"\n{Fore.YELLOW}{"="*12}{Style.RESET_ALL}{Fore.GREEN} COMPUERTA XOR {Fore.YELLOW}{"="*12}{Style.RESET_ALL}\n")
    elif userOption == 5:
        print (f"\n{Fore.YELLOW}{"="*12}{Style.RESET_ALL}{Fore.GREEN} COMPUERTA NAND {Fore.YELLOW}{"="*12}{Style.RESET_ALL}\n")
    elif userOption == 6:
        print (f"\n{Fore.YELLOW}{"="*12}{Style.RESET_ALL}{Fore.GREEN} COMPUERTA NOR {Fore.YELLOW}{"="*12}{Style.RESET_ALL}\n")
    elif userOption == 7:
        print (f"\n{Fore.YELLOW}{"="*12}{Style.RESET_ALL}{Fore.GREEN} COMPUERTA XNOR {Fore.YELLOW}{"="*12}{Style.RESET_ALL}\n")
    elif userOption == 8:
        print (f"\n{Fore.YELLOW}{"="*12}{Style.RESET_ALL}{Fore.GREEN} COMPUERTA IF{Fore.YELLOW}{"="*12}{Style.RESET_ALL}\n")
    elif userOption == 9:
        print ("\n Volviendo al menú principal...\n")
        onSubMenuGates = True
    elif userOption == 0:
        print ("\n Limpiando terminal...\n")
        clearTerm()
    else:
        print("\n Esa opción digitada no esta definida en el submenu de compuertas lógicas\n") 

    break
