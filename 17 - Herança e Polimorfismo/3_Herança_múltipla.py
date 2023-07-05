# Henrança múltipla: quando uma classe herda de mais de uma classe.
# Pode ser feita de duas maneiras:
# - Multiderivação direta
# - Multiderivação indireta


# Multideravação Direta

class Base1:
    ...

class Base2:
    ...

class Base3:
    ...

class Multiderivada(Base1, Base2, Base3):
    ...


# Multideravação Indireta

class Base1:
    ...

class Base2(Base1):
    ...

class Base3(Base2):
    ...

class Multiderivada(Base3):
    ...

# A classe Multiderivada herda da Base3, que herda da Base2, que herda da Base1.
# Em síntese, a Multirivada está herdando das 3 classes acima.
# Apesar de ser mais complexo, o efeito é o mesmo para a Multideravada.


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


salmao = Aquatico('Salomão')
salmao.cumprimentar()
salmao.nadar()

print()

cavalo = Terrestre('Fred')
cavalo.cumprimentar()
cavalo.andar()

print()

pinguin = Pinguin('Escalompas')
pinguin.cumprimentar()
pinguin.andar()
pinguin.nadar()