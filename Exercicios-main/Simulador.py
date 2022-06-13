# Simular o lançamento de um dado nos valores de 1 a 6
import random
# import PySimpleGui

class Simulador_dados:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de continuar? [s,n]\n'

    def Iniciar(self):
    # Layout
        """ 
        layout = [
            [sg.Text("Jogar o dado?")],
            [sg.Button("Sim"), sg.Button("Não")]
        ]"""
        # Criar uma janela
        """self.janela = sg.Window('Simulador de dados', Layout = layout)"""
        # Ler os valores
        """self.eventos, self.valores = janela.Read()"""
        # Fazer alguma coisa com esses valores
        while True:
            resposta = input(self.mensagem)
            try:
                # if self.eventos in 'Sn': "Onde houver "resposta substitui por 'self.eventos'""
                if resposta in "Ss":
                    self.Gerar_Valor()
                elif resposta in "Nn":
                    print("Obrigado por usar o programa!")
                    break
                else:
                    print("Ocorreu um erro na sua resposta")
            except:
                print("Digite s ou n como resposta! Informe s ou n!")

    def Gerar_Valor(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))

simulador = Simulador_dados()
simulador.Iniciar()

