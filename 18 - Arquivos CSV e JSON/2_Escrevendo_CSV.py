# Escrevendo em Arquivos CSV

from csv import writer   # Com listas

# with open('18 - Arquivos CSV e JSON\\filmes.csv', 'w', encoding='utf8') as arquivo:
#     escritor_csv = writer(arquivo)  # abrindo o arquivo para a escrita
#     escritor_csv.writerow(['Título', 'Gênero', 'Duração'])  # escrevendo em uma linha
#     while True:
#         opcao = input('Deseja adcionar um filme [S/N]? ')
#         if opcao.upper() == 'S':
#             titulo = input('Informe o nome do filme: ')
#             genero = input('Informe o gênero do filme: ')
#             duracao = input('Informe a duração do filme (em minutos): ')
#             escritor_csv.writerow([titulo, genero, duracao])
#         else:
#             break


from csv import DictWriter   # Com dicionários

with open('18 - Arquivos CSV e JSON\\filmes.csv', 'w', encoding='utf8') as arquivo:
    cabecalho = ['Título', 'Gênero', 'Duração']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)  # abrindo o arquivo para a escrita com cabecalho
    escritor_csv.writeheader()  # escrevendo o cabecalho
    while True:
        opcao = input('Deseja adcionar um filme [S/N]? ')
        if opcao.upper() == 'S':
            titulo = input('Informe o nome do filme: ')
            genero = input('Informe o gênero do filme: ')
            duracao = input('Informe a duração do filme (em minutos): ')
            escritor_csv.writerow({'Título':titulo, 'Gênero':genero, 'Duração':duracao})
        else:
            break