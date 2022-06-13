"""Faça um programa que carregue uma lista com os modelos de cinco carros outra lista com o consumo desses carros, isto é, 
quantos quilômetros cada um desses carros faz com um litro de combustível. Calcule e mostre:
O modelo do carro mais econômico; Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma 
distância de 1000 quilômetros e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro. 
Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. 
Os dados são fictícios e podem mudar a cada execução do programa. Comparativo de Consumo de Combustível

Veículo 1
Nome: fusca
Km por litro: 7
Veículo 2
Nome: gol
Km por litro: 10
Veículo 3
Nome: uno
Km por litro: 12.5
Veículo 4
Nome: Vectra
Km por litro: 9
Veículo 5
Nome: Peugeout
Km por litro: 14.5

Relatório Final
1 - fusca           -    7.0 -  142.9 litros - R$ 321.43
2 - gol             -   10.0 -  100.0 litros - R$ 225.00
3 - uno             -   12.5 -   80.0 litros - R$ 180.00
4 - vectra          -    9.0 -  111.1 litros - R$ 250.00
5 - peugeout        -   14.5 -   69.0 litros - R$ 155.17
O menor consumo é do peugeout."""

modelos = []
consumos = []
cont = 0 
custo = 0
gasto = 0
menor = 0
menor_modelo = ''

# Solicitar as informações do carro e armazenar na lista
for i in range(1,6):
    print("Veículo %d" % i)
    modelos.append(input("Nome: "))
    consumos.append(float(input("Km por litro: ")))

print("\nRelatório Final")
for m in modelos:
    # Calculando os custos e gasto do carro
    custo = 1000 // consumos[cont] 
    gasto = custo * 2.25

    # Imprimindo a tabela
    print("Um",m, "consome ", consumos[cont]," - ", custo ,"litros por R$", gasto)
    
    # Testando o menor gasto dos carros
    if cont == 0:
        menor = gasto
        menor_modelo = m
    if menor > gasto:
        menor = gasto
        menor_modelo = m
    cont += 1
print("O menor consumo é do %s." % (menor_modelo))
