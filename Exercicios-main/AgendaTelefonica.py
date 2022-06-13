# Agenda eletronica em Python.              #
lista = [] #define uma variavel para a lista
#le os dados do arquivo e joga pra lista
arq2 = open("agenda.csv","a+")
lista = arq2.readlines()
arq2.close()

# Apresenta o menu
def menu():
    print ("""AGENDA ELETRONICA\n
          Escolha a opção: \n
             (1) Inserir contato:\n
             (2) Deletar:\n
             (3) Mostrar agenda:\n
             (4) finalizar programa:\n""")
#função: lista_agenda, adiciona, remove e mostra a lista
    
def lista_agenda(nome, data, opc):
    if(opc == 1):
        contato = nome + ": " + data + "\n" #concatenao nome e data
        lista.append(contato)
        lista.sort() #ordena a lista por prioridade, o que tiver encima tem prioridade maior

    elif(opc == 2):
        if (lista == []): #se lista for vazia
            print("Lista Vazia\n")
        else:
            lista.pop(0)#remove o elemento de maior prioridade, ou seja, indice 0 da lista
            print("Removido o elemento de maior prioridade")

    elif(opc == 3):
        if (lista == []):
            print("Lista vazia!\n")
        else:
            print("Nome:|Data:\n")
            for i in lista:
                print(i)

    elif (opc == 4):
        arq = open("agenda.csv","w") #escreve por cima do arquivo antigo (atualiza lista)
        tam = len(lista) #recebe o tamanho da lista
        #for que insere os valores no arquivo separado por ';' sendo nome = indice par e data = impar

        for i in range(tam):
            arq.write(lista[i])

        arq.close()

#funcao principal
opc = 0 #variavel pro menu
while (opc != 4 ):
    menu() #chama o menu
    while True:
        try:
            opc = int(input('')) #recebe a opção
            break
        except:
            print("Digite só numeros válidos")

    if (opc == 1 ):
        print("Informe o nome do contato: ")
        nome = input('')

        print("informe a data de nascimento: [DD/MM/AAAA]")
        data = input('')

        lista_agenda(nome, data, 1) #chama a função para inserir na lista

    elif (opc == 2):
        lista_agenda(0,0,2) #chama a função para deletar o nome na lista

    elif (opc == 3): #chama a função para mostrar na tela
        print("Lista de contatos: ")
        lista_agenda(0,0,3)
                
lista_agenda(0,0,4) #grava a lista na agenda
print("FIM DO PROGRAMA!")
