# O operador Walrus permite fazer atribuição e retorno em uma mesma expressão.
# Walrus -> :=


# Modo Clássico
nome = 'Thiago Reis'
print('Thiago Reis')

# Usando o Walrus
print(nome := 'Thiago Reis')


# Modo Clássico
cesta = []
fruta = input('Digite uma fruta: ')
while fruta != 'sair':
    cesta.append(fruta)
    fruta = input('Digite uma fruta: ')

# Modo Walrus
cesta = []
while (fruta := input('Digite uma fruta: ')) != 'sair':
    cesta.append(fruta)

