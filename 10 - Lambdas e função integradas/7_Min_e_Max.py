# max() -> Retorna o maior valor de um iterável ou de dois ou mais elementos.

tupla = (9,2,3,14,56,18,43,27)
# print(max(tupla))

lista = [9,2,3,14,56,18,43,27]
# print(max(lista))

conjunto = {9,2,3,14,56,18,43,27}
# print(max(conjunto))

dicionario = {'a':9, 'b':2, 'c':14, 'd':56, 'e':18, 'f':43, 'g':27}
# print(max(dicionario.values()))

n1, n2 = 43, 27
# print(max(n1,n2))

# min() -> Retorna o menor valor de um iterável ou de dois ou mais elementos.

tupla = (9,2,3,14,56,18,43,27)
# print(min(tupla))

lista = [9,2,3,14,56,18,43,27]
# print(min(lista))

conjunto = {9,2,3,14,56,18,43,27}
# print(min(conjunto))

dicionario = {'a':9, 'b':2, 'c':14, 'd':56, 'e':18, 'f':43, 'g':27}
# print(min(dicionario.values()))

n1, n2 = 43, 27
# print(min(n1,n2))


# Outras Aplicações

nomes = ['Alessando Massafera', 'José Carlos', 'Thiago dos Reis', 'Mario Sérgio Cortella']

# Maior nome
# print(max(nomes, key=lambda nome: len(nome)))  # for nome in nomes: return len(nome)
# Menor nome
# print(min(nomes, key=lambda nome: len(nome)))


musicas = [
{'título': 'Thunderstruck', 'tocou': 5},
{'título': 'Dead Skin Mask', 'tocou': 3},
{'título': 'Back in Black', 'tocou': 8},
{'título': 'Too old to Rock in Roll', 'tocou': 15},
]

# print(max(musicas, key=lambda musica: musica['tocou']))
# print(min(musicas, key=lambda musica: musica['tocou']))

# Imprimindo somento o título da música
print(max(musicas, key=lambda musica: musica['tocou'])['título'])
print(min(musicas, key=lambda musica: musica['tocou'])['título'])

# Método Tradicional
mais_tocada = musicas[0]
menos_tocada = musicas[0]
for musica in musicas:
    if musica['tocou'] > mais_tocada['tocou']:
        mais_tocada = musica
    if musica['tocou'] < menos_tocada['tocou']:
        menos_tocada = musica
print(mais_tocada['título'])
print(menos_tocada['título'])

# Agora observe a economia de linhas e variáveis que você ganha usando max() e min() com lambda.

