# {retorno for valor in iterável}

num = {num for num in range(10)}
print(num)

# {retorno for valor in iterável if condição}

pares = {n for n in num if n % 2 == 0}
impares = {n for n in num if n % 2 != 0}
print(pares)
print(impares)

# {retorno if condição else retorno for valor in iterável}

res = {n*2 if n % 2 == 0 else n*3 for n in num}
print(res)

# Com strings

vogais = {letra for letra in 'Thiago dos Reis Andre'.lower() if letra in 'aeiou' }
print(vogais)