# Matrizes com list comprehension

listas = [[1,2,3],[4,5,6],[7,8,9]]

# Printando os dados

# for lista in listas:
#     for num in lista:
#         print(num)

[[print(num) for num in lista] for lista in listas]


# Manipulando os dados

# for lista in range(3):
#     for num in range(3):
#         listas[lista][num] *= 2
# print(listas)

dobro = [[num*2 for num in lista] for lista in listas]
print(dobro)


# Gerando uma matriz 3X3

# matriz = []
# for m in range(1,4):
#     linha = []
#     for n in range(1,4):
#         linha.append((m,n))
#     print(linha)
#     matriz.append(linha)

matriz = [[(m,n) for n in range(1,4)] for m in range(1,4)]
[print(lista) for lista in matriz]