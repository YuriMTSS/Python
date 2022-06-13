# Jogo de decisões onde tenho que criar vários finais diferentes baseados nas respostas

# Qual o cenário: estou em uma guerra e entra 2 nações e temos 2 lados: LadoA e LadoB
# O LadoA ira vencer, o LadoB ira perder
# Preciso tomar as decisões corretas para o LadoA vencer

class Jogo_Avantura:
    def __init__(self):
        # A opção da esquerda será o LadoA e o da direita o LadoB como no exemplo
        self.pergunta_1 = 'Você nasceu no Norte ou no Sul? (n/s)' # Norte = LadoA, Sul = LadoB
        self.pergunta_2 = 'Você prefere a espada ou o escudo? (espada/escudo)' 
        self.pergunta_3 = 'Sua especialidade é linha de frente ou tática? (linha/tatica)'
        self.historia_1 = 'Você será o heroi da linha de frente!'
        self.historia_2 = 'Você será um héroi protegendo nossas tropas!'
        self.historia_3 = 'Você vai se sacrificar na batalha!' 
        self.historia_4 = 'Você não é capaz de lutar nessa batalha!'

    def Iniciar(self):
        resposta_1 = input(self.pergunta_1)
        if resposta_1 == 'n':
            resposta_1B = input(self.pergunta_2)
            if resposta_1B == 'espada':
                print(self.historia_1)
            if resposta_1B == 'escudo':
                print(self.historia_2)
        if resposta_1 == 's':
            resposta_1B = input(self.pergunta_3)
            if resposta_1B == 'linha':
                print(self.historia_3)
            if resposta_1B == 'tatico':
                print(self.historia_4)
        


jogar = Jogo_Avantura()
jogar.Iniciar()