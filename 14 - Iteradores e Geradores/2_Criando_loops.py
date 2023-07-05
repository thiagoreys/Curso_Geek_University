lista = [1,2,3,4,5]

# Versão pythônica
# for n in lista:
#     print(n)

# Versão raiz
def for_print(iteravel):
    it = iter(iteravel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break

for_print(lista)
