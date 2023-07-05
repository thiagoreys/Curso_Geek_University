# @property faz com que os atributos privados sejam acessados fora da classe.
# @.setter faz com que se possa manipular os atributos privados fora da classe.
# Obs: O setter deve ser sempre usado em conjunto com o property, colocando-o após o mesmo.

class Conta:
    contador = 400
    def __init__(self, titular, saldo, limite):
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__conta = Conta.contador + 1
        Conta.contador = self.__conta

    @property
    def titular(self):
        return self.__titular
    
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    @property
    def conta(self):
        return self.__conta

    def extrato(self):
        print(f'Titular: {self.__titular}')
        print(f'Conta: {self.__conta}')
        print(f'Saldo: R$ {self.__saldo}')
        print(f'Limite: R$ {self.__limite}')
        print()

    def depositar(self, valor):
        self.__saldo += abs(valor)

    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= abs(valor)
        else:
            print('Saldo insuficiente.')

    def transferir(self, valor, destinatario):
        if valor <= self.__saldo:
            self.__saldo -= valor
            destinatario.__saldo += valor
        else:
            print('Saldo insuficiente.')

    @property
    def valor_total(self):
        return self.__saldo + self.__limite



conta1 = Conta('João Batista', 500, 1000)
conta2 = Conta('Maria José', 850, 1500)

soma = conta1.saldo + conta2.saldo
print(f'A soma dos saldos das contas é {soma}.')

conta1.limite = 1200
conta1.extrato()

print(f'O cliente {conta1.titular} tem um total de R$ {conta1.valor_total} para usar.')