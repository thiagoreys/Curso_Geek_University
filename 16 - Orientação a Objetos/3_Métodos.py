# Métodos são funções dentro da classe.
# Os métodos podem ser classificados como de instância ou de classe.


class Produto:
    cod = 1000
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        self.cod = Produto.cod + 1
        Produto.cod = self.cod
    
    # Método de instância
    def desconto(self, porcentagem):
        """Retorna o valor do produto com desconto."""
        return self.preco * (100 - porcentagem) / 100


p1 = Produto('Playstation 4', 3000)
print(p1.desconto(10))


class ContaCorrente:
    conta = 5000
    def __init__(self, limite, saldo):
        self.numero = ContaCorrente.conta + 1
        self.limite = limite
        self.saldo = saldo
        ContaCorrente.conta = self.numero

    @classmethod  # Método de classe
    def n_usuarios(cls):
        print(f'Temos {cls.conta - 5000} usuário(s) cadastrados(s).')


user1 = ContaCorrente(3000, 1500)
user2 = ContaCorrente(1500, 600)
user3 = ContaCorrente(5000, 2500)

ContaCorrente.n_usuarios()

# Em síntese, usamos métodos de instância quando o método usa atributos de instância, 
# e métodos de classe quando o método usa apenas atributos de classe.


# Também podemos fazer métodos privados:
class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        print(f'Cadastro Bem-sucedido. Seu nome de usuário é: {self.__gera_usuario()}')

    # Método Privado
    def __gera_usuario(self):
        return self.email.split('@')[0]


user = Usuario('Julio Fernando', 'juliofer123@gmail.com')
# print(user.__gera_usuario)  # Só pode ser acessado dentro da classe

