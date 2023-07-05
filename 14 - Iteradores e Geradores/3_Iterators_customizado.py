# Criando a função range(a,b)

class Contador:
    def __init__(self, menor, maior):
        self.menor = menor
        self.maior = maior
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.menor < self.maior:
            n = self.menor
            self.menor += 1
            return n
        raise StopIteration
    

for n in Contador(1,51):
    print(n)

# for n in range(1,51):
#     print(n)