import re
import os
import sys
from colorama import init, Fore, Back, Style
import inquirer
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from util import *

init()

def showActualGate(answerS1) -> None:
    print("="*60)
    print(f"Compuerta {answerS1}".center(60))
    print("="*60,"\n ")

def showActualVar() -> str:
    return f"> Variables booleanas: A:{statementObj['A']}, B:{statementObj['B']}, C:{statementObj['C']}, D:{statementObj['D']}"    

def mainMenu() -> dict:
    print("A continuación podrá ver las diferentes opciones\nque tiene para interactuar con el proyecto\n ")
    
    optionsMenu = [
        inquirer.List(
            "menu",
            message="Seleccione una opción",
            choices=[
                ("Ingresar variables booleanas (A, B, C, D)", "var-bool"),
                ("Ir al Submenú 1 (Lector de Compuertas)", "submenu1"),
                ("Ir al Submenú 2 (Circuitos Lógicos)", "submenu2"),
                ("Limpiar pantalla", "LIMPIAR"),
                ("Salir", "SALIR")
            ]
        )
    ]
    return inquirer.prompt(optionsMenu)

def subMenu1(objVar) -> dict:
    
    print(" "*30, showActualVar())
    optionsSubMenu = [
        inquirer.List(
            "submenu", 
            message= f"Seleccione una opcion: ",

            choices=[
                (f"{Fore.LIGHTYELLOW_EX}► {Style.RESET_ALL}Compuerta {Fore.MAGENTA}AND{Style.RESET_ALL}", "AND"),
                (f"{Fore.LIGHTYELLOW_EX}► {Style.RESET_ALL}Compuerta {Fore.MAGENTA}OR{Style.RESET_ALL}", "OR"),
                (f"{Fore.LIGHTYELLOW_EX}► {Style.RESET_ALL}Compuerta {Fore.MAGENTA}NOT{Style.RESET_ALL}", "NOT"),
                (f"{Fore.LIGHTYELLOW_EX}► {Style.RESET_ALL}Compuerta {Fore.MAGENTA}XOR{Style.RESET_ALL}", "XOR"),
                (f"{Fore.LIGHTYELLOW_EX}► {Style.RESET_ALL}Compuerta {Fore.MAGENTA}NAND{Style.RESET_ALL}", "NAND"),
                (f"{Fore.LIGHTYELLOW_EX}► {Style.RESET_ALL}Compuerta {Fore.MAGENTA}NOR{Style.RESET_ALL}", "NOR"),
                (f"{Fore.LIGHTYELLOW_EX}► {Style.RESET_ALL}Compuerta {Fore.MAGENTA}XNOR{Style.RESET_ALL}", "XNOR"),
                (f"{Fore.LIGHTYELLOW_EX}► {Style.RESET_ALL}Compuerta {Fore.MAGENTA}IF{Style.RESET_ALL}", "IF"),
                (f"{Fore.RED}► VOLVER AL MENÚ PRINCIPAL{Style.RESET_ALL}", "SALIR"),
                (f"{Fore.GREEN}► LIMPIAR TERMINAL{Style.RESET_ALL}", "LIMPIAR")
                ]
            )
    ]
    return inquirer.prompt(optionsSubMenu) 
    

def subMenu2(objVar) -> dict:
    print(" "*30, showActualVar())
    optionsSubMenu2 = [
        inquirer.List(
            "submenu2",
            message= f"Seleccione una opcion: ",
            choices=[
                (f"{Fore.LIGHTYELLOW_EX}►{Style.RESET_ALL}{Fore.MAGENTA}Gráfica #1{Style.RESET_ALL}", "LITERAL1"),
                (f"{Fore.LIGHTYELLOW_EX}►{Style.RESET_ALL}{Fore.MAGENTA}Gráfica #2{Style.RESET_ALL}", "LITERAL2"),
                (f"{Fore.LIGHTYELLOW_EX}►{Style.RESET_ALL}{Fore.MAGENTA}Gráfica #3{Style.RESET_ALL}", "LITERAL3"),
                (f"{Fore.RED}► VOLVER ATRAS{Style.RESET_ALL}", "SALIR")
            ]
        )
    ]
    return inquirer.prompt(optionsSubMenu2)

# answersubMenu2 =subMenu2(statementObj)
# print (f"\n{Fore.YELLOW} {"►"*20}{Style.RESET_ALL}{Fore.MAGENTA} GRAFICAS {Style.RESET_ALL}{Fore.YELLOW} {"◄"*20}{Style.RESET_ALL}\n")
# print(answersubMenu2["submenu2"])
# print (f"►"*66+'\n')



# answersubMenu2 = inquirer.prompt(optionsSubMenu2)
# print(f"\n{Fore.YELLOW} {"►"*20}{Style.RESET_ALL}{Fore.MAGENTA} GRAFICAS {Style.RESET_ALL}{Fore.YELLOW} {"◄"*20}{Style.RESET_ALL}\n")
# print(answersubMenu2["submenu2"])
# print(f"="*66+'\n')

# if answersubMenu2["submenu2"] == "►Gráfica #1":
#         print (f"\n {Fore.YELLOW}{"►"*20}{Style.RESET_ALL}{Fore.MAGENTA} Gráfica#1 {Style.RESET_ALL}{Fore.YELLOW} {"◄"*20}{Style.RESET_ALL} \n")
# elif answersubMenu2["submenu2"] == "►Gráfica #2":
#         print (f"\n{Fore.YELLOW}{"►"*20}{Style.RESET_ALL}{Fore.MAGENTA} Gráfica #2 {Style.RESET_ALL}{Fore.YELLOW} {"◄"*20}{Style.RESET_ALL}\n")
# elif answersubMenu2["submenu2"] == "►GRÁFICA #3":
#         print (f"\n{Fore.YELLOW}{"►"*20}{Style.RESET_ALL}{Fore.MAGENTA} Gráfica #3 {Style.RESET_ALL}{Fore.YELLOW} {"◄"*20}{Style.RESET_ALL}\n")
