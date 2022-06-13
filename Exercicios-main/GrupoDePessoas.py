def analise_grupos():
    mais_18 = 0
    homens = 0
    mulheres_menos_20 = 0
    
    while True:
        
        idade = int(input('Informe a idade da pessoa: '))
        sexo = ' '
        while sexo not in 'MF':
            sexo = str(input('Informe o sexo da pessoa: [M/F]')).strip().upper()[0]


        if idade > 18:
            mais_18 += 1
        if sexo == 'M':
            homens += 1
        if sexo == 'F' and idade < 20:
            mulheres_menos_20 += 1

        continuar = ' '
        while continuar not in 'SN':
            continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        if continuar in 'N':
            print(f'\nTotal de pessoas com mais de 18 anos {mais_18}')
            print(f'Total de Homens cadastrados foram {homens}')
            print(f'Total de mulheres com menos de 20 anos é {mulheres_menos_20}')
            break
        



analise_grupos()