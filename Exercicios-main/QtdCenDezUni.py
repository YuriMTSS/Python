"""Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades.
Observando os termos no plural a colocação do "e", da vírgula entre outros. 
Exemplo: 326 = 3 centenas, 2 dezenas e 6 unidades ou então 12 = 1 dezena e 2 unidades """
numero = int(input('Digite um numero inteiro positivo: '))

if numero < 1000:
    while numero > 1:
        unidade = numero % 10
        numero /= 10

        dezena = numero % 10
        numero /= 10
        
        centena = numero % 1000
        numero /= 10

        dezena = int(dezena)
        centena = int(centena)
        
        print(centena,'centena(s),',dezena,'dezena(s) e',unidade,'unidade(s)')
else:
    print("Digite um número menor que 1000")
