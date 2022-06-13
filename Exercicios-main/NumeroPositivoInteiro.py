""" 
Faça um algoritmo estruturado que leia uma quantidade não determinada de números positivos.
Calcule a quantidade de números pares e ímpares, a média de valores pares e a média geral dos
números lidos. O número que encerrará a leitura será zero.  
"""
Pares = 0
Impares = 0
Positivos = 0
Cont_Media = 0
Media = 0
Cont_Media_Pares = 0
Media_Pares = 0
termino = 1

while termino != 0:    
    print("Digite 0 se deseja sair do loop")
    numero = int(input("Digite um valor: "))

    if numero != 0:
        if numero % 2 == 0:
            Pares += 1
        
        else:
            Impares += 1

        if numero > 0:
            Positivos += 1

        Media += numero
        Cont_Media += 1
        ResultadoMedia = Media / Cont_Media

        if numero % 2 == 0:
            Media_Pares += numero
            Cont_Media_Pares += 1
            Resultado_Media_Pares = Media_Pares / Cont_Media_Pares
    else:
        termino = 0

print(Pares, " pares")
print(Impares, " impares")
print(ResultadoMedia, " media")
print(Resultado_Media_Pares, " media pares")
