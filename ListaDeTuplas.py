# Objetivo: Utilizar ciclos for para iterar sobre una lista de tuplas.
# Instrucciones: Dada una lista de tuplas que contienen el nombre y la edad de varias personas, usa un ciclo for para imprimir un mensaje personalizado para cada persona.

personas = [ ("Daniela", 21) , ("Carlos", 24) , ("Amanda", 18) , ("Noa", 19)]
for nombre, edad in personas:
    print(f"Hola, soy {nombre} y tengo {edad} años.")
