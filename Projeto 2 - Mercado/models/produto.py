from utils.helper import valor_em_reais

class Produto:
    contator = 1

    def __init__(self, nome, preco):
        self.codigo = Produto.contator
        self.nome = nome
        self.preco = preco
        Produto.contator += 1
    
    def __str__(self):
        return f'Produto: {str(self.nome)} \nCód: {str(self.codigo)} \nPreço: {valor_em_reais(self.preco)}'