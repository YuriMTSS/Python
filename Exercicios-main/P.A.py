#class Progressao_Aritmetica:
 #   def __init__(self):
  #      self.primeiro = 'Primeiro termo: '
   #     self.razao = 'Razão: '
    
#    def Iniciar(self):
 #       primeiro = self.primeiro
  #      print(primeiro)
   #     razao = self.razao
    #    print(razao)

#        decimo = self.primeiro + (10 - 1) * self.razao
 #       for c in range(primeiro, decimo + razao, razao):
  #          print('{}'.format(c), end=' -> ')
   #     print('Acabou')

#pa = Progressao_Aritmetica()
#pa.Iniciar()



def gerador_PA():
    print('Gerador de PA')
    print('-='*10)
    primeiro = int(input('Primeiro termo: '))
    razao = int(input('Razão: '))
    termo = primeiro
    cont = 1
    total_termos = 0
    mais = 10

    while mais != 0:
        total_termos += mais
        while cont <= total_termos:
            print('{}->'.format(termo),end = '')
            termo += razao
            cont += 1

        mais = int(input('\nQuantos termos você quer mostrar a mais?\n '))
    print('Foram mostrados ao todo {} termos.'.format(total_termos))
    print('FIM')

gerador_PA()