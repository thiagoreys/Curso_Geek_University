# Consulte a tabela no site para ver os outros modos de abertura de arquivo:
# https://docs.python.org/pt-br/3/library/functions.html#open

# 'x' -> Cria o arquivo para a escrita somente se ele não existir.
# with open('13 - Leitura e Escrita em arquivos\\Texto.txt', 'x', encoding="utf8", ) as arquivo:
#     arquivo.write(input('Digite o que deseja colocar no arquivo: '))

# 'a' -> Abre o arquivo para escrita, adicionando o texto no final caso já exista.
with open('13 - Leitura e Escrita em arquivos\\Texto.txt', 'a', encoding="utf8", ) as arquivo:
    arquivo.write('Tudo o que for digitado aqui será adicionado no final do arquivo.\n')

# '+' -> É utilizado como complemento de um modo, para realizar leitura e escrita do mesmo arquivo.
with open('13 - Leitura e Escrita em arquivos\\Texto.txt', 'a+', encoding="utf8", ) as arquivo:
    arquivo.write('Finalização do arquivo.\n')
    arquivo.seek(0)
    print(arquivo.read())