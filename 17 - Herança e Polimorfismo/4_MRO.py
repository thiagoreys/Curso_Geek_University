# Method Resolution Order (MRO)

class Animal:
    
    def __init__(self, nome):
        self.nome = nome

    def cumprimentar(self):
        print(f'Olá, eu sou o {self.nome}')


class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)
    
    def nadar(self):
        print(f'{self.nome} está nadando.')

    def cumprimentar(self):
        print(f'Eu sou o {self.nome} e vivo em ambientes aquáticos.')


class Terrestre(Animal):
    
    def __init__(self, nome):
        super().__init__(nome)
    
    def andar(self):
        print(f'{self.nome} está andando')
    
    def cumprimentar(self):
        print(f'Eu sou o {self.nome} e vivo em ambientes terrestres.')
    

class Pinguin(Terrestre, Aquatico):

    def __init__(self, nome):
        super().__init__(nome)

    def cumprimentar(self):
        print(f'Eu sou o {self.nome} e vivo em ambientes aquáticos e terrestres.')


print(Pinguin.__mro__)