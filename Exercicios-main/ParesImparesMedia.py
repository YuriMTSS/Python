media_geral = 0
media_impares = 0
cont_impar = 0
media_pares = 0
cont_par = 0

for _ in range (1,6):
    Numero_usuario = int(input("Informe um número: "))
    media_geral += Numero_usuario 

    if Numero_usuario % 2 == 0:
        media_pares += Numero_usuario
        cont_par += 1
    else:
        media_impares += Numero_usuario
        cont_impar += 1

print("Média geral: ", media_geral / 5)
print("Média pares: ", media_pares / cont_par)
print("Média impar: ", media_impares / cont_impar)