""" 
Construa um algoritmo em PORTUGOL para determinar a situação
(APROVADO/EXAME/REPROVADO) de um aluno, dado a sua freqüência
e sua nota, sendo que:

Freqüência até 75% Reprovado
Freqüência entre 75% e 100% e Nota até 3.0 Reprovado
Freqüência entre 75% e 100% e Nota de 3.0 até 7.0 Exame
Freqüência entre 75% e 100% e Nota entre 7.0 e 10.0 Aprovado 
"""

nota = float(input("Informe a nota do aluno: "))
frequencia = float(input("Informe a frequancia do aluno: "))

if frequencia < 75:
    print("Reprovado")
elif nota < 3 and frequencia >= 75:
    print("Reprovado")
elif  nota >= 3 and nota < 7:
    print("Exame")
else:
    print("Aprovado") 
