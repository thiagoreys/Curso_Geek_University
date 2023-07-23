from models.cliente import Cliente
from utils.helper import float_para_RS
from time import sleep

class Conta:
    c = 1001
    def __init__(self, cliente: Cliente) -> None:
        self.__numero = Conta.c
        self.__cliente = cliente
        self.__saldo = 0.0
        self.__limite = 100
        Conta.c += 1

    @property
    def numero(self) -> int:
        return self.__numero

    @property
    def cliente(self) -> object:
        return self.__cliente

    @property
    def saldo(self) -> float:
        return self.__saldo

    @saldo.setter
    def saldo(self, valor: float) -> None:
        self.__saldo = valor

    @property
    def limite(self) -> float:
        return self.__limite
  
    @limite.setter
    def limite(self, valor: float) -> None:
        self.__limite = valor

    def __str__(self) -> str:
        return f'Conta: {self.numero} \nCliente: {self.cliente.nome} \nSaldo: {float_para_RS(self.saldo)} \nLimite: {float_para_RS(self.limite)}'


    def depositar(self, valor: float) -> None:
        if valor > 0:
            self.saldo += valor
            print('Depósito efetuado com sucesso.')
        else:
            print('Valor de depósito inválido.')
    

    def sacar(self, valor: float) -> None:
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                print(f'Sacando {float_para_RS(valor)} da sua conta.')
            else:
                if valor <= (self.saldo + self.limite):
                    restante = self.saldo - valor
                    self.saldo = 0
                    self.limite += restante 
                    print(f'Sacando {float_para_RS(valor)} da sua conta.')
                    print('Obs: O valor solicitado ultrapassa o seu saldo, portanto, completamos o valor do saque com o seu limite.')
                else:
                    print('Saque não realizado.')
                    print('Você não possui saldo e nem limite suficiente para o valor solicitado.')
        else:
            print('Valor inválido.')


    def transferir(self, destino: object, valor: float) -> None:
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                destino.saldo += valor
                print(f'Transferindo {float_para_RS(valor)} para a conta do(a) {destino.numero}.')
                sleep(1)
                print(f'Transferência realizada com sucesso.')
            else:
                if valor <= (self.saldo + self.limite):
                    restante = self.saldo - valor
                    self.saldo = 0
                    self.limite += restante
                    destino.saldo += valor
                    print('Obs: Você não possui saldo suficiente para a transferência, portanto, vamos completar o valor com o seu limite.')
                    print(f'Transferindo {float_para_RS(valor)} para a conta {destino.numero}.')
                    sleep(1)
                    print(f'Transferência realizada com sucesso.')
                else:
                    print('Transferência não realizada.')
                    print('Você não possui saldo e nem limite suficiente para o valor solicitado.')
        else:
            print('Valor inválido.')