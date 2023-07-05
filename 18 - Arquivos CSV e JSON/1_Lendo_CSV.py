# CSV: Comma-Separated Values (Valores Separados por Virgula)
# Apesar do nome, os valores podem ser separados por qualquer caratectere, inclusive o espaço.

# Módulos para se trabalhar com arquivos CSV:
# - reader: permite que iteremos sobre as linhas do arquivo como listas.
# - DictReader: permite que iteremos sobre as linhas como um OrderedDict.


from csv import reader

with open('18 - Arquivos CSV e JSON\\lutadores.csv', encoding='utf8') as arquivo:
    leitor_csv = reader(arquivo, delimiter=',')  # Gerando um iterator
    next(leitor_csv)  # Pulando o cabeçalho
    for linha in leitor_csv:  # Cada linha é uma lista
        print(f'{linha[0]} nasceu no(a) {linha[1]} e mede {linha[2]} cm.')

print()

from csv import DictReader

with open('18 - Arquivos CSV e JSON\\lutadores.csv', encoding='utf8') as arquivo:
    leitor_csv = DictReader(arquivo, delimiter=',')  # Gerando um iterator
    for linha in leitor_csv:  # Cada linha é um OrderedDict
        print(f"{linha['Nome']} nasceu no(a) {linha['País']} e mede {linha['Altura (cm)']} cm.")