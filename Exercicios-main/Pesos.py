class peso:
    def __init__(self):
        self.maior = 0
        self.menor = 0

    def Iniciar(self):
        for i in range(1,6):
            peso = float(input('Informe o peso da pessoa {} em kg: '.format(i)))
            if i == 1:
                self.maior = peso
                self.menor = peso
            else:
                if peso > self.maior:
                    self.maior = peso
                if peso < self.menor:
                    self.menor = peso
        print('O maior peso foi {}kg.'.format(self.maior))
        print('O menor peso foi {}kg.'.format(self.menor))

peso = peso()
peso.Iniciar()