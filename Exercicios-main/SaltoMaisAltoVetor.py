"""Em uma competição de salto em distância cada atleta tem direito a cinco saltos. 
O resultado do atleta será determinado pela média dos cinco valores restantes. 
Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta 
em seus saltos e depois informe o nome, os saltos e a média dos saltos. O programa deve ser 
encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
Atleta: Rodrigo Curvêllo
 
Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m"""


texto_salto = ['Primeiro', 'Segundo', 'Terceiro', 'Quarto', 'Quinto']
saltos_do_atleta = [0.0, 0.0, 0.0, 0.0, 0.0]
melhor_salto = pior_salto = media_saltos = 0
atleta = input("Atleta: ")

# Verificando se o nome do atleta foi digitado
if atleta != '':
    for c in range(4):
        saltos_do_atleta[c] = float(input(f"{texto_salto[c]} salto: "))

    # Ordenando a lista de saltos
    saltos_do_atleta.sort()

    # Melhor, Pior e Média
    melhor_salto = max(saltos_do_atleta)
    pior_salto   = min(saltos_do_atleta)
    media_saltos = (saltos_do_atleta[1] + saltos_do_atleta[2] + saltos_do_atleta[3])/3    

    # Exibindo os resultados
    print("="*30)
    print(f"Melhor salto............: {melhor_salto}")
    print(f"Pior salto..............: {pior_salto}")
    print(f"Media dos demais saltos.: {media_saltos:.2f}\n")
    print("Resultado final: ")
    print(f"{atleta}: {media_saltos:.2f}")
else:
    print('Informe o nome do atleta') 