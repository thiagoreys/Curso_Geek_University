# Generators são objetos usados para trabalhar com quantidade de dados muito grandes, pois são econômicos em memória.

import sys

gen = (n for n in range(10000))
print(gen)
lista = [n for n in range(10000)]

print(sys.getsizeof(gen))  # Tamanho em bytes
print(sys.getsizeof(lista))

# print(lista)
# print(list(gen))  # A memória só é usada no momento da execução.
# print(list(gen))  # Depois de usado uma vez, os dados são apagados da memória.

# for n in gen:  # Também podemos iterar em generators.
#     print(n)