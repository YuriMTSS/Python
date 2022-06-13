""" Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o
 tempo aproximado de download do arquivo usando este link (em minutos) """

arquivo = float(input("Tamanho do arquivo em MB: "))
link = float(input("Velocidade do link da internet em Mbps: "))

tempo_aproximado = arquivo / (link / 8)

print("Tempo aproximado: ", tempo_aproximado, " minutos")


