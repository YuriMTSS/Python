""" Faça um programa que lê as duas notas parciais obtidas por 
um aluno numa disciplina ao longo de um semestre, e calcule a sua média.
A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E 
 O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a 
mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E
  """
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))

media = (nota1 + nota2) / 2

print("Média: ", media)

if media >= 9.0:
    print("A")
    print("Aprovado")
elif media <= 9.0 and media >= 7.5:
    print("B")
    print("Aprovado")
elif media <= 7.5 and media >= 6.0:
    print("C")
    print("Aprovado")
elif media <= 6.0 and media >= 4.0:
    print("D")
    print("Reprovado")
else:
    print("E")
    print("Reprovado")

