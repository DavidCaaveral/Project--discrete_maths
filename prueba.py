import re
from colorama import init, Fore, Back, Style
import inquirer

init()

statementObj = { # Inicialización de keys de objeto
    'A': -1,
    'B': -1,
    'C': -1,
    'D': -1
}
tituloPrincipal = f"{Fore.GREEN}LOGIC CRAFT{Style.RESET_ALL}"

while True:
    pass 
    print(f"{Fore.YELLOW}={Style.RESET_ALL}"*67)
    print(tituloPrincipal.center(76))
    print(f"{Fore.YELLOW}={Style.RESET_ALL}"*67+'\n')
    print("A continuación podrá ver las diferentes opciones\nque tiene para interactuar con el proyecto\n ")
    
    optionsMenu = [
        inquirer.List(
            "menu",
            message="Seleccione una opcion",
            choices=[
                ("Ingresar variables booleanas (A, B, C, D)", "var-bool"),
                ("Mostrar valor actual de las variables","actua-var-bool"),
                ("Ir al Submenú 1 (Lector de Compuertas)","submenu1"),
                ("Ir al Submenú 2 (Circuitos Lógicos)","submenu2"),
                ("Limpiar pantalla","LIMPIAR"),
                ("Salir","SALIR")
            ]
        )
    ]
    answerMenu = inquirer.prompt(optionsMenu)
    
    print(answerMenu["menu"])
    print(f"="*66+'\n')
    
    if (answerMenu["menu"] == "var-bool"):
        print(f"\n{"="*8}> {Fore.CYAN}1. Ingreso de variables booleanas (A, B, C, D){Style.RESET_ALL} <{"="*8} \n")
        for key in statementObj:
            questionBool = [
                inquirer.List(
                    "valor",
                    message=f"Ingrese valor para {key}",
                    choices=[0, 1]
                )
            ]

            answerObj = inquirer.prompt(questionBool)

            statementObj[key] = answerObj["valor"]
    print(statementObj)
    print("")
    break    
