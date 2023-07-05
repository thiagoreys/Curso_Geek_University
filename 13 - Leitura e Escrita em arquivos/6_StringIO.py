# StringIO -> Utilizado para ler e escrever arquivos em memória RAM.

from io import StringIO

msg = 'Esta é uma string qualquer.\n'

arquivo = StringIO(msg)
print(arquivo.read())

arquivo.write('Outra mensagem.\n')

arquivo.seek(0)
print(arquivo.read())