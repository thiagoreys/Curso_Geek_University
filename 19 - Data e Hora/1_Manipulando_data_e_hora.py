# https://docs.python.org/pt-br/3/library/datetime.html

import datetime

# Data e hora atual
print(datetime.datetime.now())

# Alterando data-hora
inicio = datetime.datetime.now()
fim = inicio.replace(year=2025, month=6, day=5, hour=17, minute=0, second=0, microsecond=0)  
print(fim)

# Criando data-hora
evento = datetime.datetime(2023, 5, 11, 20)
print(evento)

# Transformando str em datetime
nascimento = input('Digite sua data de nascimento (dia/mês/ano): ')
nascimento = nascimento.split('/')
nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))
print(nascimento)

# Acessando os elementos datetime
print(inicio.year)
print(inicio.month)
print(inicio.day)
print(inicio.hour)
print(inicio.minute)
print(inicio.second)
print(inicio.microsecond)