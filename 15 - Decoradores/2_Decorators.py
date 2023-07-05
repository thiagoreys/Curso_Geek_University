# ----------------- Decorators (Decoradores) ---------------------
# São funções que aprimoram comportamento de outras funções (HOF).
# Possuem uma sintaxe própria usando o '@' (Syntact Sugar). 

# Função decoradora - sem o Syntact Sugar (Não recomendado).
def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer você.')
        funcao()
        print('Tenha um ótimo dia.')
    return sendo

# Funções para serem decoradas
def saudacao():
    print('Seja muito bem vindo à Geek University.')

def raiva():
    print('EU TE ODEIO!')


# saudacao()  # Função comum
saudacao_decorada = seja_educado(saudacao)  # Decorando a função
# saudacao_decorada()  # Função decorada

# raiva()  # Função comum
raiva_educada = seja_educado(raiva)  # Decorando a função
# raiva_educada() # Função decorada


# Função Decoradora com Syntact Sugar (Recomendado).
def seja_educado_mesmo(funcao):
    def sendo_educado():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um excelente dia!')
    return sendo_educado

@seja_educado_mesmo  # Decorando a função
def apresentando():
    print('Meu nome é Pedro.')

@seja_educado_mesmo  # Decorando a função
def ir_embora():
    print('Agora eu preciso ir, tenho um compromisso.')


# apresentando()  # Função decorada
# ir_embora()  # Função decorada

# Obs: Veja que a função não precisa ser adcionada à uma variável, ela já é decorada diretamente.
# Basicamente, o Syntact Sugar faz com que a função comum seja adcionada à função decoradora.