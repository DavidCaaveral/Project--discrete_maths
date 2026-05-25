import os
import time
#submenus logicgates
def clearTerm() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
# Limpiar teminal 
#lector compuerta logica 
#circuito logico, integrado al menu principal.
userOption=-1 
onSubMenuGates = True

while onSubMenuGates:

    print("\n----------------------------SUBMENU DE COMPUERTAS LÓGICAS----------------------------\n")
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
        print ("\n----------------------------COMPUERTA AND----------------------------\n")
        onSubMenuGates = False      
    elif userOption == 2:
        print ("\n----------------------------COMPUERTA OR----------------------------\n")
        onSubMenuGates = False
    elif userOption == 3:
        print ("\n----------------------------COMPUERTA NOT----------------------------\n")
        onSubMenuGates = False
    elif userOption == 4:
        print ("\n----------------------------COMPUERTA XOR----------------------------\n")
        onSubMenuGates = False
    elif userOption == 5:
        print ("\n----------------------------COMPUERTA NAND----------------------------\n")
        onSubMenuGates = False
    elif userOption == 6:
        print ("\n----------------------------COMPUERTA NOR----------------------------\n")
        onSubMenuGates = False
    elif userOption == 7:
        print ("\n----------------------------COMPUERTA XNOR----------------------------\n")
        onSubMenuGates = False
    elif userOption == 8:
        print ("\n----------------------------COMPUERTA IF----------------------------\n")
        onSubMenuGates = False
    elif userOption == 9:
        print ("\nVolviendo al menú principal...\n")
        onSubMenuGates = True
    elif userOption == 0:
        clearTerm()
        print ("\nLimpiando terminal...\n")
        time.sleep(1)
        clearTerm()
    else:
        print("\nEsa opción digitada no esta definida en el submenu de compuertas lógicas\n")

