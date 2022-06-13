"""Faça um programa que leia um número indeterminado de valores, correspondentes a notas, 
encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). 
Após esta entrada de dados, faça:
Mostre a quantidade de valores que foram lidos;
Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
Calcule e mostre a soma dos valores;
Calcule e mostre a média dos valores;
Calcule e mostre a quantidade de valores acima da média calculada;
Calcule e mostre a quantidade de valores abaixo de sete;
Encerre o programa com uma mensagem; """

notas = 0
notas_lidas = []
soma = 0
media = 0
valores_acima_media = 0
valores_abaixo_7 = 0


#Começando o loop
while notas != -1:
    notas = float(input("Informe uma nota ou -1 pra terminar: "))
    if notas != -1:
        notas_lidas.append(notas)

#Quantidade de valores lidos
print("Valores lidos totalizam: ", len(notas_lidas))

#Exibir os valores informados em ordem
print("Notas lidas: ", notas_lidas)

#Valores na ordem inversa ao informado um abaixo do outro
print("Ordem decrescente uma baixo da outra")
for i in range(len(notas_lidas) - 1,-1,-1):
    print((notas_lidas[i]))

#Soma dos valores
for i in notas_lidas:
    soma += i
print("A soma dos valores é: ",soma)

#Média dos valores
media = soma / len(notas_lidas)
print("A média dos valores é: ", media)

#Imprimir valores acima da média
for i in notas_lidas:
    if i > media:
        valores_acima_media += 1
print("Quantidade acima da média: ", valores_acima_media)

#Valores abaixo de 7
for i in notas_lidas:
    if i < 7:
        valores_abaixo_7 += 1
print("Quantidade abaixo de 7: ", valores_abaixo_7)

#Encerre o programa com uma mensagem
print("Obrigado por usar o programa!")
