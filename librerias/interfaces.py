import re
import os
import sys
from colorama import init, Fore, Back, Style
import inquirer
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from librerias.util import *

init()

def showActualGate(answerS1) -> None:
    print(f"{Fore.LIGHTYELLOW_EX}={Style.RESET_ALL}"*60)
    print(f"{Style.BRIGHT}Compuerta {answerS1}{Style.RESET_ALL}".center(60))
    print(f"{Fore.LIGHTYELLOW_EX}={Style.RESET_ALL}"*60,"\n ")

def showActualVar() -> str:
    booleanVarMessage = f"> Variables booleanas: A:{statementObj['A']}, B:{statementObj['B']}, C:{statementObj['C']}, D:{statementObj['D']}"
    if statementObj['A'] == -1:
        booleanVarMessage = f"> Variables booleanas: A:{None}, B:{None}, C:{None}, D:{None}" 
    return f"{Back.GREEN}{booleanVarMessage}{Style.RESET_ALL}"

def mainMenu() -> dict:
    print(" "*60, showActualVar())
    print("\nA continuación podrá ver las diferentes opciones\nque tiene para interactuar con el proyecto\n ")
    
    optionsMenu = [
        inquirer.List(
            "menu",
            message="Seleccione una opción",
            choices=[
                (f"{Fore.LIGHTYELLOW_EX}► {Style.RESET_ALL}Ingresar variables booleanas {Style.BRIGHT}(A, B, C, D){Style.RESET_ALL}", "var-bool"), 
                (f"{Fore.LIGHTYELLOW_EX}► {Style.RESET_ALL}Ir al Submenú 1 {Style.BRIGHT}(Lector de Compuertas){Style.RESET_ALL}", "submenu1"),
                (f"{Fore.LIGHTYELLOW_EX}► {Style.RESET_ALL}Ir al Submenú 2 {Style.BRIGHT}(Circuitos Lógicos){Style.RESET_ALL}", "submenu2"),
                (f"{Fore.LIGHTYELLOW_EX}► {Style.RESET_ALL}{Fore.GREEN}Limpiar pantalla{Style.RESET_ALL}", "LIMPIAR"),
                (f"{Fore.LIGHTYELLOW_EX}► {Style.RESET_ALL}{Fore.RED}Salir{Style.RESET_ALL}", "SALIR")
            ]
        )
    ]
    return inquirer.prompt(optionsMenu)

def subMenu1(objVar) -> dict:
    print(" "*60, showActualVar())
    optionsSubMenu = [
        inquirer.List(
            "submenu", 
            message= f"Seleccione una opción",

            choices=[
                (f"{Fore.LIGHTYELLOW_EX}► {Style.RESET_ALL}Compuerta {Style.BRIGHT}AND{Style.RESET_ALL}", "AND"),
                (f"{Fore.LIGHTYELLOW_EX}► {Style.RESET_ALL}Compuerta {Style.BRIGHT}OR{Style.RESET_ALL}", "OR"),
                (f"{Fore.LIGHTYELLOW_EX}► {Style.RESET_ALL}Compuerta {Style.BRIGHT}NOT{Style.RESET_ALL}", "NOT"),
                (f"{Fore.LIGHTYELLOW_EX}► {Style.RESET_ALL}Compuerta {Style.BRIGHT}XOR{Style.RESET_ALL}", "XOR"),
                (f"{Fore.LIGHTYELLOW_EX}► {Style.RESET_ALL}Compuerta {Style.BRIGHT}NAND{Style.RESET_ALL}", "NAND"),
                (f"{Fore.LIGHTYELLOW_EX}► {Style.RESET_ALL}Compuerta {Style.BRIGHT}NOR{Style.RESET_ALL}", "NOR"),
                (f"{Fore.LIGHTYELLOW_EX}► {Style.RESET_ALL}Compuerta {Style.BRIGHT}XNOR{Style.RESET_ALL}", "XNOR"),
                (f"{Fore.LIGHTYELLOW_EX}► {Style.RESET_ALL}Compuerta {Style.BRIGHT}IF{Style.RESET_ALL}", "IF"),
                (f"{Fore.RED}► Volver al menú principal{Style.RESET_ALL}", "SALIR"),
                (f"{Fore.GREEN}► Limpiar pantalla{Style.RESET_ALL}", "LIMPIAR")
                ]
            )
    ]
    return inquirer.prompt(optionsSubMenu) 
    
def subMenu2(objVar) -> dict:
    print(" "*30, showActualVar())
    optionsSubMenu2 = [
        inquirer.List(
            "submenu2",
            message= f"Seleccione una opción",
            choices=[
                (f"{Fore.LIGHTYELLOW_EX}► {Style.RESET_ALL}{Style.BRIGHT}Gráfica #1{Style.RESET_ALL}", "LITERAL1"),
                (f"{Fore.LIGHTYELLOW_EX}► {Style.RESET_ALL}{Style.BRIGHT}Gráfica #2{Style.RESET_ALL}", "LITERAL2"),
                (f"{Fore.LIGHTYELLOW_EX}► {Style.RESET_ALL}{Style.BRIGHT}Gráfica #3{Style.RESET_ALL}", "LITERAL3"),
                (f"{Fore.RED}► Volver al menú principal{Style.RESET_ALL}", "SALIR"),
                (f"{Fore.GREEN}► Limpiar pantalla{Style.RESET_ALL}", "LIMPIAR")
            ]
        )
    ]
    return inquirer.prompt(optionsSubMenu2)
