# Trabalhando com JSON e Pickle

# É necessário instalar a biblioteca jsonpickle
# terminal: pip install jsonpickle

# Obs: Para esse código funcionar, este arquivo python precisa estar no diretório principal.

import jsonpickle

class Gato:

    def __init__(self, nome, raca):
        self.nome = nome
        self.raca = raca
    
    def miar(self):
        print('Miau Miau!')


felix = Gato('Felix', 'Vira-Lata')
ret = jsonpickle.encode(felix)
print(ret)

# Escrevendo arquivo jsonpickle
with open('felix.json', 'w') as arquivo:
    ret = jsonpickle.encode(felix)
    arquivo.write(ret)

# Lendo arquivo jsonpickle
with open('felix.json', 'r') as arquivo:
    conteudo = arquivo.read()
    ret = jsonpickle.decode(conteudo)
    print(ret)
    print(f'Olá, eu sou o {felix.nome} {felix.raca}.')
    felix.miar()