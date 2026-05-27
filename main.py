# 1. Importaciones de librerías
import os
import time
from colorama import init, Fore, Back, Style
from librerias.compuertas import *
from librerias.interfaces import *
from util import *

# 2. Definición de constantes globales

# 3. Definición de funciones

# 4. Definición de clases (opcional)

# 5. Bloque principal de ejecución
def main():
    while True:
        electedOption = mainMenu()["menu"]
        match electedOption:
            
            case "var-bool":
                print(f"="*66+'\n')
                print(f"\n{"="*8}> {Fore.CYAN} Ingreso de variables booleanas {Style.RESET_ALL} <{"="*8} \n")
                for key in statementObj:
                    questionBool = [
                        inquirer.List(
                            "value",
                            message=f"Ingrese valor para {key}",
                            choices=[0, 1]
                        )
                    ] 

                    answerObj = inquirer.prompt(questionBool)

                    statementObj[key] = answerObj["value"]
                print("Cargando...".center(76))
                time.sleep(2)
                print(f"\nVariables asignadas con exito {" - -"*5} A:{statementObj['A']}, B:{statementObj['B']}, C:{statementObj['C']}, D:{statementObj['D']}\n \n")
                print("Redirigiendo...".center(76), "\n")
                time.sleep(2)
                
            case "submenu1":
                
                if not booleanValidation(statementObj):
                    continue
                
                print(f"="*66+'\n')
                print(f"\n{"="*21}> {Fore.CYAN} Compuertas Logicas {Style.RESET_ALL} <{"="*21} \n \n")
                
                Flag = True
                while Flag:
                    listVarElected = []
                    submenuOption1= subMenu1(statementObj)["submenu"]
                    definedRange = 1 if submenuOption1 == "NOT" or submenuOption1 == "IF" else 2 #un operador ternario que asigna un valor u otro 
                    
                    if submenuOption1 == "SALIR":
                        break

                    if submenuOption1 == "LIMPIAR":
                        clearTerm()
                        continue
                    
                    for i in range(definedRange):
                        questionVar = [
                            inquirer.List(
                                "var",
                                message=f"Ingrese las variables que desee utilizar {"=="*5} {showActualVar()}",
                                choices=['A','B','C','D']
                            )
                        ]
                        answerVar = inquirer.prompt(questionVar)
                        listVarElected.append(answerVar['var'])
                        
                    varAS1 = listVarElected[0]
                    varBS1 = listVarElected[1] if len(listVarElected) > 1 else "" 
                    valueAS1 = statementObj[listVarElected[0]]   
                    valueBS1 = statementObj[listVarElected[1]] if len(listVarElected) > 1 else -1 
                    match submenuOption1:
                        case "AND":
                            localAnd = andLogicGate(valueAS1,valueBS1)
                            showActualGate(submenuOption1)
                            print(f">OPERACIÓN:")
                            showgates(varAS1,varBS1,localAnd,submenuOption1)
                            print(f">DIAGRAMA:")
                            print(andLogicGateDiagram(valueAS1,valueBS1,varAS1,varBS1))
                        case "OR":
                            localOr = orLogicGate(valueAS1,valueBS1)
                            showActualGate(submenuOption1)
                            print(f">OPERACIÓN:")
                            showgates(varAS1,varBS1,localOr,submenuOption1)
                            print(f">DIAGRAMA:")
                            print(orLogicGateDiagram(valueAS1,valueBS1,varAS1,varBS1))  
                        case "NOT":
                            localNot = notLogicGate(valueAS1)
                            showActualGate(submenuOption1)
                            print(f">OPERACIÓN:")
                            print(f"{submenuOption1} {varAS1} → {localNot}".center(60))
                            print(f">DIAGRAMA:")
                            print(notLogicGateDiagram(valueAS1,varAS1))  
                        case "XOR":
                            localXor = xorLogicGate(valueAS1,valueBS1)
                            showActualGate(submenuOption1)
                            print(f">OPERACIÓN:")
                            showgates(varAS1,varBS1,localXor,submenuOption1)
                            print(f">DIAGRAMA:")
                            print(xorLogicGateDiagram(valueAS1,valueBS1,varAS1,varBS1))     
                        case "NAND":
                            localNAnd = nAndLogicGate(valueAS1,valueBS1)
                            showActualGate(submenuOption1)
                            print(f">OPERACIÓN:")
                            showgates(varAS1,varBS1,localNAnd,submenuOption1)
                            print(f">DIAGRAMA:")
                            print(nAndLogicGateDiagram(valueAS1,valueBS1,varAS1,varBS1))  
                        case "NOR":
                            localNOr = nOrLogicGate(valueAS1,valueBS1)
                            showActualGate(submenuOption1)
                            print(f">OPERACIÓN:")
                            showgates(varAS1,varBS1,localNOr,submenuOption1)
                            print(f">DIAGRAMA:")
                            print(nOrLogicGateDiagram(valueAS1,valueBS1,varAS1,varBS1))  
                        case "XNOR":
                            localXNOr = xNorLogicGate(valueAS1,valueBS1)
                            showActualGate(submenuOption1)
                            print(f">OPERACIÓN:")
                            showgates(varAS1,varBS1,localXNOr,submenuOption1)
                            print(f">DIAGRAMA:")
                            print(xNorLogicGateDiagram(valueAS1,valueBS1,varAS1,varBS1))    
                        case "IF":
                            localIf = ifLogicGate(valueAS1)
                            showActualGate(submenuOption1)
                            print(f">OPERACIÓN:")
                            print(f"{submenuOption1} {varAS1} → {localIf}".center(60))
                            print(f">DIAGRAMA:")
                            print(ifLogicGateDiagram(valueAS1,varAS1))      
                           

# 6. Punto de entrada
if __name__ == "__main__":
    main()
    
