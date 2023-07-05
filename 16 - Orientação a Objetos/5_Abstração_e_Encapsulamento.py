# Abstração e Encapsulamento são métodos utilizados para facilitar o uso de uma classe,
# mostrando ao usuário apenas dados relevantes.

class Conta:
    contador = 400
    def __init__(self, titular, saldo, limite):
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__conta = Conta.contador + 1
        Conta.contador = self.__conta

    def extrato(self):
        print(f'Titular: {self.__titular}')
        print(f'Conta: {self.__conta}')
        print(f'Saldo: R$ {self.__saldo}')
        print(f'Limite: R$ {self.__limite}')
        print()

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('O valor de depósito precisa ser positivo.')

    def sacar(self, valor):
        if valor > 0:
            if valor <= self.__saldo:
                self.__saldo -= valor
            else:
                print('Saldo insuficiente.')
        else:
            print('O valor de saque precisa ser positivo.')

    def transferir(self, valor, destinatario):
        self.__saldo -= valor
        destinatario.__saldo += valor


conta1 = Conta('João Batista', 300, 1000)
conta1.depositar(100)
conta1.sacar(50)
conta1.extrato()

conta2 = Conta('Maria José', 500, 1200)
conta2.transferir(100, conta1)
conta2.extrato()
conta1.extrato()