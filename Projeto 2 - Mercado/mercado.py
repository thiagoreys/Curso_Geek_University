from typing import List, Dict
from time import sleep

from models.produto import Produto
from utils.helper import valor_em_reais

produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []


def menu():
    print()
    print(' Supermecado Cosmos '.center(40,'='))
    print('\nSelecione uma opção abaixo:')
    print('1 - Cadastrar produto.')
    print('2 - Listar produtos cadastrados.')
    print('3 - Comprar produto.')
    print('4 - Mostrar carrinho de compras.')
    print('5 - Fechar pedido.')
    print('6 - Sair do sistema.\n')
    
    opcao = int(input('Nº da opção: '))

    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produtos()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        vizualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print('Programa finalizado.')
        sleep(1)
        exit()
    else:
        print('Opção inválida.')
        sleep(1)
        menu()


def cadastrar_produto():
    print('-'*40)
    print('Cadastro de Produto'.center(40))
    print('-'*40)
    nome = input('Nome: ').capitalize()
    preco = float(input('Preço: '))
    produto = Produto(nome, preco)
    produtos.append(produto)
    print(f'O produto {produto.nome} foi cadastrado com sucesso!')
    sleep(1)
    menu()

def listar_produtos():
    if len(produtos) > 0:
        print('-'*40)
        print('Produtos Cadastrados'.center(40))
        print('-'*40)
        for produto in produtos:
            print(produto)
            print('-'*40)
    else:
        print('Ainda não existe produtos cadastrados.')
    sleep(1)
    menu()
    
def comprar_produto():
    if len(produtos) > 0:
        codigo = int(input(('Código do produto: ')))
        produto = pega_produto_por_codigo(codigo)
        if produto:
            if len(carrinho) > 0:
                for item in carrinho:
                    for produto_carrinho in item:
                        if produto_carrinho == produto:
                            item[produto] += 1
                            print(f'Mais um {produto.nome} foi adcionado ao carrinho.')
                            sleep(1)
                            menu()
                        else:
                            item = {produto: 1}
                            carrinho.append(item)
                            print(f'O produto {produto.nome} foi adcionado ao carrinho.')
                            sleep(1)
                            menu()
            else:
                item = {produto: 1}
                carrinho.append(item)
                print(f'O produto {produto.nome} foi adcionado ao carrinho.')
                sleep(1)
                menu()
    else:
        print('Ainda não existe produtos cadastrados.')
    sleep(1)
    menu()

def vizualizar_carrinho():
    if len(carrinho) > 0:
        print('-'*40)
        print('Carrinho de Compras'.center(40))
        print('-'*40)
        for item in carrinho:
            for produto, qtd in item.items():
                print(produto)
                print('Quantidade:', qtd)
            print('-'*40)
    else:
        print('Nenhum produto foi adcionado ao carrinho.')
    sleep(1)
    menu()

def fechar_pedido():
    if len(carrinho) > 0:
        print('-'*40)
        print('Finalização de Pedido'.center(40))
        print('-'*40)
        valor_total = 0
        for item in carrinho:
            for produto, qtd in item.items():
                print(produto)
                print(f'Quantidade: {qtd}')
                valor_total += produto.preco * qtd
                print('-'*40)
        sleep(1)
        print(f'Total a pagar: {valor_em_reais(valor_total)}')
        print('-'*40)
        sleep(3)
        print(f'Obrigado pela preferência. Volte sempre!')
        carrinho.clear()

    else:
        print('Você precisa adcionar produtos ao carrinho, para fechar o pedido.')
        sleep(2)
        menu()
      
def pega_produto_por_codigo(codigo):
    for produto in produtos:
        if produto.codigo == codigo:
            return produto
    print('Código não cadastrado.')


if __name__ == '__main__':
    menu()