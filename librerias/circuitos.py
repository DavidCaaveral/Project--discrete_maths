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

print(secondCircuitDiagram(0,0,0,'A','B','C'))