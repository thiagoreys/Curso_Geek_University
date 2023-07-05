from models.operacoes import Operacoes


def jogar(pontos):
    print('Informe o nível de dificuldade desejado: (1 - Fácil, 2 - Médio, 3 - Difícil, 4 - Expert) ')
    dificuldade = int(input())
    jogo = Operacoes(dificuldade)

    print('\nInforme o resultado para a seguinte operação:')
    resultado = int(input(f'{jogo.mostrar_operacao} = '))

    if jogo.checar_resultado(resultado):
        pontos += jogo.pontos_dificuldade
    else:
        pontos -= jogo.pontos_dificuldade
    print(f'\nAgora você tem {pontos} ponto(s).')
    
    continuar = int(input('Deseja continuar no jogo? (1 - Sim, 0 - Não)\n'))

    if continuar:
        jogar(pontos)
    else:
        print(f'Você finalizou com {pontos} ponto(s).')


pontos = 0
if __name__ == '__main__':
    jogar(pontos)