# Compuerta AND
def andLogicGate(a,b) -> int:
    return a*b

# Diagrama 
def andLogicGateDiagram(a,b,keyA,keyB) -> str:
    localAnd = andLogicGate(a,b)
    return f"""
             ______
{keyA}: {a} -------|      \\
            | AND   )---- {localAnd}
{keyB}: {b} -------|______/
"""
# Compuerta OR
def orLogicGate(a,b) -> int:
    return (a+b) - 1 if (a+b) > 1 else a+b

# Diagrama 
def orLogicGateDiagram(a,b,keyA,keyB) -> str:
    localOr = orLogicGate(a,b)
    return f"""
             _____
{keyA}: {a} --------\\     \\
              ) OR  )---- F: {localOr}
{keyB}: {b} --------/_____/
"""

# Compuerta NOT
def notLogicGate(a) -> int:
    return 1 - a

# Diagrama 
def notLogicGateDiagram(a,keyA) -> str:
    notA = notLogicGate(a)
    return f"""
              |\\
              |  \\
{keyA}: {a} ---------|NOT>o----- F: {notA}
              |  /
              |/
"""

# Compuerta XOR
def xorLogicGate(a,b) -> int:
    notA = notLogicGate(a)
    notB = notLogicGate(b)

    return orLogicGate(a=(a * notB) ,b=(b * notA))

# Diagrama 
def xorLogicGateDiagram(a,b,keyA,keyB) -> str: 
    localXor = xorLogicGate(a,b)
    return f"""
              _____
{keyA}: {a} --------\\\\     \\
              )) XOR )---- F: {localXor}
{keyB}: {b} --------//_____/
"""
# Compuerta IF
def ifLogicGate(a) -> int:
    return  (a) - 1 if a > 1 else a 

# Diagrama 
def ifLogicGateDiagram(a,keyA) -> str:
    localIf = ifLogicGate(a)
    return f"""
              |\\
              |  \\
{keyA}: {a} ---------|IF >----- F: {localIf}
              |  /
              |/
"""
# Compuerta NAND
def nAndLogicGate(a,b) -> int:
    localAnd = andLogicGate(a,b)
    return notLogicGate(localAnd)

# Diagrama 
def nAndLogicGateDiagram(a,b,keyA,keyB) -> str:
    localNAnd = nAndLogicGate(a,b)
    return f"""
             ______
{keyA}: {a} -------|      \\
            | NAND  )o--- F: {localNAnd}
{keyB}: {b} -------|______/
""" 

# Compuerta NOR
def nOrLogicGate(a,b) -> int:
    localOr = orLogicGate(a,b)
    return notLogicGate(localOr)

# Diagrama 
def nOrLogicGateDiagram(a,b,keyA,keyB) -> str:
    localNOr = nOrLogicGate(a,b)
    return f"""
              _____
{keyA}: {a} --------\\     \\
              ) NOR )o--- F: {localNOr}
{keyB}: {b} --------/_____/
"""

# Compuerta XNOR
def xNorLogicGate(a,b) -> int:
    localXor = xorLogicGate(a,b)
    return notLogicGate(localXor)

# Diagrama 
def xNorLogicGateDiagram(a,b,keyA,keyB) -> str:
    localXNor = xNorLogicGate(a,b)
    return f"""
              _____
{keyA}: {a} --------\\\\     \\
              ))XNOR )o--- SALIDA ESPERADA
{keyB}: {b} --------//_____/
"""
# 