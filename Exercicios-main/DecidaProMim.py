# Faça uma pergunta para o programa te dar uma resposta

import random

class Decida_Por_Mim:
    def __init__(self):
        self.respostas = [
            'Com certeza, você deve fazer isso!',
            'Não sei, você que sabe!',
            'Não faz isso não!',
            'Acho que ta na hora certa!',
            'Eu te ajudo se quiser!',
            'Vamos matar aula!',
            'O povo é bem burro ein!'
        ]
    
    def Iniciar(self):
        input('Faça sua pergunta: ')
        print(random.choice(self.respostas))

faca = Decida_Por_Mim()
faca.Iniciar()