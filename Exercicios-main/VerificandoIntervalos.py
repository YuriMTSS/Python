""" 
Escrever um algoritmo que leia uma quantidade desconhecida de números e conte quantos deles
estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deve
terminar quando for lido um número negativo.  
"""
numero = 1
Intervalo1 = 0
Intervalo2 = 0
Intervalo3 = 0
Intervalo4 = 0

while numero >= 0:
    numero = int(input("Digite um número: "))
    if numero >= 0 and numero <= 25:
        Intervalo1 += 1
    elif numero >= 26 and numero <= 50:
        Intervalo2 += 1
    elif numero >= 51 and numero <= 75:
        Intervalo3 += 1
    elif numero >= 76 and numero <= 100:
        Intervalo4 += 1
print("Intervalo 0 a 25: ", Intervalo1)
print("Intervalo 26 a 50: ", Intervalo2)
print("Intervalo 51 a 75: ", Intervalo3)
print("Intervalo 76 a 100: ", Intervalo4)


