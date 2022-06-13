class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
    
    def TrocarCor(self):
        troca = input("Trocar a cor atual {}? [s/n]".format(self.cor))
        troca = troca[0].lower()

        if troca == 's':
            nova_cor = input("Nova cor: ")
            self.cor = nova_cor
        else:
            print("Ok! A cor continua {}.".format(self.cor))
    
    def MostrarCor(self):
        print("A cor atual é {}.".format(self.cor))

def main():
    Bola1 = Bola("Azul", 5, "Metal")

    while True:
        Bola1.MostrarCor()
        Bola1.TrocarCor()

        continuar = input("Continuar? [s/n]")
        continuar = continuar[0].lower()

        if continuar == 'n':
            break
    
    Bola1.MostrarCor()

main()