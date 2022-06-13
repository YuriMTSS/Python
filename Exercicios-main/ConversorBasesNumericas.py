"""Leia um número inteiro e peça ao usuario qual a base de conversão
binario
octal
hexadecimal"""

num = int(input("Digite um número inteiro: "))
print("""Escolha uma das bases para conversão:
[ 1 ] Binário
[ 2 ] Octal
[ 3 ] Hexadecimal""")
opcao = int(input("Sua opção: "))
if num == 1:
    print("{} em binário é {}".format(num, bin(num)[2:]))
elif num == 2:
    print("{} em octal é {}". format(num, oct(num)[2:]))
else:
    print("{} em hexadecimal é {}".format(num, hex(num)[2:]))
