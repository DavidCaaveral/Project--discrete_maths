print("___________________________________________________________________________________________________________")
print("\nFigura 2\n")

# Expresión original
print("Z = [(A x B) + (A x C)]")

print("""
                   ______
A ----+------------|      \\       
      |            | AND   )---------------|
B ----)------------|______/                |       _____
      |                                    |       \\     \\
      |                                    ---------) OR  )---- Z
      |                                    |       /_____/
      |            ______                  |
      -------------|      \\                |
                   | AND   )---------------|
C -----------------|______/
""")

# simplificación
print("""
Simplificación de la expresion a través de leyes booleanas:
      
Z = [(A x B) + (A x C)])     → Expresion original
Z =   A x (B x C)            → Distributiva inversa / Factor común
Z =   A x (B x C)            → Expresión simplificada
""")




print("___________________________________________________________________________________________________________")
print("\nFigura 1\n")
# Expresión original
print("F = {[((A x B) + B) xor (A x C)'] + D'}'")


print("""
              ______
A ----+-------|      \\     
      |       | AND   )-----------|     _____               |\\
B -+--)-------|______/            |     \\     \\             |  \\
   |  |                           -------) OR  )------------|IF >-----------|
   |  |                           |     /_____/             |  /            |     _____
   ---)---------------------------|                         |/              |    \\\\     \\
      |                                                                     ------)) XOR )-----------|
      |       ______                                                        |    //_____/            |
      --------|      \\                                                      |                        |     _____       
              | NAND  )o----------------------------------------------------|                        |     \\     \\ 
C ------------|______/                                                                               -------) NOR )o----------  F
                                                                                                     |     /_____/     
                                                                                                     |
              |\\                                                                                     |
              |  \\                                                                                   |
C ------------|NOT>o---------------------------------------------------------------------------------|
              |  / 
              |/   


""")
# transformacion
print("""
     Reescritura de la expresion con operadores logicos a expresion con operaciones booleanas

F = {[((A x B) + B) xor (A x C)'] + D'}'     →     Expresión original  con operadores logicos especiales
F = {[((AB)+B)((AC)')'+((AB)+B)'(AC)']+D'}'  →     Expandir termino xor
F = {[((AB)+B)((AC)')'+((AB)+B)'(AC)']+D'}'  →     Expresión reescrita con operaciones booleanas basicas""")
 
# simplificacion 
print("""     
Simplificación de la expresion a través de leyes booleanas:
      
F = {[((AB)+B)((AC)')'+((AB)+B)'(AC)']+D'}'  →     Expresión
F = {[((AB)+B)(AC)+((AB)+B)'(AC)']+D'}'      →     Doble negación
F = {[(B)(AC)+((AB)+B)'(AC)']+D'}'           →     Absorción del tipo (AB+B=B)
F = {[ABC+((AB)+B)'(AC)']+D'}'               →     Asociativa
F = {[ABC+(B)'(AC)']+D'}'                    →     Absorción del tipo (AB+B=B)
F = {[ABC+B'(AC)']+D'}'                      →     Asociativa
F = {[ABC+B'(A'+C')]+D'}'                    →     De Morgan
F = {[ABC+A'B'+B'C']+D'}'                    →     Distributiva 
F = (ABC+A'B'+B'C'+D')'                      →     Asociativa
F = (ABC+A'B'+B'C'+D')'                      →     Expresión simplificada 
      """)

print("___________________________________________________________________________________________________________")
print("\nFigura 3\n")

# Expresión original
print("R = [ A -> (B <-> C) ] xor (B ^ D)")
# expresion transformada para grafica
print("R = [ A' + (B xor C)'] xor (B x D)")

print("""
                             
            |\\            
            |  \\          
A ----------|NOT>o-------------
            |  /              |     _____
            |/                |     \\     \\
                              -------) OR  )--------
               _____          |     /_____/        |
B ------+-----\\\\     \\        |                    |       _____   
        |      ))XNOR )o-------                    |      \\\\     \\
C ------)-----//_____/                             --------))XNOR )------- R
        |                                          |      //_____/    
        |      ______                              |
        -------|      \\                            |
               | AND   )----------------------------
D -------------|______/

""")

# Transformacion

print("""
    Reescritura de la expresion con operadores logicos a expresion con operaciones booleanas

R = [ A -> (B <-> C) ] xor (B ^ D)     →     Expresión original  con operadores logicos especiales
R = [ A -> (B <-> C) ] xor (B x D)     →     Reemplazar (^) por el termino (multiplicación)
R = [ A -> (BC+B'C') ] xor (  BD )     →     Expandir y reemplazar el termino (<->)
R = [(A'+ BC + B'C') ] xor (  BD )     →     Expandir y reemplazar el termino ( ->)
R = (A'+BC+B'C')(BD)'+(A'+BC+B'C')'BD  →     Expandir y reemplazar el termino (XOR)
R = (A'+BC+B'C')(BD)'+(A'+BC+B'C')'BD  →     Expresión reescrita con operaciones booleanas basicas  
      """)

# Simplificación
print("""
      Simplificación de la expresion a través de leyes booleanas:
      
R = (A'+BC+B'C')(BD)'+(A'+BC+B'C')'BD                     →    Expresión
R = (A'+BC+B'C')(B'+D')+(A'+BC+B'C')'BD                   →    De Morgan
R = (A'+BC+B'C')B'+(A'+BC+B'C')D'+(A'+BC+B'C')'BD         →    Distributiva
R = A'B'+BCB'+B'C'B'+A'D'+BCD'+B'C'D'+(A'+BC+B'C')'BD     →    Distributiva
R = A'B'+0+B'C'+A'D'+BCD'+B'C'D'+(A'+BC+B'C')'BD          →    Inversos: (BB'=0)
R = A'B'+B'C'+A'D'+BCD'+B'C'D'+(A'+BC+B'C')'BD            →    Identidades
R = A'B'+B'C'+A'D'+BCD'+(A'+BC+B'C')'BD                   →    Absorción:(B'C'+B'C'D'=B'C')
R = A'B'+B'C'+A'D'+BCD'+(A')'(BC)'(B'C')'BD               →    De Morgan
R = A'B'+B'C'+A'D'+BCD'+A(B'+C')(B+C)BD                   →    De Morgan
R = A'B'+B'C'+A'D'+BCD'+AB(B'+C')(B+C)D                   →    Conmutativa
R = A'B'+B'C'+A'D'+BCD'+A(BB'+BC')(B+C)D                  →    Distributiva
R = A'B'+B'C'+A'D'+BCD'+A(0+BC')(B+C)D                    →    Inversos
R = A'B'+B'C'+A'D'+BCD'+ABC'(B+C)D                        →    Identidades
R = A'B'+B'C'+A'D'+BCD'+(ABC'B+ABC'C)D                    →    Distributiva
R = A'B'+B'C'+A'D'+BCD'+(ABC'+0)D                         →    Inversos: (CC'=0)
R = A'B'+B'C'+A'D'+BCD'+ABC'D                             →    Identidades
R = A'B'+B'C'+A'D'+BCD'+ABC'D                             →    Expresión simplificada
      
      """)

