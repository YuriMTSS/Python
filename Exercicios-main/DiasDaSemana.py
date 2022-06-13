""" 
Criar um algoritmo em PORTUGOL que leia o um número inteiro entre 1 e 7 e
escreva o dia da semana correspondente. Caso o usuário digite um número fora desse
intervalo, deverá aparecer uma mensagem informando que não existe dia da semana
com esse número. 
"""

dia = int(input("Digite um número relativo aos dias da semana: "))

if dia < 1 and dia > 7:
    print("Não representa um dia da semana")
elif dia == 1:
    print("Domingo")
elif dia == 2:
    print("Segunda Feira")
elif dia == 3:
    print("Terça Feira")
elif dia == 4:
    print("Quarta Feira")
elif dia == 5:
    print("Quinta Feira")
elif dia == 6:
    print("Sexta Feira")
elif dia == 7:
    print("Sabado")
