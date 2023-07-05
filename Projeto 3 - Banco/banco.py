from typing import List
from time import sleep

from models.cliente import Cliente
from models.conta import Conta

contas: List[Conta] = []


def menu():
    print(' Universe Bank '.center(40,'='), '\n')
    print('1 - Criar conta')
    print('2 - Efetuar saque')
    print('3 - Efetuar depósito')
    print('4 - Efetuar transferência')
    print('5 - Listas contas')
    print('6 - Sair do sistema')

    opcao = int(input('\nEscolha uma opção no menu: '))

    if opcao == 1:
        criar_conta()
    elif opcao == 2:
        efetuar_saque()
    elif opcao == 3:
        efetuar_deposito()
    elif opcao == 4:
        efetuar_transferencia()
    elif opcao == 5:
        listar_contas()
    elif opcao == 6:
        print('Sistema finalizado.')
        exit()
    else:
        print('Opcão inválida.')
        sleep(1)
        menu()


def criar_conta():
    print('Informe os dados do cliente.')
    nome = input('Nome: ')
    email = input('E-mail: ')
    cpf = input('CPF: ')
    data_nascimento = input('Data de nascimento (dia/mês/ano): ')

    cliente = Cliente(nome, email, cpf, data_nascimento)
    conta = Conta(cliente)
    contas.append(conta)

    print('Conta criada com sucesso.')
    print(' Dados da conta '.center(40,'-'))
    print(conta)
    print('-'*40)
    
    sleep(3)
    menu()


def efetuar_saque():
    if contas:
        numero = int(input('Número da conta do saque: '))
        conta = buscar_conta_por_num(numero)
        if conta:
            valor = float(input('Valor do saque: '))
            conta.sacar(valor)
        else:
            print('A conta não foi encontrada.')
    else:
        print('Ainda não existem contas cadastradas.')
    sleep(2)
    menu()


def efetuar_deposito():
    if contas:
        numero = int(input('Número da conta do depósito: '))
        conta = buscar_conta_por_num(numero)
        if conta:
            valor = float(input('Valor do depósito: '))
            conta.depositar(valor)
        else:
            print('A conta não foi encontrada.')
    else:
        print('Ainda não existem contas cadastradas.')
    sleep(2)
    menu()


def efetuar_transferencia():
    if contas:
        num_rementente = int(input('Numero da conta rementente: '))
        conta_rementente = buscar_conta_por_num(num_rementente)
        if conta_rementente:
            num_destino = int(input('Numero da conta destino: '))
            conta_destino = buscar_conta_por_num(num_destino)
            if conta_destino:
                valor = float(input('Valor da transferência: '))
                conta_rementente.transferir(conta_destino, valor)
            else:
                print('A conta não foi encontrada.')
        else:
            print('A conta não foi encontrada.')
    else:
        print('Ainda não existem contas cadastradas.')
    sleep(2)
    menu()
    

def listar_contas():
    if contas:
        print(' Contas Cadastradas '.center(40,'-'))
        for conta in contas:
            print(conta)
            print('-'*40)
    else:
        print('Ainda não existem contas cadastradas.')
    sleep(2)
    menu()


def buscar_conta_por_num(num):
    c = None
    if contas:
        for conta in contas:
            if conta.numero == num:
                c = conta
    return c


if __name__ == '__main__':
    menu()