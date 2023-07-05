# O sorted() não altera a lista original, como o sort(), ele apenas retorna uma lista ordenada.
# Obs: não importa qual tipo de iterável que o sorted() receba, ele sempre vai retornar uma lista.
# Porém, o resultado pode ser convertido para qualquer iterável.

numeros = (4,1,6,8,2,3,1)
ordenado = sorted(numeros)
# print(numeros)
# print(ordenado)
# print(set(ordenado))

# Revertendo a ordem
# print(sorted(numeros, reverse=True))

# Trabalhando com dados mais complexos
users = [{'username': 'Samuelx', 'tweets': ['Hj o rolê vai ser louco', 'Fé no pai que o inimigo cai']},
         {'username': 'Emanuelly', 'tweets': ['To tiste', 'Que saudade dele', 'Supeeera negah']},
         {'username': 'Jorge123', 'tweets': []},
         {'username': 'Bobf1', 'tweets': ['Só queria que sexta chegasse logo', 'O pai ta on']},
         {'username': 'Matheus5', 'tweets': []},
         {'username': 'LucasFrancs', 'tweets': ['Hj vai dar mengooo!']}]

ord_por_username = sorted(users, key=lambda user: user['username'])
# print(*ord_por_username, sep='\n')

ord_por_atividade = sorted(users, reverse=True, key=lambda user: len(user['tweets']))
print(*ord_por_atividade, sep='\n')