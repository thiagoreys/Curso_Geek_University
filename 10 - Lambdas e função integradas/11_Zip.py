# Zip -> Recebe iteráveis e junta seus elementos em tuplas (Zip Object).

lista1 = [1,2,3]
lista2 = [4,5,6,7]

ziplistas = zip(lista1,lista2)
# print(ziplistas)
print(list(ziplistas))  # O elemento sem par é deixado de fora
print(tuple(ziplistas))  # Após serem retornados uma vez, os valores são apagados.
print(dict(ziplistas))  # No dicionário, a 1ª lista será a chave e a 2ª o valor.

# Também podemos 'zipar' mais de 2 iteráveis.
tupla = ('a','b','c')
ziplistas = zip(lista1,lista2,tupla)
# print(set(ziplistas))


# Exemplo Mais Complexo

alunos = ['Maria', 'João', 'Lucas']
prova1 = [7.5, 8.3, 5]
prova2 = [9, 5.7, 8]
prova3 = [8, 7, 6.5]

notas = zip(prova1, prova2, prova3)
# print(list(notas))
medias = [round(sum(nota)/3, 2) for nota in notas]
# print(list(media))
boletim = zip(alunos, medias)
print(dict(boletim))