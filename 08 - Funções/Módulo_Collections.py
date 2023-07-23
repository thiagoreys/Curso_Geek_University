"""
# Módulo Coletions
https://docs.python.org/pt-br/3/library/collections.html#module-collections

Counter:

# Exemplo 1

# Podemos utilizar qualquer iterável
lista = [1,2,4,1,3,4,7,8,9,5,2,6,7,8,3,7,8,3,2,1,3,5,1,6,1]

res = Counter(lista)
print(type(res))
print(res) # Quantas vzs aparece cada elemento.

# Exemplo 2

print(Counter('Geek University'))

# Exemplo 3

texto = '''Um algoritmo nada mais é que uma sequência de instruções ou comandos realizados de forma sistemática 
com a finalidade de resolver um problema ou executar uma determinada tarefa. Ou seja, é criado para resolver 
“problemas”, com instruções bastante simples e exatas.'''

palavras = texto.split()

print(Counter(palavras)) # Quantas vzs cada palavra aparece no texto.

"""

from collections import Counter

texto = '''Um algoritmo nada mais é que uma sequência de instruções ou comandos realizados de forma sistemática 
com a finalidade de resolver um problema ou executar uma determinada tarefa. Ou seja, é criado para resolver 
“problemas”, com instruções bastante simples e exatas.'''

palavras = texto.split()

print(Counter(palavras))   # Quantas vzs cada palavra aparece no texto.
print(Counter(palavras).most_common(5))  # 5 palavras que mais aparecem no texto.
