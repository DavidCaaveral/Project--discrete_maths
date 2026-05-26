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
    print ("9. Volver al menú principal\n")
    print ("0. limpiar terminal\n")

    userOption = int(input("Ingrese una opcion: "))
    if userOption == 1: 
        print ("\n----------------------------COMPUERTA AND----------------------------\n")
    elif userOption == 2:
        print ("\n----------------------------COMPUERTA OR----------------------------\n")
    elif userOption == 3:
        print ("\n----------------------------COMPUERTA NOT----------------------------\n")
    elif userOption == 4:
        print ("\n----------------------------COMPUERTA XOR----------------------------\n")
    elif userOption == 5:
        print ("\n----------------------------COMPUERTA NAND----------------------------\n")
    elif userOption == 6:
        print ("\n----------------------------COMPUERTA NOR----------------------------\n")
    elif userOption == 7:
        print ("\n----------------------------COMPUERTA XNOR----------------------------\n")
    elif userOption == 8:
        print ("\n----------------------------COMPUERTA IF----------------------------\n")
    elif userOption == 9:
        print ("\nVolviendo al menú principal...\n")
        onSubMenuGates = True
    elif userOption == 0:
        print ("\nLimpiando terminal...\n")
        clearTerm()
    else:
        print("\nEsa opción digitada no esta definida en el submenu de compuertas lógicas\n") 