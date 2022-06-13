"""Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. 
Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

Compara duas strings
String 1: Brasil Hexa 2006
String 2: Brasil! Hexa 2006!
Tamanho de "Brasil Hexa 2006": 16 caracteres
Tamanho de "Brasil! Hexa 2006!": 18 caracteres
As duas strings são de tamanhos diferentes.
As duas strings possuem conteúdo diferente."""

texto_1 = 'Brasil Hexa 2006'
texto_2 = 'Brasil! Hexa 2006!'

tamanho_1 = len(texto_1)
tamanho_2 = len(texto_2)

print("Tamanho de {} é {} caracteres".format(texto_1, tamanho_1))
print("Tamanho de {} é {} caracteres".format(texto_2, tamanho_2))

if tamanho_1 != tamanho_2:
    print("As duas strings são de tamanhos diferentes.")
