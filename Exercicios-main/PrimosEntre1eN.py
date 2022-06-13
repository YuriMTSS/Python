"""
Faça um programa que mostre todos os primos 
entre 1 e N sendo N um número inteiro fornecido 
pelo usuário. O programa deverá mostrar também 
o número de divisões que ele executou para encontrar 
os números primos. Serão avaliados o funcionamento,
o estilo e o número de testes (divisões) executados.
"""
primos = []
cont = 0
divisoes = 0
numero = int(input("Numero: "))

for x in range(1,numero):
    contador_divisor = 0
    divisoes += 1
    for y in range(1, x + 1):
        if x % y == 0:
            contador_divisor += 1

    if contador_divisor == 2:
        cont += 1
        primos.append(x)

print("Divisoes: ", divisoes)
print("Total de primos: ", cont)
print("Primos:", primos)

