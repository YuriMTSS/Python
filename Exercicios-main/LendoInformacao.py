"""Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd'; """

nome = str(input("informe um nome: "))
idade = int(input("informe a idade: "))
salario=float(input("informe um salário: "))
sexo = str(input("informe a inicial do seu sexo: "))
estado_civil = str(input("informe a inicial do seu estado civil: "))

while (len(nome) <=  3 ):
	nome = str(input("informe um nome: "))

while idade > 150 or idade < 0:
	idade = int(input("informe a idade: "))
	
while  salario < 0:
	salario = float(input("informe um salário: "))
	
while sexo != "f" and sexo!= "m":
	sexo = str(input("informe a inicial do seu sexo: "))

while estado_civil != "s" and estado_civil != "c" and estado_civil != "v" and estado_civil != "d":
	estado_civil = str(input("informe a inicial do seu estado civil: "))
