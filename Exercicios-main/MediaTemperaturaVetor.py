"""Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. 
Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, 
e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . )."""

# Entrada
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
temperatura_ano = []
soma_temperaturas = 0
media_anual = 0


# Processamento

# Recebe as medias do mes, armazena na lista e depois soma
for i in range(0, len(meses)):
    temperatura_do_mes = int(
        input("Informe a temperatura média do mês " + meses[i] + ": "))
    temperatura_ano.append(temperatura_do_mes)
    soma_temperaturas += (temperatura_ano[i])

    # Pega a soma e tira a divisão inteira das medias e recebe a anual
media_anual = soma_temperaturas // 12

print("Media: ", media_anual)

# Percorre a lista das temperaturas do ano e verifica a condição, se a temperatura for maior que a média anual ele imprime o mês
for i in range(0, len(temperatura_ano)):
    if temperatura_ano[i] > media_anual:

        # Saída
        print(str(i + 1) + " - " + meses[i])
