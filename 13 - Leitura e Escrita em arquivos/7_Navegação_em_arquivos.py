# Comandos no terminal:
# cd .. -> diretório acima (anterior)
# cd . -> diretório local

# Utilizando o módulo 'os', podemos fazer a manipulação de arquivos pelo python.
import os

os.chdir('c:\\Users\\Thiago Reis\\Documents')  # Alterar diretório atual
print(os.getcwd())  # Mostrar diretório atual

# Verificar se o diretório é absoluto
print(os.path.isabs('C:\\Users\\Thiago Reis\\Documents\\Programação\\Curso Geek University'))

# Juntando diretórios
print(os.path.join(os.getcwd(), 'Geek'))

# Listando os diretórios e arquivos
print(os.listdir())
print(os.listdir('C:\\Users\\Thiago Reis\\Documents\\Programação\\Curso Geek University'))


import sys

print(sys.platform) # Mostrar plataforma