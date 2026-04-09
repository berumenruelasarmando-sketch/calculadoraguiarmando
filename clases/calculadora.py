class Calculadora(object):
    def __init__(self,num1,num2):
        self.numero1= num1
        self.numero2= num2
        self.resultado=0
    
    def calcularSumar(self):
        self.resultado = self.numero1 + self.numero2