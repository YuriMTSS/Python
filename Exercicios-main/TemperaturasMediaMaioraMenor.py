"""O Departamento Estadual de Meteorologia lhe contratou para desenvolver 
um programa que leia um conjunto indeterminado de temperaturas, e informe 
ao final a menor e a maior temperaturas informadas, bem como a média das 
temperaturas."""
Qtd_temperaturas = int(input("Quantidade de temperaturas a serem processadas: "))
somatorio = 0

for x in range(Qtd_temperaturas):
    temperatura = int(input("Digite a temperatura: "))
    somatorio += temperatura

    menor = temperatura
    maior = temperatura

    if maior > temperatura:
        menor = temperatura
    else:
        maior = temperatura

print()
print("Menor temperatura: ", menor)
print("Maior temperatura: ", maior)
print("Média de temperatura: ", somatorio / Qtd_temperaturas)
