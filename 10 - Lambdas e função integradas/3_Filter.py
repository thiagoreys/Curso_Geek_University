# Serve para filtrar dados de uma determinada coleção.

import statistics

dados = [0.3, 0.5, 0.6, 0.9, 3.2, 4.3, 2.1]

media = statistics.mean(dados)  # Média Aritmética
# print(media)

res = filter(lambda x: x > media, dados) # (função, iterável)
# Se o dado satisfazer a condição, será retornado.
# print(list(res)) # Dados filtrados.

# print(list(res)) # Os valores tbm são zerados, após serem retornados.


# Removendo dados faltantes

paises = ['Brasil','Colômbia','Chile','','','Equador','','Venezuela','Argentina','']
res = filter(None, paises)
# print(list(res))


# Filtrando usuários inativos

users = [{'username': 'Samuelx', 'tweets': ['Hj o rolê vai ser louco', 'Fé no pai que o inimigo cai']},
         {'username': 'Emanuelly', 'tweets': ['To tiste', 'Que saudade dele', 'Supeeera negah']},
         {'username': 'Jorge123', 'tweets': []},
         {'username': 'Bobf1', 'tweets': ['Só queria que sexta chegasse logo', 'O pai ta on']},
         {'username': 'Matheus5', 'tweets': []},
         {'username': 'LucasFrancs', 'tweets': ['Hj vai dar mengooo!']}]

# inativos = list(filter(lambda user: user['tweets'] == [], users))
inativos = list(filter(lambda user: not user['tweets'], users))
# print(*inativos, sep='\n')


# Combinando map() com filter()

alunos = [('Jorge', 7.5), ('Matheus', 8.7), ('Lucas', 4.2), ('Guilherme', 5), ('Maria', 6.5), ('Pedro', 7) ]

aprovados = list(map(lambda aluno: f'{aluno[0]} passou.', filter(lambda aluno: aluno[1] >= 7, alunos)))
# Observe que filter() está dentro de map() e está retornando para map() apenas os alunos que passaram.
print(*aprovados, sep='\n')





