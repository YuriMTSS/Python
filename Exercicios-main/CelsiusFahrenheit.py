""" Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a 
temperatura em graus Celsius.Em seguida um Programa que peça a temperatura em graus 
Celsius, transforme e mostre em graus Fahrenheit
C = 5 * ((F-32) / 9) 
F = c * 1.8 + 32
"""

fahrenheit = int(input("Informe a temperatura em Fahrenheit: "))
celsius = int(input("Informa a temperatura em Celsius: "))


c = 5 * ((fahrenheit-32) / 9)
f = celsius * 1.8 + 32

print("Celsius: ", c)
print("Fahrenheit: ", f)

