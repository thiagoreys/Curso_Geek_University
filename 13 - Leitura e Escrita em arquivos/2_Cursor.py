# Para movimentarmos o cursor dentro de um arquivo de texto, ulizamos a função Seek().

arquivo = open('13 - Leitura e Escrita em arquivos\\Texto.txt', encoding="utf8")
# print(arquivo.read())

# Para lermos o arquivo novamente, devemos movimentar o cursor para o início.
# arquivo.seek(0)
# print(arquivo.read())

# Também podemos limitar até onde queremos que o arquivo seja lido no read().
# arquivo.seek(0)
# print(arquivo.read(25))

# Podemos movimentar o curso para qualquer caractere do texto com o seek().
# arquivo.seek(15)
# print(arquivo.read())

# Também podemos ler o arquivo por linha.
# arquivo.seek(0)
# print(arquivo.readline())
# print(arquivo.readline())
# print(arquivo.readline())

# Como o retorno da função open() é uma string, podemos usar os mesmos métodos.
# print(arquivo.read().title())
# print(arquivo.read().split())

# Também podemos separar as linhas do arquivo em uma lista.
# print(arquivo.readlines())
# print(len(arquivo.readlines()))  # Mostrando a quantidade de linhas

# OBS: Quando abrimos um arquivo utilizando a função open(), é criado uma conexão entre o arquivo e o programa.
# Portanto, ao finalizar o trabalho com o arquivo é necessário fechá-lo.
# Para fecharmos utilizamos o close().
arquivo.close()

# Para verificarmos se o arquivo está aberto ou fechado, utilizamos o atributo closed.
print(arquivo.closed)