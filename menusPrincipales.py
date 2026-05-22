from colorama import init, Fore, Back, Style
# Menús principales

statementObj = { # Inicialización de keys de objeto
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
    print("A continuación podrá ver las diferentes opciones que tiene para interactuar con el proyecto:\n")
    print("1. Ingresar variables booleanas (A, B, C, D)")
    print("2. Mostrar valor actual de las variables")
    print("3. Ir al Submenú 1 (Lector de Compuertas)")
    print("4. Ir al Submenú 2 (Circuitos Lógicos)")
    print("5. Limpiar pantalla")
    print("6. Salir\n")

    opcionUsuario=int(input("Por favor ingrese una opción valida de las mostradas anteriormente "))

    #OPCION 1.

    if opcionUsuario==1:
        print("\n----------------------------1. Ingreso de variables booleanas (A, B, C, D)----------------------------")

    # Escritura de variables en el objeto
    for key in statementObj:
        statementObj[key] = int(input(f"\nIngrese valor para {key} (0 o 1): "))
        while statementObj[key] != 0 and statementObj[key] != 1:
                print("Error. Solo se permite 0 o 1.")
                statementObj[key]= int(input(f"Ingrese valor para {key} (0 o 1): "))
    
    break
    # else:
    #     print("\nEsa opción digitada no esta definida en el menú principal\n")
    #     enMenuPrincipal == False



