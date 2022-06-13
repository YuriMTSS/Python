"""Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:
1 , 2, 3, 4  - Votos para os respectivos candidatos 
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco
Faça um programa que calcule e mostre:
O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;
A percentagem de votos nulos sobre o total de votos;
A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero."""
possiveis_votos = [1, 2, 3, 4, 5, 6]
candidatos = ["Ciro Gomes", "Bolsonaro Genocida", "João Amoeba", "Lula Molusco", "Nulo", "Branco"]
votos = []

print("1 - Ciro Gomes")
print("2 - Bolsonaro Genocida")
print("3 - João Amoeba")
print("4 - Lula Molusco")
print("5 - Nulo")
print("6 - Branco")

voto = True
n_votos = 1
while voto != 0:
    print("Voto n°", n_votos)
    voto = int(input("Digite o seu voto ou informe 0 para sair: "))
    if voto == 0:
        break
    else:
        while voto not in possiveis_votos:
            print("[Voto invalido.]")
            voto = int(input("Digite o seu voto: "))
        votos.append(voto)
    n_votos += 1

contador = 0

for i in range(len(candidatos)):
    print("Votos para ", candidatos[contador], end=": ")
    if votos.count == 0:
        print("0")
        contador += 1
    else:
        print(votos.count(contador + 1))
        contador += 1

porcentagem_nulo = (votos.count(5) / len(votos)) * 100
porcentagem_branco = (votos.count(6) / len(votos)) * 100
print("\nPorcentagem Nulos: ", porcentagem_nulo, "%\nPorcentagem Brancos: ",porcentagem_branco,"%")