# Para escrevermos em um arquivo devemos abri-lo com o modo 'w' no open().
# Depois, utilizamos a função .write() para a escrita.
# Se o arquivo não existir, será criado.
# Se o arquivo já existir, será substituído.


# Exemplo 1:
# with open('13 - Leitura e Escrita em arquivos\\Texto.txt', 'w', encoding="utf8", ) as arquivo:
#     arquivo.write('Tudo o que for digitado aqui será escrito no arquivo.\n' )
#     arquivo.write('Tudo o que for digitado aqui será escrito no arquivo.\n' )
#     arquivo.write('Tudo o que for digitado aqui será escrito no arquivo.\n' )


# Exemplo 2:
# with open('13 - Leitura e Escrita em arquivos\\Texto.txt', 'w', encoding="utf8", ) as arquivo:
#     arquivo.write(input('Digite o que deseja colocar no arquivo: '))


# Exemplo 3:
with open('13 - Leitura e Escrita em arquivos\\Lista de Compras.txt', 'w', encoding="utf8", ) as arquivo:
    print('LISTA DE COMPRAS')
    while True:
        item = input("Digite o próximo ítem ou 's' para sair: ").capitalize()
        if item != 'S':
            arquivo.write(item + '\n')
        else:
            break
