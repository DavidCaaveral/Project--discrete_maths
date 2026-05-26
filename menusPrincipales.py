from colorama import init, Fore, Back, Style
# Menús principales

statementObj = { # Inicialización de keys de objeto  Diccionario
    'A': -1,
    'B': -1,
    'C': -1,
    'D': -1
}

# Inicializacion de variables
opcionUsuario=-1
enMenuPrincipal = False
    
while enMenuPrincipal == False:
    print("\n---------------------------------------MENÚ PRINCIPAL---------------------------------------\n")

init() #Inicialización de colorama
userOption=-1
insideMainMenu = False
    
while insideMainMenu == False:
    print(f"\n{Fore.CYAN}--------------------------------------->{Style.RESET_ALL}{Fore.GREEN} LOGIC-CRAFT {Style.RESET_ALL}{Fore.CYAN}<---------------------------------------{Style.RESET_ALL}\n")
    print("A continuación podrá ver las diferentes opciones que tiene para interactuar con el proyecto:\n")
    print(f"{Fore.YELLOW}1.{Style.RESET_ALL} Ingresar variables booleanas (A, B, C, D)")
    print(f"{Fore.YELLOW}2.{Style.RESET_ALL} Mostrar valor actual de las variables")
    print(f"{Fore.YELLOW}3.{Style.RESET_ALL} Ir al Submenú 1 (Lector de Compuertas)")
    print(f"{Fore.YELLOW}4.{Style.RESET_ALL} Ir al Submenú 2 (Circuitos Lógicos)")
    print(f"{Fore.YELLOW}5.{Style.RESET_ALL} {Fore.CYAN}Limpiar pantalla{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}6.{Style.RESET_ALL} {Fore.RED}Salir{Style.RESET_ALL}\n")

    opcionUsuario=int(input("Por favor ingrese una opción valida de las mostradas anteriormente "))

    #OPCION 1.

    if opcionUsuario==1:
        print("\n----------------------------1. Ingreso de variables booleanas (A, B, C, D)----------------------------")

    # Ingreso de variables en el objeto por parte del usuario
        for key in statementObj:
            statementObj[key] = int(input(f"\nIngrese valor para {key} (0 o 1): "))
            while statementObj[key] != 0 and statementObj[key] != 1:
                    print("Error. Solo se permite 0 o 1.")
                    statementObj[key]= int(input(f"Ingrese valor para {key} (0 o 1): "))
        print("\nEl valor actual de las variables:\n")  
        print(statementObj)
        print("")

        break

    #OPCION 2.


    # else:
    #     print("\nEsa opción digitada no esta definida en el menú principal\n")
    #     insideMainMenu == False
