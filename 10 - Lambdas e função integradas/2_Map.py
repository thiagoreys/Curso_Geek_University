# Serve para mapear valores para uma função.

import math

def area_circulo(r):
    return math.pi * r ** 2

# print(area_circulo(2))
# print(area_circulo(5))

# Calculado a Área de Vários Circulos

raios = [2,3,4.5,9,3.5,7]

# Forma comum
areas = []
for r in raios:
    areas.append(area_circulo(r))
print(areas)

# Usando map
areas = map(area_circulo, raios)  # (função, iterável)
# Obs: as funções usadas no map, devem ser de apenas um parâmetro.
print(list(areas))

# Usando map com lambda
areas = map(lambda r: math.pi * r ** 2, raios)
print(list(areas))

print(list(areas))  # Os valores são zerados, após serem retornados uma vez.