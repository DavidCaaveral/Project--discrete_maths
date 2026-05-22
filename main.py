# 1. Importaciones de librerías
import os
from colorama import init, Fore, Back, Style


# 2. Definición de constantes globales
statementObj = { # Inicialización de keys de objeto
    'A': -1,
    'B': -1,
    'C': -1,
    'D': -1
}


# 3. Definición de funciones

def andLogicGate(a,b) -> int:
    return a*b

def orLogicGate(a,b) -> int:
    return (a+b) - 1 if (a+b) > 1 else a+b

def notLogicGate(a) -> int:
    return 1 - a

def xorLogicGate(a,b) -> int:
    notA = notLogicGate(a)
    notB = notLogicGate(b)

    return orLogicGate(a=(a * notB) ,b=(b * notA))

def ifLogicGate(a) -> int:
    return  (a) - 1 if a > 1 else a 

def nAndLogicGate(a,b) -> int:
    localAnd = andLogicGate(a,b)
    return notLogicGate(localAnd)

def nOrLogicGate(a,b) -> int:
    localOr = orLogicGate(a,b)
    return notLogicGate(localOr)

def xnorLogicGate(a,b) -> int:
    localXor = xorLogicGate(a,b)
    return notLogicGate(localXor)

def clearTerm() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

# 4. Definición de clases (opcional)

# 5. Bloque principal de ejecución
def main():
    a = 0
    b = 0
    print(xorLogicGate(a,b))

# 6. Punto de entrada
if __name__ == "__main__":
    main()
    