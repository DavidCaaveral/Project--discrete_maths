# FUNCIONES Y VARIABLES DE USO GLOBAL

import os
import time
# OBJETO QUE CONTIENE LAS VARIABLES A,B,C,D
statementObj = { # Inicialización de keys de objeto
    'A': -1,
    'B': -1,
    'C': -1,
    'D': -1
}
# Función de validacion de llenado del objeto
def booleanValidation(objVar) -> any:
    for key in objVar:
        if objVar[key] != 0 and objVar[key] != 1:
            time.sleep (1)
            clearTerm()
            print("="*60)
            print("ERROR VARIABLES BOOLEANAS NO ASIGNADAS".center(60))
            print("="*60)
            time.sleep (2)
            clearTerm()
            return False
    return True    
# Función que limpia la terminal
def clearTerm() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
