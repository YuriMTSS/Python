""" João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu 
trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado 
de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa
que leia a variável peso e calcule o excesso. Gravar na variável excesso a quantidade de
quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do 
programa com as mensagens adequadas. """

peso = float(input("Peso do peixe: "))
excesso = 0

if peso > 50:
    excesso = peso - 50
    
multa = 4.0 * excesso

#print(excesso)
print("O excesso de peso é: ", excesso, "kg")
print("Sua multa está no valor de: R$", multa)


