# With é um bloco utilizado para facilitar o trabalho com arquivos em python.
# A sua principal vantagem é que o arquivo é fechado automaticamente após o trabalho.

with open('13 - Leitura e Escrita em arquivos\\Texto.txt', encoding="utf8") as arquivo:
    print(arquivo.readlines())

# Ao finalizar o bloco, o arquivo é fechado.
print(arquivo.closed)
