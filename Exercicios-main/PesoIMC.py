# Construa um algoritmo para determinar se o indivíduo esta com um peso favorável. 
# Essa situação é determinada através do IMC, que é definida pela relação do Peso e o quadrado da
# Altura do indivíduo. Ou seja, IMC = Peso / (Altura**2) e, a situação do peso é determinada pela tabela abaixo:
# IMC abaixo de 20 - Abaixo do peso
# IMC de 20 até 25 - Peso Normal
# IMC de 25 até 30 - Sobre Peso
# IMC de 30 até 40 - Obeso
# IMC de 40 e acima - Obeso Mórbido 

Peso = float(input("Entre com o peso: "))
Altura = float(input("Entre com a altura: "))
IMC = Peso / (Altura ** 2)
print("Seu IMC é: ", IMC)

if IMC < 20:
	print("Abaixo do peso")
elif IMC >= 20 and IMC < 25:
	print("Peso normal")
elif IMC >= 25 and IMC < 30:
	print("Sobre peso")
elif IMC >= 30 and IMC < 40:
	print("Obeso")
else:
	print("Obeso mórbido")
 