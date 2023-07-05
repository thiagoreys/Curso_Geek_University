# -------------- Preservando Metadatas com Wraps ---------------- #
# Metadatas (metadados): dados intrísecos em arquivos.
# Wraps: faz com que os dados intrísecos da função original sejam preservados.

from functools import wraps

def ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        '''Eu sou uma função decoradora.'''
        print(f'Você está chamando: {funcao.__name__}')
        print(f'Aqui está a documentação: {funcao.__doc__}')
        return funcao(*args,**kwargs)
    return logar

@ver_log
def soma(a, b):
    '''Soma dois números'''
    return a + b

# print(soma(10,30))
print(soma.__name__)  # Agora os dados foram preservados
print(soma.__doc__)