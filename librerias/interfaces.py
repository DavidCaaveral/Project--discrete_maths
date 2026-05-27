import re
from colorama import init, Fore, Back, Style
import inquirer
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
            message="Seleccione una opcion",
            choices=[
            ("compuerta AND", "AND"),
            ("compuerta OR", "OR"),
            ("compuerta NOT", "NOT"),
            ("compuerta XOR", "XOR"),
            ("compuerta NAND", "NAND"),
            ("compuerta NOR", "NOR"),
            ("compuerta XNOR", "XNOR"),
            ("compuerta IF", "IF"),
            ("Volver al menú principal", "VOLVER"),
            ("limpiar terminal", "LIMPIAR")
                ]
            )
    ]
    return inquirer.prompt(optionsSubMenu) 
   