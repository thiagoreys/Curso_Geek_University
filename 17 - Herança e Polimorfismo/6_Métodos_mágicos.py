#               Métodos Mágicos                #
# São todos os métodos que utilizam dunder(____).


class Livros:

    def __init__(self, titulo, autor, ano, paginas):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.paginas = paginas

    # Soberescrevendo Métodos Mágicos:

    def __repr__(self):  # Representação do objeto
        return f'{self.titulo} - {self.autor}.'
    
    def __str__(self):  # Representação do objeto (preferencial)
        return f'{self.titulo} - {self.autor} ({self.ano}).'
    
    def __len__(self):  # Tamanho do objeto.
        return self.paginas   # retorna somente números inteiros
    
    def __add__(self, outro):  # Soma de objetos.
        return self.paginas + outro.paginas


livro1 = Livros('Memórias Póstumas de Brás Cubas', 'Machado de Assis', 1881, 320)
livro2 = Livros('Breves Respostas para Grandes Questões', 'Stephen Hawking', 2018, 254)

# __repr__
print(repr(livro1))
print(repr(livro2))

# __str__
print(livro1)
print(livro2)

# __len__
print(len(livro1))
print(len(livro2))

# __add__
print(livro1 + livro2)