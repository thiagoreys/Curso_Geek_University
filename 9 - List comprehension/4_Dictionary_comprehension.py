# Estrutura geral: {chave: retorno for itens in iterável}

#Exemplos:
# {chave: valor for chave, valor in dicionario.items}

numeros = {'a': 1,'b': 2,'c': 3, 'd': 4, 'e': 5}
quadrados = {chave : valor ** 2 for chave, valor in numeros.items()}
print(quadrados)

# {chave: valor for valor in iterável}

numeros = [1,2,3,4,5]
quadrados = {valor: valor ** 2 for valor in numeros}
print(quadrados)

# {chaves[i]: valores[i] for i in interável}

chaves = 'abcde'
valores = [1,2,3,4,5]
mistura = {chaves[i]: valores[i] for i in range(len(chaves))}
print(mistura)

# {chave: (retorno if condição else retorno) for valor in iterável}

par_ou_impar = {num: ('par' if num % 2 == 0 else 'impar') for num in range(11)}
print(par_ou_impar)