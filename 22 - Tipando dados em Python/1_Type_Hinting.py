# Type Hinting: tipagem estática em python.
# Basicamente, é um método para descrever os dados de entrada e saída de uma função.

def cumprimentar(nome: str) -> str:
    return f'Olá, {nome}'

print(cumprimentar('Thiago Reis'))


def cabecalho(txt: str, caractere: str = '=', completar: int = 50) -> str:
    return f' {txt.title()} '.center(completar, caractere)
    
print(cabecalho('Cosmos University'))
print(cabecalho('Cosmos University', '*', 60))
print(cabecalho.__annotations__)


class Pessoa:
    def __init__(self, nome: str, idade: int, peso: float) -> None:
        self.nome = nome
        self.idade = idade
        self.peso = peso

print(Pessoa.__init__.__annotations__)
joao = Pessoa('João', 35, 85.3)
print(joao.__dict__)


# Também pode ser utilizado diretamente em variáveis

nome: str = 'Thiago Reis'
idade: int = 25
solteiro: bool = True


# Obs: O python é uma linguagem de tipagem fraca, na impede que outros tipos de dados sejam adcionados.
# Como mencionado anteriormente, esté é um método de descrição. Ou seja, serve apenas para indicar ao 
# usuário quais tipos de dados devem ser adcionados às variáveis e funções.