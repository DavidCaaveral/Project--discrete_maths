from compuertas import *

def secondCircuitDiagram(a,b,c,keyA,keyB,keyC) -> str:
    firstLocalAnd = andLogicGate(a,b)
    secondLocalAnd = andLogicGate(a,c)
    unicLocalOr = orLogicGate(firstLocalAnd,secondLocalAnd)
    return f"""
                       ______
{keyA}: {a} ----+------------|      \\       
         |            | AND   )---------------|
{keyB}: {b} ----)------------|______/                |        _____
         |                                    |       \\     \\
         |                                    ---------) OR  )---- Z: {unicLocalOr}
         |                                    |       /_____/
         |             ______                 |
         -------------|      \\                |
                      | AND   )---------------|
{keyC}: {c} -----------------|______/
"""

def firstCircuitDiagram(a,b,c,d,keyA,keyB,keyC,keyD) -> str:
    firstLocalAnd = andLogicGate(a,b)
    unicLocalNand = nAndLogicGate(a,c)
    notD = notLogicGate(d)
    firstLocalOr = orLogicGate(firstLocalAnd,b)
    unicLocalIf = ifLogicGate(firstLocalOr)
    unicLocalXor = xorLogicGate(unicLocalIf,unicLocalNand)
    unicLocalNor = nOrLogicGate(unicLocalXor,notD)
    
    return f"""
                  ______
{keyA}: {a} ----+-------|      \\     
         |       | AND   )-----------|      _____              |\\
{keyB}: {b} -+--)-------|______/            |     \\     \\             |  \\
      |  |                           -------) OR  )------------|IF >-----------|
      |  |                           |     /_____/             |  /            |      _____
      ---)---------------------------|                         |/              |    \\\\     \\
         |                                                                     ------)) XOR )-----------|
         |        ______                                                       |    //_____/            |
         --------|      \\                                                      |                        |      _____       
                 | NAND  )o----------------------------------------------------|                        |     \\     \\ 
{keyC}: {c} ------------|______/                                                                               -------) NOR )o----------  F: {unicLocalNor}
                                                                                                        |     /_____/     
                                                                                                        |
                 |\\                                                                                     |
                 |  \\                                                                                   |
{keyD}: {d} ------------|NOT>o---------------------------------------------------------------------------------|
                 |  / 
                 |/   
      

"""

def thirdCircuitDiagram(a,b,c,d,keyA,keyB,keyC,keyD) -> str:
    notA = notLogicGate(a)
    firstLocalXnor = xNorLogicGate(b,c)
    unicLocalAnd = andLogicGate(b,d)
    unicLocalOr = orLogicGate(notA,firstLocalXnor)
    secondLocalXnor = xNorLogicGate(unicLocalOr,unicLocalAnd)
    
    return f"""
                             
               |\\            
               |  \\          
{keyA}: {a} ----------|NOT>o-------------
               |  /              |      _____
               |/                |     \\     \\
                                 -------) OR  )--------
                   _____         |     /_____/        |
{keyB}: {b} ------+-----\\\\     \\        |                    |        _____   
           |      ))XNOR )o-------                    |      \\\\     \\
{keyC}: {c} ------)-----//_____/                             --------))XNOR )------- R: {secondLocalXnor}
           |                                          |      //_____/    
           |       ______                             |
           -------|      \\                            |
                  | AND   )----------------------------
{keyD}: {d} -------------|______/


"""

print(thirdCircuitDiagram(1,0,1,0,'A','B','C','D'))
