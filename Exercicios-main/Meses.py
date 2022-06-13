""" 
Criar um algoritmo em PORTUGOL que leia um número inteiro entre 1 e 12 e
escrever o mês correspondente. Caso o usuário digite um número fora desse intervalo,
deverá aparecer uma mensagem informando que não existe mês com este número. 
"""

mes = int(input("Digite um numero relativo aos meses do ano"))

if mes == 1:
    print("Janeiro")
elif mes == 2:
    print("Fevereiro")
elif mes == 3:
    print("Marco")
elif mes == 4:
    print("Abril")
elif mes == 5:
    print("Maio")
elif mes == 6:
    print("Junho")
elif mes == 7:
    print("Julho")
elif mes == 8:
    print("Agosto")
elif mes == 9:
    print("Setembro")
elif mes == 10:
    print("Outubro")
elif mes == 11:
    print("Novembro")
elif mes == 12:
    print("Dezembro")
else:
    print("Opcao invalida")

