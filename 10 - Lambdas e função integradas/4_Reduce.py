""" A função reduce() recebe uma função de 2 parâmetros e um iterável.
    Ela funciona da seguinte forma:
    - Aplica a função nos dois primeiros itens do iterável.
    - Posteriormente, aplica a função usando o resultado da aplicação anterior com o próximo item do iterável.
    - Ela repete esse processo até chegar ao final no iterável.
"""

from functools import reduce

dados = [3, 5, 6, 9, 5, 4, 12, 17]

multi = lambda x, y: x * y

res = reduce(multi, dados)
print(res)

""" Obs: a função reduce foi retirada da built-in do python a partir da versão 3.0, justamente por ser facilmente 
substituída por um loop for. """

res = 1
for n in dados:
    res *= n

print(res)