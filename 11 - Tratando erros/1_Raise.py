# raise -> lançamento de erros. 
# Modo de usar: 
# raise TipoDoErro('Mensagem do Erro')
# O raise funciona de forma parecida com o return, ao ser executado a função é finalizada.

def printcolorido(msg='Sem Mensagem',cor='branco'):

  if type(msg) != str:
    raise TypeError('A mensagem precisa ser uma string.')
  cor = cor.lower()
  cores = ('cinza', 'vermelho', 'verde', 'amarelo', 'azul', 'rosa', 'ciano', 'branco')
  if cor not in cores:
    raise ValueError(f'Cor digitada inválida, só temos: {cores}')
  
  if cor == 'cinza':
    print(f'\033[30m{msg}\033[0m')
  if cor == 'vermelho':
    print(f'\033[31m{msg}\033[0m')
  if cor == 'verde':
    print(f'\033[32m{msg}\033[0m')
  if cor == 'amarelo':
    print(f'\033[33m{msg}\033[0m')
  if cor == 'azul':
    print(f'\033[34m{msg}\033[0m')
  if cor == 'rosa':
    print(f'\033[35m{msg}\033[0m')
  if cor == 'ciano':
    print(f'\033[36m{msg}\033[0m')
  if cor == 'branco':
    print({msg})


printcolorido('Olá Python', 'Ciano')
# printcolorido('Bem-vindo','Azul Royal')
printcolorido(1, 'Vermelho')