# 1. Importaciones de librerías
import os
import time
from colorama import init, Fore, Back, Style

# 2. Definición de constantes globales
statementObj = { # Inicialización de keys de objeto
    'A': -1,
    'B': -1,
    'C': -1,
    'D': -1
}

# 3. Definición de funciones

# Compuerta AND
def andLogicGate(a,b) -> int:
    return a*b

def andLogicGateDiagram(a,b) -> str:
    localAnd = andLogicGate(a,b)
    return f"""
         ______
{a} -------|      \\
         | AND   )---- {localAnd}
{b} -------|______/
"""
# Compuerta OR
def orLogicGate(a,b) -> int:
    return (a+b) - 1 if (a+b) > 1 else a+b

def orLogicGateDiagram(a,b) -> str:
    localOr = orLogicGate(a,b)
    return f"""
          _____
{a} --------\\     \\
           ) OR  )---- {localOr}
{b} --------/_____/
"""

# Compuerta NOT
def notLogicGate(a) -> int:
    return 1 - a

def notLogicGateDiagram(a) -> str:
    notA = notLogicGate(a)
    return f"""
           |\\
           |  \\
{a} ---------|NOT>o----- {notA}
           |  /
           |/
"""

# Compuerta XOR
def xorLogicGate(a,b) -> int:
    notA = notLogicGate(a)
    notB = notLogicGate(b)

    return orLogicGate(a=(a * notB) ,b=(b * notA))

# Compuerta IF
def ifLogicGate(a) -> int:
    return  (a) - 1 if a > 1 else a 

# Compuerta NAND
def nAndLogicGate(a,b) -> int:
    localAnd = andLogicGate(a,b)
    return notLogicGate(localAnd)

# Compuerta NOR
def nOrLogicGate(a,b) -> int:
    localOr = orLogicGate(a,b)
    return notLogicGate(localOr)

# Compuerta XNOR
def xnorLogicGate(a,b) -> int:
    localXor = xorLogicGate(a,b)
    return notLogicGate(localXor)

# 
def clearTerm() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

# 4. Definición de clases (opcional)

# 5. Bloque principal de ejecución
def main():
    a = 1
    b = 1
    print(andLogicGate(a,b))
    print(andLogicGateDiagram(a,b))

# 6. Punto de entrada
if __name__ == "__main__":
    main()
    