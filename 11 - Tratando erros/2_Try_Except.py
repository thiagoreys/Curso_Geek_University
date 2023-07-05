# Forma Genérica
try:
    len(5)  
except:
    print('Erro.')


# Especificando os erros

# Exemplo 1 - Mensagem de erro.

try:
    len(5)
except TypeError:
    print('O valor não é um iterável.')


# Exemplo 2 - Mostrando o erro.

try:
    # hello()
    # len(3)
    len()
except NameError as erro:
    print(f'NameError: {erro}')
except TypeError as erro:
    print(f'TypeError: {erro}')
except:
    print('Erro desconhecido.')


# Exemplo 3 - Dentro de funções.

def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None

clientes = {'Fernando': 32, 'Carla': 25, 'Jorge': 43}

print(pega_valor(clientes, 'Fernando'))
print(pega_valor(clientes, 'Amanda'))
