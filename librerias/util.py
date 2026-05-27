import os

statementObj = { # Inicialización de keys de objeto
    'A': -1,
    'B': -1,
    'C': -1,
    'D': -1
}

def booleanValidation(objVar) -> any:
    for key in objVar:
        if objVar[key] != 0 and objVar[key] != 1:
            print("="*60)
            print("ERROR VARIABLES BOOLEANAS NO ASIGNADAS".center(60))
            print("="*60)
            return False
    return True    

def clearTerm() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
