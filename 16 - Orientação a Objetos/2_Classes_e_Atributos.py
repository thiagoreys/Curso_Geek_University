# Tipos de Atributos:
# Atributos de instância: características inviduais de cada objeto (__init__);
# Atributos de classe: características da classe do objeto;
# Atributo dinâmico: atributo gerado fora da classe do objeto (casos particulares).


class Lampada:
    # Atributos de instância:
    def __init__(self, watts, volts, preco):
        self.watts = watts
        self.volts = volts
        self.preco = preco
    
    # Atributos de classe:
    marca = 'Philips'
    fornecedor = 'Amazon'
    # Todos os objetos gerados por essa classe terão esses atributos.


led = Lampada(4.5, 220, 16.18)
# Atributo dinâmico
led.cor = 'Azul'
# Obs: O atributo dinâmico é exclusivo do objeto que o gerou, não tem nenhum vínculo com a classe.

# Acessando atributos de instância e dinâmicos:
print(led.__dict__)
print(led.watts)
print(led.volts)

# Acessando atributos de classe:
print(led.marca)  # pelo objeto
print(Lampada.fornecedor)  # pela classe


# Os atributos também podem ser privados, isto é, só podem ser acessados dentro da classe. 
# Usa-se '__' para privar o atributo:

class Usuario:
    def __init__(self, usuario, senha):
        self.__usuario = usuario
        self.__senha = senha

# Obs: No python, nada impede que o atributo privado seja acessado fora da classe, o '__' é apenas um convenção.
# Entretanto, o acesso é feito de forma diferente:

user = Usuario('Rogerinho','1234abcd')
print(user.__dict__)
print(user._Usuario__usuario)
print(user._Usuario__senha)