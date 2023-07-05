# Operações com datetime
# https://docs.python.org/pt-br/3/library/datetime.html

import datetime

# Subtração
data_hoje = datetime.datetime.now()
aniversario = datetime.datetime(2024,5,6)
delta = aniversario - data_hoje
print(delta)
print(f'Faltam {delta.days} dias para o seu aniversário.')

# Soma
data_compra = datetime.datetime.now()
dias = datetime.timedelta(days=3)
venc_boleto = data_compra + dias
print(f'Você tem até o dia {venc_boleto.day} desse mês, para pagar o boleto.')
