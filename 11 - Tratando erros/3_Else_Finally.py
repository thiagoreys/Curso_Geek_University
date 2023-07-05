# Try, Except, Else e Finally


try:
    n = int(input('Digite um número inteiro: '))
except ValueError:
    print('Você não digitou um número inteiro.')
else:
    print(f'Você digitou o número {n}.')  # Negação do except (só é executado se o except não for executado).
finally:
    print('Volte sempre.')   # O finally sempre é executado.


# Em funções

def dividir (a, b):
    try:
        return float(a) / float(b)
    except ValueError:
        return 'Erro: Você não digitou números em algarismo arábicos.'
    except ZeroDivisionError:
        return 'Não é possível dividir um número por zero.'
    
n1 = input('Digite o primeiro número (dividendo): ')
n2 = input('Digite o segundo número (divisor): ')

print(dividir(n1,n2))
