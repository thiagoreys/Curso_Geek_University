"""
all() -> retorna True se todos os elementos do iterável forem True ou se estiver vazio.
"""

# print(all([1,2,3,4,5]))
# print(all([]))
# print(all([0,0,0,0]))
# print(all([0,1,2,3]))

# Forma mais digna de usar:
nomes = ['Carlos', 'Cássio', 'Carla', 'Cassiano', 'Cristina']

# Todos os nomes da lista começam com a letra C?
print(all(nome[0] == 'C' for nome in nomes))

numeros = [2,4,6,7,8,10]

# Todos os numeros da lista são pares?
print(all(num % 2 == 0 for num in numeros))

"""
any() -> retorna True se algum dos elementos do iterável for True, se estiver vazio retorna False.
"""

# Existe algum nome na lista que começa com a letra A?
print(any(nome[0] == 'A' for nome in nomes))

# Existe algum numero impar na lista?
print(any(num % 2 != 0 for num in numeros))