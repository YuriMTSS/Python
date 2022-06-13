"""Palíndromo. Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita para esquerda ou vice−versa. 
Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação são ignorados. 
A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados. 
Faça um programa que leia uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não."""

expressao = str(input("Excreva uma expressão: ")).upper().replace(' ', '')
invertido = expressao[::-1]

if expressao == invertido:
    print("É políndromo pois {} é {}".format(expressao, invertido))
else:
    print("Não é políndromo!")

"""O método replace() é utilizado para substituir um ou mais trechos em uma string. 
Ele contém parâmetros para auxiliar a forma de substituição desse conteúdo."""