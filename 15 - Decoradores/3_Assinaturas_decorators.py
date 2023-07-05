# Decorators com diferentes assinaturas

def gritar(funcao):
    def caps_lock(*args, **kwargs):
        return funcao(*args,**kwargs).upper()
    return caps_lock

@gritar
def saudacao(nome):
    return f'Olá, eu sou o(a) {nome}.'

@gritar
def ordernar(principal, acompanhamento):
    return f'Eu gostaria de um(a) {principal} com {acompanhamento}.'


print(saudacao('Angelina'))
print(ordernar('Picanha', 'Batata Frita'))



# Por baixo dos panos:
# Na verdade a função decorada se torna o retorno da função decoradora, com a função comum já embutida.
print(saudacao.__name__)
print(ordernar.__name__)
