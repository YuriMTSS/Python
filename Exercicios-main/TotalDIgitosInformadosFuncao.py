"""Faça uma função que informe a quantidade de dígitos de um
determinado número inteiro informado"""

def qtd_digitos(n):
    numero = str(n)
    return len(numero)

numero = int(input("Informe um numero inteiro: "))
print("Foram informados {} digitos.".format(qtd_digitos(numero)))
