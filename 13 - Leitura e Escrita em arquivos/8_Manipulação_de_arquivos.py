import os

# Verificando se um arquivo ou diretório existe
print(os.path.exists('c:\\Users\\Thiago Reis\\Documents')) # Diretório absoluto
print(os.path.exists('c:\\Users\\Thiago Reis\\Documents\\Texto.txt'))
print(os.path.exists('8 - Funções'))  # Diretória atual

# Criando arquivos
open('13 - Leitura e Escrita em arquivos\\arquivo-criado.html','w').close() # Diretório relativo ao atual

# Criando diretórios
os.mkdir('13 - Leitura e Escrita em arquivos\\Nova pasta')

# Renomeando arquivos
os.rename('13 - Leitura e Escrita em arquivos\\arquivo-criado.html', 
          '13 - Leitura e Escrita em arquivos\\arquivo-renomeado.html')

# Renomeando pastas
os.rename('13 - Leitura e Escrita em arquivos\\Nova pasta', 
          '13 - Leitura e Escrita em arquivos\\Pasta renomeada')

# Apagando arquivos
os.remove('13 - Leitura e Escrita em arquivos\\arquivo-renomeado.html')

# Apagando diretórios vazios
os.rmdir('13 - Leitura e Escrita em arquivos\\Pasta renomeada')

import shutil
# Agando diretórios com arquivos
shutil.rmtree('13 - Leitura e Escrita em arquivos\\Pasta com arquivos')


# OBS: Os diretórios e arquivos são apagados permanentemente, isto é, eles não vão para a lixeira.