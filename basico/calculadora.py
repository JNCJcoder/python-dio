class Calculadora:
    def __init__(self, numero1, numero2):
        self.a = numero1
        self.b = numero2
    
    def soma(self):
        return self.a + self.b

    def subtracao(self):
        return self.a - self.b

    def multiplicacao(self):
        return self.a * self.b

    def divisao(self):
        return self.a / self.b

calculadora = Calculadora(10, 2)