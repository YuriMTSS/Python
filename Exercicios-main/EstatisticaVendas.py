def Vendas_Produtos():    
    soma_produtos = preco_maior_1000 = cont = menor = 0
    mais_barato = ' '

    while True:
        nome_produto = str(input('Informe o nome do produto: '))
        preco_produto = float(input('Informe o preço dos produtos: '))
    
        cont += 1
        soma_produtos += preco_produto
        if preco_produto > 1000:
            preco_maior_1000 += 1

        if cont == 1:
            maior = preco_produto
            menor = preco_produto
            mais_barato = nome_produto
        else:
            if preco_produto < menor:
                menor = preco_produto
                mais_barato = nome_produto


        continuar = ' '
        while continuar not in 'SN':
            continuar = str(input('Outro produto?\n [S/N] ')).strip().upper()[0]
        if continuar == 'N':
            print('='*30)
            print('---Imprimindo resultados---')
            print(f'A soma total dos valores foi {soma_produtos:.3f}')
            print(f'O total de produtos maior que 1000 foram {preco_maior_1000}')
            print(f'O produto mais barato foi {mais_barato} que custa {menor}')
            print('='*30)
            break


Vendas_Produtos()
