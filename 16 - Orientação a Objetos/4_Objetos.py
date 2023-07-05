class Lampada:
    # Atributos de instância:
    def __init__(self, watts, volts):
        self.watts = watts
        self.volts = volts
        self.ligada = False
    
    def check_lampada(self):
        if self.ligada:
            print('A lampada está ligada.')
        else:
            print('A lampada está desligada.')

    def ligar_desligar(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True
    

l1 = Lampada(10,220)
l2 = Lampada(5,110)

l1.ligar_desligar()
l2.ligar_desligar()

l1.check_lampada()
l2.check_lampada()

l1.ligar_desligar()
l2.ligar_desligar()

l1.check_lampada()
l2.check_lampada()