# Estruturas condicionais em list comprehension

# Usando if
pares = [numero for numero in range(10) if numero % 2 == 0]
impares = [numero for numero in range(10) if numero % 2 != 0]

print(pares)
print(impares)

# Usando if e else
res = [f'{n} é par' if n % 2 == 0 else f'{n} é impar' for n in range(5)]
#     (retorno) if (condição) else (retorno) for (elemento) in (iterável)
print(res)