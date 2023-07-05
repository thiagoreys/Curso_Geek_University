# Funções de Maior Grandeza - Higher Order Functions (HOF)
# Quando uma linguagem de programação suporta HOF, significa que podemos ter funções que retornam outras funções
# e/ou recebem funções como parâmetro. Além de poder atribuir estas funções à variáveis.

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def calcular(num1, num2, funcao):
    return funcao(num1, num2)

# print(calcular(9, 3, somar))
# print(calcular(9, 3, subtrair))
# print(calcular(9, 3, multiplicar))
# print(calcular(9, 3, dividir))


# Funções Aninhadas
from random import choice

# retornando a função já executada
def cumprimento(pessoa):
    def humor():
        return choice(('Eai ', 'Suma daqui ', 'Gostei de você '))
    return humor() + pessoa

# print(cumprimento('Marcos'))
# print(cumprimento('Alexandre'))
# print(cumprimento('Maria'))
# print(cumprimento('Geovane'))

# Retornando a função não executada
def gerador_de_risos():
    def risada():
        return choice(('kkkkkkkkkkk','hahahahahahah','hehehehehe'))
    return risada

rindo = gerador_de_risos()
print(rindo())

# Exemplo mais complexo
def rindo_com_alguem(pessoa):
    def dando_risada():
        risada = choice(('kkkkkkkkkkk','hahahahahahah','hehehehehe'))
        return f'{risada} {pessoa}'
    return dando_risada

rindo = rindo_com_alguem('Natália')
print(rindo())

