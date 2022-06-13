""" 
Criar um algoritmo em PORTUGOL que a partir da idade e peso do paciente calcule a dosagem de determinado medicamento e imprima a receita 
informando quantas gotas do medicamento o paciente deve tomar por dose. Considere que o medicamento em questão possui 500 mg por ml, 
e que cada ml corresponde a 20 gotas.
- Adultos ou adolescentes desde 12 anos, inclusive, se tiverem peso igual ou
acima de 60 quilos devem tomar 1000 mg; com peso abaixo de 60 quilos
devem tomar 875 mg.
- Para crianças e adolescentes abaixo de 12 anos a dosagem é calculada pelo
peso corpóreo conforme a tabela a seguir:

5 kg a 9 kg - 125 mg
9.1 kg a 16 kg - 250 mg
16.1 kg a 24 kg - 375 mg
24.1 kg a 30 kg - 500 mg
Acima de 30 kg - 750 mg  
"""

idade = int(input("Idade do paciente: "))
peso = float(input("Peso do paciente: "))

gota = 500 / 20

if peso < 5:
    print("Não pode tomar remedio")
elif idade >= 12:
    if peso >= 60:
        print("Pode tomar ", 1000 / gota, " gotas")
    else:
        print("Pode tomar ", 875 / gota, "gotas")
elif peso <= 9:
    print("Tomar ", 125 / gota, " gotas")
elif peso <= 16:
    print("Tomar ", 250/gota, " gotas")
elif peso <= 24:
    print("Tomar ", 375/gota, " gotas")
elif peso <= 30:
    print("Tomar ", 500/gota, " gotas")
else:
    print("Tomar ", 750/gota, " gotas")
