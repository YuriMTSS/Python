""" 
Criar um algoritmo em PORTUGOL que leia o destino do passageiro, se a viagem
inclui retorno e informar o preço da passagem conforme a tabela a seguir:
Região Norte R$ 500,00 R$ 900,00
Região Nordeste R$ 350,00 R$ 650,00
Região Centro-Oeste R$ 350,00 R$ 600,00
Região Sul R$ 300,00 R$ 550,00  
"""
opcao = int(input("Informe a opcao da viagem: "))
volta = bool(input())

if volta:
    if opcao == 1:
        preco = 900
    elif opcao == 2:
        preco = 650
    elif opcao == 3:
        preco = 600
    elif opcao == 4:
        preco = 550
    else:
        print("Opcao invalida")
else:
    if opcao == 2:
        preco = 500
    elif opcao == 2:
        preco = 350
    elif opcao == 3:
        preco = 350
    elif opcao == 4:
        preco = 300
    else:
        print("Opcao invalida")
