from models.cliente import Cliente
from models.conta import Conta

cliente1 = Cliente('Marcos Antonio','marcosantonio@gmail.com','123.123.123-09','10/07/2001')
cliente2 = Cliente('Jorge Matheus','jorgematheus@gmail.com','123.456.789-00','02/05/1992')

print(cliente1)
print(cliente2)

conta1 = Conta(cliente1)
conta2 = Conta(cliente2)

print(conta1)
print(conta2)