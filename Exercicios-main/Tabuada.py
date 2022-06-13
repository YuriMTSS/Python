""" Escrever um algoritmo que leia um valor para uma variável N de 1 a 10 e calcule a tabuada de
N. Mostre a tabuada na forma: 0 x N = 0, 1 x N = 1N, 2 x N = 2N, ..., 10 x N = 10N. """

N = int(input("Digite o número: "))

for a in range (1,11):
    print("--" * 6)
    for N in range(1,11):
        print('{:2} x {:2} = {:2}'.format(a, N, a*N))
        