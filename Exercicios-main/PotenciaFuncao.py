"""Faça uma função que computa a potência ab
para valores a e b (assuma números inteiros) 
passados por parâmetro (não use o operador **)."""

def potencia(base, expoente):
    resultado = 1
    for _ in range(expoente):
        resultado *= base   # base ** expoente = base * base (expoente vezes)
    return resultado

base = int(input("Informe a base em inteiro: "))
expoente = int(input("Informe o expoente em inteiro: "))

print("A potencia de {} com {} é {}".format(base, expoente, potencia(base, expoente)))
