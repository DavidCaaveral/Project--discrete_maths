# Menús principales

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

       #VARIABLE A 
    variableA = int(input("\nIngrese valor para A (0 o 1): "))
    while variableA != 0 and variableA != 1:
            print("Error. Solo se permite 0 o 1.")
            variableA = int(input("Ingrese valor para A (0 o 1): "))

        #VARIABLE B
    variableB = int(input("\nIngrese valor para B (0 o 1): "))
    while variableB != 0 and variableB != 1:
            print("Error. Solo se permite 0 o 1.")
            variableA = int(input("Ingrese valor para B (0 o 1): "))
    
    break
    # else:
    #     print("\nEsa opción digitada no esta definida en el menú principal\n")
    #     enMenuPrincipal == False



