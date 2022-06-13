"""Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

quantos espaços em branco existem na frase.
quantas vezes aparecem as vogais a, e, i, o, u."""

vogais = ['a', 'e', 'i', 'o', 'u']
cont_vogal = 0
frase = str(input("Informe uma frase: "))

# Conta espaços
print("Espaços: ", frase.count(" "))

# Verifica as vogais
for v in vogais:
    print(v, ":", frase.lower().count(v), end="\n")
"""
A função count() também pode ser utilizada para saber se um determinado elemento está contido, 
até porque, se o valor retornado for igual a 0, sabemos, que determinado elemento ainda não foi adicionado """
"""
Com o método lower(), retornamos uma cópia da string com todas as letras maiúsculas convertidas em minúsculas. """