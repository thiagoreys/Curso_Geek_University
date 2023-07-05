import random

print(random.random())  # Gera um número aleatório entre 0 e 1.

print(random.uniform(1,7))  # Gera um número aleatório dentro de um intervalo estabelecido.

print(random.randint(1,10))  # Gera um número inteiro aleatório, dentro de um intervalo estabelecido.

print(random.choice([1,3,6,8,'cavalo',True,(),{},[]]))  # Escolhe um ítem aleatoriamente dentro de um iterável.

lista = [1,2,3,4,5,6,7,8,9]
random.shuffle(lista)   # Embaralha ítens de um iterável.
print(lista)