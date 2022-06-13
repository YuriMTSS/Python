"""Faça um Programa que leia uma lista de 10 caracteres, e diga quantas consoantes foram lidas.
#Imprima as consoantes."""

caractere = []
vogais = ["a","e","i","o","u"]
cont_vogal = 0

for x in range (10):
    entrada = input("Caractere: ")
    caractere.append(entrada)

    if entrada in vogais:
        cont_vogal += 1

print ("Consoantes: ",(len(caractere)) - cont_vogal)
