"""
Programa deverá ler o nome, idade e sexo de 4 pessoas
No final mostrar:
    A média de idade de grupo
    Qual o nome do homem mais velho
    Quantas mulheres tem menos de 20 anos
"""

class analise_grupo:
    def __init__(self):
        self.soma_idades = 0
        self.media_idades = 0
        self.maior_idade_homem = 0
        self.nome_velho = ''
        self.mulheres_menor_20 = 0

    def Iniciar(self):
        for i in range (1,5):
            print('-------{}º PESSOA -------'.format(i))
            nome = str(input('Nome: ')).strip()
            idade = int(input('Idade: '))
            sexo = str(input('Sexo [M/F]: ')).strip()
            
            # Calcular média das idades
            self.soma_idades += idade

            # Verificar o homem com maior idade
            if i == 1 and sexo in 'Mm':
                self.nome_velho = nome
                self.maior_idade_homem = idade
            else:
                if idade > self.maior_idade_homem and sexo in 'Mm':
                    self.nome_velho = nome
                    self.maior_idade_homem = idade

            # Verificar mulheres com idade menor que 20
            if idade < 20 and sexo in 'Ff':
                self.mulheres_menor_20 += 1

        
        self.media_idades = self.soma_idades / 4
        print('A média de idade do grupo é de: {}'.format(self.media_idades))
        print('O Homem com a maior idade é {} com {} anos.'.format(self.nome_velho, self.maior_idade_homem))
        print('O total de mulheres com idade menor que 20 é {}.'.format(self.mulheres_menor_20))

analise = analise_grupo()
analise.Iniciar()
