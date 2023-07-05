# Polimorfismo - Muitas formas
# Acontece quando os métodos são sobrescritos nas subclasses, assumindo assim formas diferentes.


class Animal:

    def __init__(self, nome):
        self.nome = nome
    
    def falar(self):
        raise NotImplementedError('Este método precisa ser implementadado por uma subclasse.')
    
    def comer(self):
        print(self.nome, 'está comendo.')


class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(self.nome, 'está latindo.')


class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)
    
    def falar(self):
        print(self.nome, 'está miando.')


class Tigre(Animal):

    def __init__(self, nome):
        super().__init__(nome)
    
    def falar(self):
        print(self.nome, 'está rugindo.')



cachorro = Cachorro('Caramelo')
gato = Gato('Felix')
tigre = Tigre('Jorge')

gato.falar()
cachorro.falar()
tigre.falar()

print()

gato.comer()
cachorro.comer()
tigre.comer()