from random import randint

class Operacoes:
    def __init__ (self, dificuldade: int) -> None: 
        '''1 - Fácil; 2 - Moderado; 3 - Difícil; 4 - Expert'''
        self.dificuldade = dificuldade
        self.valor1 = self.gerar_valor
        self.valor2 = self.gerar_valor
        self.operacao = randint(1, 3)  # 1 Somar, 2 Diminuir, 3 Multiplicar
        self.resultado = self.gerar_resultado

    def __str__(self) -> str:
        op = ''
        if self.operacao == 1:
            op = 'somar'
        if self.operacao == 2:
            op = 'subtrair'
        if self.operacao == 3:
            op = 'multiplicar'
        return f'Valor 1: {self.valor1} \nValor 2: {self.valor2} \nDificuldade: {self.dificuldade} \nOperação: {op}'


    @property
    def gerar_valor(self) -> int:
        if self.dificuldade == 1:
            return randint(0,10)
        elif self.dificuldade == 2:
            return randint(0,100)
        elif self.dificuldade == 3:
            return randint(0,1000)
        elif self.dificuldade == 4:
            return randint(0,10000)
        else:
            return randint(0,1000000)

    @property
    def gerar_resultado(self) -> int:
        if self.operacao == 1:
            return self.valor1 + self.valor2
        if self.operacao == 2:
            return self.valor1 - self.valor2
        if self.operacao == 3:
            return self.valor1 * self.valor2
   
    @property
    def mostrar_operacao(self) -> str:
        if self.operacao == 1:
            return f'{self.valor1} + {self.valor2}'
        if self.operacao == 2:
            return f'{self.valor1} - {self.valor2}'
        if self.operacao == 3:
            return f'{self.valor1} * {self.valor2}'
 
    @property
    def pontos_dificuldade(self) -> int:
        if self.dificuldade == 1:
            return 1
        elif self.dificuldade == 2:
            return 5
        elif self.dificuldade == 3:
            return 10
        elif self.dificuldade == 4:
            return 15
        else:
            return 20


    def checar_resultado(self, resposta) -> bool:
        if self.resultado == resposta:
            print('Resposta correta!')
            return True
        else:
            print('Resposta errada!')
            print(f'{self.mostrar_operacao} = {self.resultado}')
            return False