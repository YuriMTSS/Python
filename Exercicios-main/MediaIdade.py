"""Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar 
se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a 
turma é jovem, adulta ou idosa, conforme a média calculada """
media = 0

quantidade = int(input("Quantidade de pessoas: "))
for _ in range(quantidade):
    idade = int(input("Informe a idade: "))
    media += idade

print("Média", media/quantidade)
if media >= 0 and media <= 25:
    print("Turma Jovem")
elif media >= 26 and idade <= 60:
    print("Turma Adulto")
else:
    print("Turma Idoso")
