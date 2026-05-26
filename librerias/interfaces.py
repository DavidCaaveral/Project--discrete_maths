import re
from colorama import init, Fore, Back, Style
import inquirer
from main import statementObj
from main import clearTerm
import os

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
                ("Mostrar valor actual de las variables", "actua-var-bool"),
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
            message= (f"\n{Fore.YELLOW}{"►"*12}{Style.RESET_ALL}{Fore.MAGENTA}  COMPUERTAS LÓGICAS {Style.RESET_ALL}{Fore.YELLOW}{"◄"*12}{Style.RESET_ALL}\n"),

            choices=[
                (f"{Fore.LIGHTYELLOW_EX}►{Style.RESET_ALL}COMPUERTA {Fore.MAGENTA}AND{Style.RESET_ALL}", "AND"),
                (f"{Fore.LIGHTYELLOW_EX}► {Style.RESET_ALL}COMPUERTA {Fore.MAGENTA}OR{Style.RESET_ALL}", "OR"),
                (f"{Fore.LIGHTYELLOW_EX}► {Style.RESET_ALL}COMPUERTA {Fore.MAGENTA}NOT{Style.RESET_ALL}", "NOT"),
                (f"{Fore.LIGHTYELLOW_EX}► {Style.RESET_ALL}COMPUERTA {Fore.MAGENTA}XOR{Style.RESET_ALL}", "XOR"),
                (f"{Fore.LIGHTYELLOW_EX}► {Style.RESET_ALL}COMPUERTA {Fore.MAGENTA}NAND{Style.RESET_ALL}", "NAND"),
                (f"{Fore.LIGHTYELLOW_EX}► {Style.RESET_ALL}COMPUERTA {Fore.MAGENTA}NOR{Style.RESET_ALL}", "NOR"),
                (f"{Fore.LIGHTYELLOW_EX}► {Style.RESET_ALL}COMPUERTA {Fore.MAGENTA}XNOR{Style.RESET_ALL}", "XNOR"),
                (f"{Fore.LIGHTYELLOW_EX}► {Style.RESET_ALL}COMPUERTA {Fore.MAGENTA}IF{Style.RESET_ALL}", "IF"),
                (f"{Fore.RED}► VOLVER AL MENÚ PRINCIPAL{Style.RESET_ALL}", "SALIR"),
                (f"{Fore.GREEN}► LIMPIAR TERMINAL{Style.RESET_ALL}", "LIMPIAR")
                ]
            )
    ]
    return inquirer.prompt(optionsSubMenu) 
    
subMenu1(statementObj)

optionsSubMenu2 = [ 
     inquirer.List(
         "submenu2",
         message=(f"\n{Fore.YELLOW}{"►"*12}{Style.RESET_ALL}{Fore.MAGENTA} SELECCIONE LA GRÁFICA QUE DESEA VISUALIZAR {Style.RESET_ALL}{Fore.YELLOW}{"◄"*12}{Style.RESET_ALL}"),
         choices=[
             (f"{Fore.LIGHTYELLOW_EX}►{Style.RESET_ALL}{Fore.MAGENTA}GRÁFICA #1{Style.RESET_ALL}", "LITERAL1"),
             (f"{Fore.LIGHTYELLOW_EX}►{Style.RESET_ALL}{Fore.MAGENTA}GRÁFICA #2{Style.RESET_ALL}", "LITERAL2"),
             (f"{Fore.LIGHTYELLOW_EX}►{Style.RESET_ALL}{Fore.MAGENTA}GRÁFICA #3{Style.RESET_ALL}", "LITERAL3"),
             (f"{Fore.RED}► VOLVER ATRAS{Style.RESET_ALL}", "SALIR")
         ]
     )
 ]

answersubMenu2 = inquirer.prompt(optionsSubMenu2)
print(f"\n{Fore.YELLOW} {"►"*8} {Fore.MAGENTA}GRAFICAS{Style.RESET_ALL} {Fore.YELLOW} {"◄"*8} {Style.RESET_ALL}\n")
print(answersubMenu2["submenu2"])
print(f"="*66+'\n')

if answersubMenu2["submenu2"] == "►GRÁFICA #1":
        print ("\n----------------------------GRÁFICA #1----------------------------\n")
elif answersubMenu2["submenu2"] == "►GRÁFICA #2":
        print ("\n----------------------------GRÁFICA #2----------------------------\n")
elif answersubMenu2["submenu2"] == "►GRÁFICA #3":
        print ("\n----------------------------GRÁFICA #3----------------------------\n")
