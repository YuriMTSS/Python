""" Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto. """

ano = int(input("Informe o ano: "))

if ano % 4 == 0:
    print("É bissexto")
else:
    print("Não é bissexto")


