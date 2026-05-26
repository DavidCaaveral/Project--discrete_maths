# 1. Importaciones de librerías
import os
import time
from colorama import init, Fore, Back, Style
from librerias.compuertas import *

# 2. Definición de constantes globales
statementObj = { # Inicialización de keys de objeto
    'A': -1,
    'B': -1,
    'C': -1,
    'D': -1
}

# 3. Definición de funciones

def clearTerm() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

# 4. Definición de clases (opcional)

# 5. Bloque principal de ejecución
def main():
    pass

# 6. Punto de entrada
if __name__ == "__main__":
    main()
    