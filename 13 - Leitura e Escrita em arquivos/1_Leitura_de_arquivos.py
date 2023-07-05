# Para lermos um arquivo utilizamos a função open().
# https://docs.python.org/pt-br/3/library/functions.html#open

# Exemplo:
arquivo = open('13 - Leitura e Escrita em arquivos\\Texto.txt', encoding="utf8")  # Atribuindo o arquivo a uma variável
print(arquivo.read())  # Lendo o arquivo

# O python usa um 'cursor' ao trabalhar com arquivos de texto.
# Depois de ler um arquivo pela primeira vez, o curso vai para o final do arquivo.
print(arquivo.read())
# Ao tentar ler o arquivo de novo, o python tentará ler o arquivo pelo final (de onde o cursor parou), 
# portando, não aparecerá nada.

