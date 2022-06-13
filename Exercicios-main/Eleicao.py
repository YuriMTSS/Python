""" Numa eleição existem três candidatos. 
Faça um programa que peça o número total de eleitores. 
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato. """

total_eleitores = int(input("Total de eleitores: "))
PT = 0 #13
PDT = 0 #15
PSDB = 0 #45

for _ in range(total_eleitores):
    opcao = int(input("Escolha uma opção:\n13 - PT\n15 - PDT\n45 - PSDB \n"))

    if opcao == 13:
        PT += 1
    elif opcao == 15:
        PDT += 1
    else:
        PSDB += 1
print("PT: ", PT)
print("PDT: ", PDT)
print("PSDB: ", PSDB)




