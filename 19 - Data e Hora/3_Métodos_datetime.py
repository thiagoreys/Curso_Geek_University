# Trabalhando com métodos em datetime
# https://docs.python.org/pt-br/3/library/datetime.html

from datetime import datetime, timedelta, timezone, time

# Trabalhando com fuso-horários: https://dayspedia.com/time-zone-map/-10800/
print(datetime.now(tz=timezone(timedelta(hours=1))))  # Londres
print(datetime.now(tz=timezone(timedelta(hours=-3))))  # Brasil
print(datetime.now(tz=timezone(timedelta(hours=9))))  # Japão
print(datetime.now(tz=timezone(timedelta(hours=-7))))  # EUA

# Manuntenção amanhã à meia-noite: combine(agora + 1 dia, meia-noite)
manutencao = datetime.combine(datetime.now() + timedelta(days=1), time())
print(manutencao)

# Dia da semanana
print(manutencao.weekday())  # dia da semana:  0 = Segunda; 1 = terça; ... 6 = domingo;
print(datetime(1998,5,6).weekday())  # Eu nasci em uma quarta-feira

# Formatando exibição data
hoje = datetime.now()
print(hoje.strftime('%d/%m/%Y'))  # Formato brasileiro

# Formatando recebimendo de data
nascimento = input('Informe sua data de nascimento (dia/mês/ano): ')
nascimento = datetime.strptime(nascimento, '%d/%m/%Y')
print(nascimento)

# Trabalhando somente com hora
almoco = time(12, 30, 0)
print(almoco)
