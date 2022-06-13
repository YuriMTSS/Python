# Criar um algoritmo que gere um valor aleatorio e tentar ate o numero ser descoberto
import random

class Chute:
    def __init__(self):
        self.valor = 0
        self.minimo = 1
        self.maximo = 10

    def Gerar_Valor(self):
        self.valor_aleatorio = random.randint(self.minimo, self.maximo)
    
    def Pedir_Valor_Aleatorio(self):
        self.valor_chute = input('Chute um número: ')

    def Iniciar(self):
        self.Gerar_Valor()
        self.Pedir_Valor_Aleatorio()
        try:
            while True:
                if int(self.valor_chute) > self.valor_aleatorio:
                    print("Você errou, o numero é menor")
                    self.Pedir_Valor_Aleatorio()

                elif int(self.valor_chute) < self.valor_aleatorio:
                    print("Você errou, o numero é maior!")
                    self.Pedir_Valor_Aleatorio()
                if int(self.valor_chute) == self.valor_aleatorio:            
                    print("Você acertou, o valor é ", self.valor_aleatorio)
                    break
        except:
            print("Só é permitido números inteiros!")
            self.Iniciar()


chute = Chute()
chute.Iniciar()