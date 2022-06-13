while True:
    print('[1] Binário') 
    print('[2] Octal')
    print('[3] Hexadecimal')
    print('[x] Sair')
    perguntanum = str(input('Digite a opção que deseja converter: '))
    print('- - - - '* 5)

    n = int(input('Digite um número: '))

    if perguntanum == 'x'or perguntanum == 'X': 
        break 
    elif perguntanum == '1' or perguntanum == '2' or perguntanum == '3': 
        if perguntanum == '1': 
            rio = str(bin(n)[2:])
            print(rio) 

        elif perguntanum == '2':
            cta = str(oct(n)[2:])
            print(cta)

        elif perguntanum == '3':
            exa = str(hex(n)[2:])
            print(exa)
    else:
        print('Opção invalida!')