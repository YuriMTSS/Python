"""Faça uma função que calcule fatorial de entrada do usuario"""

def fatorial(n):
    f = 1
    for i in range(n, 0, -1): # Começa do n e vai ate o 1 subtraindo de 1 a 1
        f *= i                # Pega os antecessores e multplica ate o 1
    return f                  # Retorna o fatorial

numero = int(input("Informe o valor: "))
print("O fatorial de {} é {}".format(numero, fatorial(numero)))
