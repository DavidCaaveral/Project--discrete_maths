import re
from colorama import init, Fore, Back, Style
import inquirer
from main import statementObj
from main import clearTerm

init()

tituloPrincipal = f"{Fore.GREEN}LOGIC CRAFT{Style.RESET_ALL}"

# while True:
#     pass 
#     print(f"{Fore.YELLOW}={Style.RESET_ALL}"*67)
#     print(tituloPrincipal.center(76))
#     print(f"{Fore.YELLOW}={Style.RESET_ALL}"*67+'\n')
#     print("A continuación podrá ver las diferentes opciones\nque tiene para interactuar con el proyecto\n ")
    
#     optionsMenu = [
#         inquirer.List(
#             "menu",
#             message="Seleccione una opción",
#             choices=[
#                 ("Ingresar variables booleanas (A, B, C, D)", "var-bool"),
#                 ("Mostrar valor actual de las variables", "actua-var-bool"),
#                 ("Ir al Submenú 1 (Lector de Compuertas)", "submenu1"),
#                 ("Ir al Submenú 2 (Circuitos Lógicos)", "submenu2"),
#                 ("Limpiar pantalla", "LIMPIAR"),
#                 ("Salir", "SALIR")
#             ]
#         )
#     ]
#     answerMenu = inquirer.prompt(optionsMenu)
    
#     print(answerMenu["menu"])
#     print(f"="*66+'\n')
    
#     if (answerMenu["menu"] == "var-bool"):
#         print(f"\n{"="*8}> {Fore.CYAN}1. Ingreso de variables booleanas (A, B, C, D){Style.RESET_ALL} <{"="*8} \n")
#         for key in statementObj:
#             questionBool = [
#                 inquirer.List(
#                     "valor",
#                     message=f"Ingrese valor para {key}",
#                     choices=[0, 1]
#                 )
#             ]

#             answerObj = inquirer.prompt(questionBool)

#             statementObj[key] = answerObj["valor"]
#     print(statementObj)
#     print("")
#     break    

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
    
    print(" "*30, f"> Variables booleanas: A:{statementObj['A']}, B:{statementObj['B']}, C:{statementObj['C']}, D:{statementObj['D']}")
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
    