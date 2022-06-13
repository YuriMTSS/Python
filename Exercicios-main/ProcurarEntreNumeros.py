# Construa um algoritmo em PORTUGOL que indique se um número digitado está
# compreendido entre 20 e 90 ou não (20 e 90 não estão na faixa de valores). 

n = int(input("Informe o número: "))

if n > 20 and n < 90:
    print ("Está na faixa")
else:
    print("Fora da faixa")
