"""
Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:
Código da cidade; Número de veículos de passeio (em 1999); Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
Qual a média de veículos nas cinco cidades juntas;
Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.
"""
menor = 0
maior = 0
count = 0
soma_veiculos = 0
soma_acidentes = 0
soma_2k = 0
cid_menor = " "
cid_maior = " "

for c in range (1,4):
    cidade = str(input("Nome da cidade: "))
    codigo = int(input("Código da cidade: "))
    veiculos = int(input("Número do veiculo de passeio: "))
    acidentes = int(input("Números de acidentes: "))

    soma_veiculos += veiculos
    soma_acidentes += acidentes

    if acidentes > maior:
        maior = acidentes
        cid_maior = cidade
    if acidentes < menor or c == 1:
        menor = acidentes
        cid_menor = cidade
    if veiculos < 2000:
        soma_2k += acidentes
        count += 1

media_5_cidades = soma_veiculos / c
media_2k = soma_2k / count
print()
print("O menor indice de incidentes foi de ", menor, " na cidade de ", cid_menor)
print("O maior indice de incidentes foi de ", maior, " na cidade de ", cid_maior)
print("Média de veículos nas 5 cidades ", media_5_cidades)
print("Média de acidentes de trânsito nas cidades com menos de 2000 é ", media_2k)
