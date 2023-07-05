# Reversed() é usado para inverter a ordem de qualquer iterável.
# Ele retorna um List Reverser Iterator.
# O retorno pode ser convertido para qualquer iterável.

algarismos = list(range(10))
# print(algarismos)
# print(reversed(algarismos))
# print(list(reversed(algarismos)))

# Reversed() em strings
nome = 'Thiago dos Reis André'

# for letra in reversed(nome):
#     print(letra,end='')

# print(''.join(list(reversed(nome))))

# Porém, é bem mais fácil usar o fatiamento de iteráveis.
print(nome[::-1])
print(algarismos[::-1])