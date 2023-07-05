# Pickle -  Serialização de objetos Python
# https://docs.python.org/pt-br/3/library/pickle.html

import pickle

class Animal:

    def __init__(self, nome):
        self.nome = nome
    
    def comer(self):
        print(f'{self.nome} está comendo...')


class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)
    
    def miar(self):
        print('Miau Miau!')


class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)
    
    def latir(self):
        print('Au Au Au!')


gato = Gato('Fred')
cachorro = Cachorro('Sansão')

# Criando arquivo pickle
with open('18 - Arquivos CSV e JSON\\animais.pickle', 'wb') as arquivo:
    pickle.dump((gato,cachorro), arquivo)

# Lendo arquivo pickle
with open('18 - Arquivos CSV e JSON\\animais.pickle', 'rb') as arquivo:
    gato, cachorro = pickle.load(arquivo)
    print(f'O gato se chama {gato.nome}.')
    gato.miar()
    print(f'O cachorro chama-se {cachorro.nome}')
    cachorro.latir()