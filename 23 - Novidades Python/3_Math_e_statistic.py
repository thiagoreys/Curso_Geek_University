import math

num = [3,5,7,9]
print(math.prod(num))  # Produto dos números da lista

print(math.sqrt(10))  # Raiz quadrada comum
print(math.isqrt(10))  # Parte inteira da raiz quadrada

print(math.dist([3,2], [1,2]))   # Distância entre 2 pontos 2D
print(math.dist([3,2,0], [1,2,3]))   # Distância entre 2 pontos 3D

print(math.hypot(3,4))  # Retorna a hipotenusa
print(math.hypot(3,4,5))  # Módulo do vetor

import statistics

print(statistics.mean([1,2,3,4,5]))  # Média simples
print(statistics.geometric_mean([1,2,3,4,5]))  # Média geométrica

print(statistics.multimode([2,3,4,5,7,3,2,3,9]))  # Moda (valor mais frequente)
print(statistics.multimode('ThiagodosReisAndre'.lower()))  # Quando há empate, todos são exibidos