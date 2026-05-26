import os
from colorama import init, Fore, Back, Style
import inquirer
from ..main import clearTerm

init()
optionssubMenu = [

    inquirer.List(
        "submenu",
        message="Seleccione una opcion",
        choices=[
            ("COMPUERTA AND", "AND"),
            ("COMPUERTA OR", "OR"),
            ("COMPUERTA NOT", "NOT"),
            ("COMPUERTA XOR", "XOR"),
            ("COMPUERTA NAND", "NAND"),
            ("COMPUERTA NOR", "NOR"),
            ("COMPUERTA XNOR", "XNOR"),
            ("COMPUERTA IF", "IF"),
            ("VOLVER AL MENÚ PRINCIPAL", "SALIR"),
            ("LIMPIAR TERMINAL", "LIMPIAR"),
        ]
    )
]

answersubMenu = inquirer.prompt(optionssubMenu) 
print(f"\n{Fore.YELLOW}{"="*12}{Style.RESET_ALL}{Fore.MAGENTA} > COMPUERTAS LÓGICAS < {Style.RESET_ALL}{Fore.YELLOW}{"="*12}{Style.RESET_ALL}\n")
print(answersubMenu["submenu"])
print(f"="*66+'\n')

if answersubMenu["submenu"] == "1. COMPUERTA AND":
        print ("\n----------------------------COMPUERTA AND----------------------------\n")
elif answersubMenu["submenu"] == "2. COMPUERTA OR":
        print ("\n----------------------------COMPUERTA OR----------------------------\n")
elif answersubMenu["submenu"] == "3. COMPUERTA  NOT":
        print ("\n----------------------------COMPUERTA NOT----------------------------\n")
elif answersubMenu["submenu"] == "4. COMPUERTA XOR":
        print ("\n----------------------------COMPUERTA XOR----------------------------\n")
elif answersubMenu["submenu"] == "5. COMPUERTA NAND":
        print ("\n----------------------------COMPUERTA NAND----------------------------\n")
elif answersubMenu["submenu"] == "6. COMPUERTA NOR":
        print ("\n----------------------------COMPUERTA NOR----------------------------\n")
elif answersubMenu["submenu"] == "7. COMPUERTA XNOR":
    print ("\n----------------------------COMPUERTA XNOR----------------------------\n")
elif answersubMenu["submenu"] == "8. COMPUERTA IF":
    print ("\n----------------------------COMPUERTA IF----------------------------\n")
elif answersubMenu["submenu"] == "9. VOLVER AL MENÚ PRINCIPAL":
    print ("\n Volviendo al menú principal...\n")
elif answersubMenu["submenu"] == "0. LIMPIAR TERMINAL":
    print ("\n Limpiando terminal...\n")
    clearTerm()
else:
    print("\n Esa opción digitada no esta definida en el submenu de compuertas lógicas\n") 


optionssubMenu2 = [ 
     inquirer.List(
         "submenu2",
         message="Selecciona la grafica que deseas visualizar",
         choices=[
             ("GRÁFICA #1", "LITERAL1"),
             ("GRÁFICA #2", "LITERAL2"),
             ("GRÁFICA #3", "LITERAL3"),
             ("Volver atras", "SALIR")
         ]
     )
 ]

answersubMenu2 = inquirer.prompt(optionssubMenu2)
print(f"\n{Fore.YELLOW}{"="*12}{Style.RESET_ALL}{Fore.MAGENTA} > GRAFICAS < {Style.RESET_ALL}{Fore.YELLOW}{"="*12}{Style.RESET_ALL}\n")
print(answersubMenu2["submenu2"])
print(f"="*66+'\n')

    if answersubMenu2["submenu2"] == "GRÁFICA #1":
        print ("\n----------------------------GRÁFICA #1----------------------------\n")
    elif answersubMenu2["submenu2"] == "GRÁFICA #2":
        print ("\n----------------------------GRÁFICA #2----------------------------\n")
    elif answersubMenu2["submenu2"] == "GRÁFICA #3":
        print ("\n----------------------------GRÁFICA #3----------------------------\n")
