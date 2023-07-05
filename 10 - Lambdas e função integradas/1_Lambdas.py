# São funções sem nome, que possuem apenas declaração e retorno.
# Geralmente são atribuidas a variáveis, para que possam ser utilizadas.


# Função comum
# def bem_vindo(nome):
#     return f'Olá {nome.capitalize()}, seja bem-vindo!'
# print(bem_vindo('Thiago'))

# Função lambda
bem_vindo = lambda nome: f'Olá {nome}, seja bem-vindo!'
# print(bem_vindo('Thiago'))


# Elas podem ter nenhuma ou muitas entradas

python = lambda: print('Bem-vindo ao mundo Python!')
# python()

exponenciação = lambda x, n: print(x ** n)
# exponenciação(2,3)


# Usando lambdas em funções

autores = ['Isaac Asimov', 'Carl Sagan', 'Stephen Hawking', 'Clóvis de Barros Filho', 'Arthur C. Clarke', 'H. G. Wells' ]

autores.sort(key=lambda nome: nome.split(' ')[-1])  # Ordenando autores pelo sobrenome
# print(autores)


# Lambda como retorno de função

def gerar_função_quadratica(a,b,c):
    return lambda x: a*x**2 + b*x + c

funcao_quadratica = gerar_função_quadratica(3,4,5) # definindo o valor de a, b e c

# Definindo o valor de x
print(funcao_quadratica(3))
print(funcao_quadratica(5))
print(funcao_quadratica(0))


