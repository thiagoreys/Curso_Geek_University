# ------- Convertendo tipos de dados com decoradores --------- #

def forca_tipo(*tipos):
    def decorador(funcao):
        def converte(*args, **kwargs):
            novo_args = []
            for (valor, tipo) in zip(args, tipos):
                novo_args.append(tipo(valor))
            return funcao(*novo_args, **kwargs)
        return converte
    return decorador

@forca_tipo(str, int)  # Determinando os tipos de dados que será recebido pela função
def repete_msg(msg, vezes):
    for vez in range(vezes):
        print(msg)

repete_msg('Geek', '3')

@forca_tipo(float,float)
def dividir(a,b):
    print(a/b)

dividir('1',5)

# Observe que quando os dados não são dos tipos requisitados, eles são convertidos para tais tipos.