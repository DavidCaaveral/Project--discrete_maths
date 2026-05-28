# 1. Importaciones de librerías
import os
import time
from colorama import init, Fore, Back, Style
from librerias.compuertas import *
from librerias.interfaces import *
from librerias.util import *
from librerias.circuitos import *

# 2. Definición de constantes globales

# 3. Definición de funciones

# 4. Definición de clases (opcional)

# 5. Bloque principal de ejecución
def main():
    
    print(f"{Fore.LIGHTYELLOW_EX}{'='*60}{Style.RESET_ALL}")
    print(f"{Fore.LIGHTGREEN_EX}LOGICRAFT{Style.RESET_ALL}".center(70))
    print(f"{Fore.LIGHTYELLOW_EX}{'='*60}{Style.RESET_ALL}")

    while True:
    
        electedOption = mainMenu()["menu"] # llamada al diccioanrio que retorna el la funcion mainMenu que usa inquirer
        
        # función para salir
        if electedOption == "SALIR":
                    break
        # función para limpiar la terminal 
        if electedOption == "LIMPIAR":
                    clearTerm()
                    continue
        
        # switch utilizado       
        match electedOption:
            # en caso de elegir el ingreso de las variables booleanas
            case "var-bool":
                print(f"="*66+'\n')
                print(f"\n{"="*8}> {Fore.CYAN} Ingreso de variables booleanas {Style.RESET_ALL} <{"="*8} \n")
                
                #itera sobre el diccionario de variables para llenar todas sus keys
                for key in statementObj:
                    # uso de inquirer para menu de 0 o 1
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
            # en caso de elegir el lector de compuertas    
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
                            print(f"{Style.BRIGHT}►OPERACIÓN:{Style.RESET_ALL}")
                            showgates(varAS1,varBS1,localAnd,submenuOption1)
                            print(f"{Style.BRIGHT}►DIAGRAMA:{Style.RESET_ALL}")
                            print(andLogicGateDiagram(valueAS1,valueBS1,varAS1,varBS1))
                        case "OR":
                            localOr = orLogicGate(valueAS1,valueBS1)
                            showActualGate(submenuOption1)
                            print(f"{Style.BRIGHT}►OPERACIÓN:{Style.RESET_ALL}")
                            showgates(varAS1,varBS1,localOr,submenuOption1)
                            print(f"{Style.BRIGHT}►DIAGRAMA:{Style.RESET_ALL}")
                            print(orLogicGateDiagram(valueAS1,valueBS1,varAS1,varBS1))  
                        case "NOT":
                            localNot = notLogicGate(valueAS1)
                            showActualGate(submenuOption1)
                            print(f"{Style.BRIGHT}►OPERACIÓN:{Style.RESET_ALL}")
                            print(f"{submenuOption1} {varAS1} → {localNot}".center(60))
                            print(f"{Style.BRIGHT}►DIAGRAMA:{Style.RESET_ALL}")
                            print(notLogicGateDiagram(valueAS1,varAS1))  
                        case "XOR":
                            localXor = xorLogicGate(valueAS1,valueBS1)
                            showActualGate(submenuOption1)
                            print(f"{Style.BRIGHT}►OPERACIÓN:{Style.RESET_ALL}")
                            showgates(varAS1,varBS1,localXor,submenuOption1)
                            print(f"{Style.BRIGHT}►DIAGRAMA:{Style.RESET_ALL}")
                            print(xorLogicGateDiagram(valueAS1,valueBS1,varAS1,varBS1))     
                        case "NAND":
                            localNAnd = nAndLogicGate(valueAS1,valueBS1)
                            showActualGate(submenuOption1)
                            print(f"{Style.BRIGHT}►OPERACIÓN:{Style.RESET_ALL}")
                            showgates(varAS1,varBS1,localNAnd,submenuOption1)
                            print(f"{Style.BRIGHT}►DIAGRAMA:{Style.RESET_ALL}")
                            print(nAndLogicGateDiagram(valueAS1,valueBS1,varAS1,varBS1))  
                        case "NOR":
                            localNOr = nOrLogicGate(valueAS1,valueBS1)
                            showActualGate(submenuOption1)
                            print(f"{Style.BRIGHT}►OPERACIÓN:{Style.RESET_ALL}")
                            showgates(varAS1,varBS1,localNOr,submenuOption1)
                            print(f"{Style.BRIGHT}►DIAGRAMA:{Style.RESET_ALL}")
                            print(nOrLogicGateDiagram(valueAS1,valueBS1,varAS1,varBS1))  
                        case "XNOR":
                            localXNOr = xNorLogicGate(valueAS1,valueBS1)
                            showActualGate(submenuOption1)
                            print(f"{Style.BRIGHT}►OPERACIÓN:{Style.RESET_ALL}")
                            showgates(varAS1,varBS1,localXNOr,submenuOption1)
                            print(f"{Style.BRIGHT}►DIAGRAMA:{Style.RESET_ALL}")
                            print(xNorLogicGateDiagram(valueAS1,valueBS1,varAS1,varBS1))    
                        case "IF":
                            localIf = ifLogicGate(valueAS1)
                            showActualGate(submenuOption1)
                            print(f"{Style.BRIGHT}►OPERACIÓN:{Style.RESET_ALL}")
                            print(f"{submenuOption1} {varAS1} → {localIf}".center(60))
                            print(f"{Style.BRIGHT}►DIAGRAMA:{Style.RESET_ALL}")
                            print(ifLogicGateDiagram(valueAS1,varAS1))      
           
            case "submenu2":
                
                if not booleanValidation(statementObj):
                    continue
                
                print(f"="*66+'\n')
                print(f"\n{"="*21}> {Fore.CYAN} Circuitos Logicos {Style.RESET_ALL} <{"="*22} \n \n")
                
                Flag = True
                while Flag:
                    listVarElectedS2 = []
                    submenuOptionS2 = subMenu2(statementObj)["submenu2"]
                    definedRangeS2 = 3 if submenuOptionS2 == "LITERAL2"  else 4 #un operador ternario que asigna un valor u otro   
                    
                    if submenuOptionS2 == "SALIR":
                        break

                    if submenuOptionS2 == "LIMPIAR":
                        clearTerm()
                        continue
                    
                    for i in range(definedRangeS2):
                        questionVarS2 = [
                            inquirer.List(
                                "varS2",
                                message=f"Ingrese las variables que desee utilizar {"=="*5} {showActualVar()}",
                                choices=['A', 
                                         'B', 
                                         'C', 
                                         'D']
                            )
                        ]
                        answerVarS2 = inquirer.prompt(questionVarS2)
                        listVarElectedS2.append(answerVarS2['varS2'])  
                        
                    varAS2 = listVarElectedS2[0]
                    varBS2 = listVarElectedS2[1]
                    varCS2 = listVarElectedS2[2]
                    varDS2 = listVarElectedS2[3] if len(listVarElectedS2) > 3 else "" 
                    valueAS2 = statementObj[listVarElectedS2[0]]   
                    valueBS2 = statementObj[listVarElectedS2[1]]   
                    valueCS2 = statementObj[listVarElectedS2[2]]
                    valueDS2 = statementObj[listVarElectedS2[3]] if len(listVarElectedS2) > 3 else -1 
                    
                    match submenuOptionS2:
                        case "LITERAL1":
                            print("="*60)
                            print(F"{Fore.CYAN}► Punto 1 <{Style.RESET_ALL}".center(60))
                            print("="*60,"\n ")
<<<<<<< HEAD
                            time.sleep(2)
                            print(f"► EXPRESIÓN:\n")
                            print(originalExpresionLit1())
                            time.sleep(2)
                            print(f"\n► DIAGRAMA:\n") 
                            print(firstCircuitDiagram(valueAS2,valueBS2,valueCS2,valueDS2,varAS2,varBS2,varCS2,varDS2)) 
                            time.sleep(2)
                            print(f"\n► TRANSFORMACIÓN:\n")
                            print(tramsformationExpresionLit1())
                            time.sleep(2)
                            print(f"\n► SIMPLIFICACIÓN:\n")
=======
                            print(f"{Fore.CYAN}► EXPRESIÓN:\n{Style.RESET_ALL}")
                            print(originalExpresionLit1())
                            print("="*60, "\n")
                            print(f"{Fore.CYAN}\n► DIAGRAMA:\n{Style.RESET_ALL}") 
                            print(firstCircuitDiagram(valueAS2,valueBS2,valueCS2,valueDS2,varAS2,varBS2,varCS2,varDS2)) 
                            print("="*60, "\n")
                            print(f"{Fore.CYAN}\n► TRANSFORMACIÓN:\n{Style.RESET_ALL}")
                            print(tramsformationExpresionLit1())
                            print("="*60, "\n")
                            print(f"{Fore.CYAN}\n► SIMPLIFICACIÓN:\n{Style.RESET_ALL}")
>>>>>>> 9730e3a6ca830e18c69662ac978be1845d0207fe
                            print(simplificationExpresionLit1())
                        case "LITERAL2":
                            print("="*60)
                            print(F"{Fore.CYAN}► Punto 2 <{Style.RESET_ALL}".center(60))
                            print("="*60,"\n ")
<<<<<<< HEAD
                            time.sleep(2)
                            print(f"► EXPRESIÓN:\n")
                            print(originalExpresionLit2())
                            time.sleep(2)
                            print(f"\n► DIAGRAMA:\n") 
                            print(secondCircuitDiagram(valueAS2,valueBS2,valueCS2,varAS2,varBS2,varCS2)) 
                            time.sleep(2)
                            print(f"\n► SIMPLIFICACIÓN:\n")
=======
                            print(f"{Fore.CYAN}► EXPRESIÓN:\n{Style.RESET_ALL}")
                            print(originalExpresionLit2())
                            print("="*60, "\n")
                            print(f"{Fore.CYAN}\n► DIAGRAMA:\n{Style.RESET_ALL}") 
                            print(secondCircuitDiagram(valueAS2,valueBS2,valueCS2,varAS2,varBS2,varCS2)) 
                            print("="*60, "\n")
                            print(f"{Fore.CYAN}\n► SIMPLIFICACIÓN:\n{Style.RESET_ALL}")
>>>>>>> 9730e3a6ca830e18c69662ac978be1845d0207fe
                            print(simplificationExpresionLit2())
                            
                        case "LITERAL3":
                            print("="*60)
                            print(F"{Fore.CYAN}► Punto 3 <{Style.RESET_ALL}".center(60))
                            print("="*60,"\n ")
<<<<<<< HEAD
                            time.sleep(2)
                            print(f"► EXPRESIÓN:\n")
                            print(originalExpresionLit3())
                            time.sleep(2)
                            print(f"\n► EXPRESIÓN ORIGINAL TRANSFORMADA:\n")
                            print(transformGraficExpresionLit3)
                            time.sleep(2)
                            print(f"\n► DIAGRAMA:\n") 
                            print(thirdCircuitDiagram(valueAS2,valueBS2,valueCS2,valueDS2,varAS2,varBS2,varCS2,varDS2)) 
                            time.sleep(2)
                            print(f"\n► TRANSFORMACIÓN:\n")
                            print(transformExpresionLit3())
                            time.sleep(2)
                            print(f"\n► SIMPLIFICACIÓN:\n")
=======
                            print(f"{Fore.CYAN}► EXPRESIÓN:\n{Style.RESET_ALL}")
                            print(originalExpresionLit3())
                            print("="*60, "\n")
                            print(f"{Fore.CYAN}\n► EXPRESIÓN ORIGINAL TRANSFORMADA:\n{Style.RESET_ALL}")
                            print(transformGraficExpresionLit3())
                            print("="*60, "\n")
                            print(f"{Fore.CYAN}\n► DIAGRAMA:\n{Style.RESET_ALL}") 
                            print(thirdCircuitDiagram(valueAS2,valueBS2,valueCS2,valueDS2,varAS2,varBS2,varCS2,varDS2)) 
                            print("="*60, "\n")
                            print(f"{Fore.CYAN}\n► TRANSFORMACIÓN:\n{Style.RESET_ALL}")
                            print(transformExpresionLit3())
                            print("="*60, "\n")
                            print(f"{Fore.CYAN}\n► SIMPLIFICACIÓN:\n{Style.RESET_ALL}")
>>>>>>> 9730e3a6ca830e18c69662ac978be1845d0207fe
                            print(simplificationExpresionLit3())
    time.sleep(2)
    print(f"{Fore.YELLOW}={Style.RESET_ALL}"*60)
    print(f"{Style.BRIGHT}HASTA PRONTO{Style.RESET_ALL}".center(65))
    print(f"{Fore.YELLOW}={Style.RESET_ALL}"*60)
# 6. Punto de entrada
if __name__ == "__main__":
    main()
    
