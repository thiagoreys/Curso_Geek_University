# Herança é um método utilizado para aproveitar código ou extender classes.
# Ela faz com que atributos e métodos sejam herdados entre classes.

class Pessoa:  # SuperClass
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'   

class Cliente(Pessoa):   # Cliente herda de Pessoa
    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)   # Acessando o bloco construtor da SuperClass
        self.__renda = renda
    
class Funcionario(Pessoa):   # Funcionario herda de Pessoa
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

    # Sobescrita de Métodos (Overriding)
    def nome_completo(self):
        return f'Funcionário: {self.__matricula} Nome: {self._Pessoa__nome} {self._Pessoa__sobrenome}'


cliente1 = Cliente('Jorge','Silva','126 472 78 70',5000)
funcionario1 = Funcionario('Sthephany', 'Moreira', '543 564 865 62', 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())

# print(cliente1.__dict__)
# print(funcionario1.__dict__)


