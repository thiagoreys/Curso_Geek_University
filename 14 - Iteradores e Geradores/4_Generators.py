"""
Generators
- São um tipo de iterators.
- Podem ser criados com Generator Fuctions.
- Também podem ser criados com Generator Expression (Aula 6, Seção 10).

Generator Fuctions
- Podem ter mais de um retorno (yield).
- Retornam Generators.

"""
# Exemplo de Generator Fuction
def conta_ate(valor_max):
    c = 1
    while c <= valor_max:
        yield c
        c += 1


# Exemplo de Generator
gen1 = conta_ate(5)
print(type(gen1))
print(next(gen1))
print(next(gen1))
for num in gen1:   # Vai começar de onde parou
    print(num)
print()

gen2 = conta_ate(10)
print(next(gen2))
print(list(gen2))   # O item já mostrado é removido do iterator