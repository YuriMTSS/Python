# -*- coding:utf -8 -*-


'''
sudo nautilus
gksu nautilus

'''


"""
for i in range (10):
	print (i)
"""

#CONVENÇÕES DE NOMES DE CLASSES, MÉTODOS E FUNCÕES EM PYTHON
#Não usar I, O, l, como variáveis para não confundir com 1 e 0.
#Pacotes ->   nomes pequenos, minúsculos = package
#Classes -> iniciais maiúsculas = NomeDeUmaClasse (CamelCase)
#Funcões e métodos -> minúsculos separados por underline(underscore) = nome_de_uma_funcao 'ou' nome_de_um_metodo
#         permitifo onde o contexto é predominante = nomeDeUmaFuncao (evitar)
#Constantes, em nível de módulo = MAX_OVERFLOW 'ou' TOTAL
#Variáveis e Parâmetros -> minúsculas (com '_') => Ex: numero 'ou' numero_principal
#Linhas em branco separam funções/classes (duas linhas) -----   ou métodos (uma linha)
#Espaços em branco - > separa operadores matemáticos, binários, de comparação, de atribuição => if variavel == False: print (2 * 3)
#Usar => def funcao(a,b)             funcao(2, 3) na chamada dela

#return super().escuta(frase)
#print(dir(__builtins__))



'''
Nesse caso utilizamos o caractere de escape \'. Abaixo temos uma lista de todos os caracteres de escape definidos em Python:

\n - Nova linha. Move o cursor para o início da próxima linha.
\t - Tabulação Horizontal. Move o cursor para a próxima parada de tabulação (tab).
\r - Retorno de carro. Move o cursor para o início da linha atual; não avança para a próxima linha.
\b - Backspace. Retrocede o cursor um caractere.
\a - Alerta. Emite o som de sino do sistema.
\\ - Barra invertida (Backslash).
\" - Caractere de aspas duplas.
\' - Caractere de aspas simples.
'''





















"""
#ARVORE DE NATAL
import time
sl=1
time.sleep(sl)


slp=0.5
n=6
for i in range(1,n,2):
	print (5*" ",int((n-i)/2)*" ",i*"*")
	time.sleep(slp)

n=8
for i in range(3,n,2):
	print (4*" ",int((n-i)/2)*" ",i*"*")
	time.sleep(slp)
	
n=16
for i in range(5,n,2):
	print ((int((n-i)/2)+1)*" ",i*"*")
	time.sleep(slp)
	
n=15
n1=3
print (int((n)/2)*" ",n1*"*")
time.sleep(slp)
print (int((n)/2)*" ",n1*"*")
time.sleep(slp)
print (int((n)/2)*" ",n1*"*")
print()
print (int((n)/2-4)*" ","FELIZ NATAL !")

"""


"""
# EH PRIMO?

while True:
	n=int(input("Digite o numero: "))
	if n<=1:
		print("Deve ser maior ou igual a 1")
	else:
		break


teste=""
for i in range (2,n):
	#if teste=="fim":
	#	break
	#for j in range (2,i+1):
	#	if i%j==0:
	#		print ("Não é primo")
	#		teste="fim"
	#		break
	#	if i>=(j/2+1):
	#		print ("É primo")				
	#		break
	if n%i==0:
		print ("Não é primo")
		break
	if i<(n-1):		
		continue
	else:
		print ("É primo")				
"""

"""
n = int(input('A sequência de Fibonacci de: '))
a, b = 0, 1
while a < n:
    print(a, end=',')
    a, b = b, a+b
print('FIM')
"""


"""	
lista=[10,7,12,3,45,20,34,5]

maior=lista[0]
for i in lista:
	if i>maior:
		maior=i
		
print (maior)		
"""

"""
#Dado o nome do estudante, diga qual o primeiro nome e o sobrenome dele.

nome=input("Digite o nome do aluno:\n")

lista=nome.split(" ")
#print (lista)
print ("O primeiro nome é:",lista[0])
print("O sobrenome é:",lista[(len(lista)-1)])
"""


"""
tupla = (2,3,7,5)
lista=[2,3,7,5]
del lista[1]
print (lista)
tupla2=tupla[1:]
print (tupla2)
"""


"""
lista=["a",2]
del lista["a"]
print (lista)
"""

"""
print ("***********************************************")
print ("***********************************************")
print ("**                                           **")
print ("**        SEJA BEM-VINDO AO QUIZ RCM         **")
print ("**                                           **")
print ("***********************************************")
print ("***********************************************")
"""

"""
class Conta:
	def __init__ (self,a,b):
		self.a=a
		self.b=b
		print (2)



a=2
b=5
		
nov=Conta(a,b)		
nove=Conta(a,b)		
print(nov)		
print (nove)
"""

"""
for i in range (1,11):
	for j in range (1,11):
		if j==10:
			print ("*")
		else:
			print ("*", end=" ")
"""


"""
nome="abc"
a=list(nome)
print (a)
"""

"""
lista=["a","b","c"]
print(*lista,sep="")
"""		

"""
lista=[1,2,3]
lista=lista[1:]
print (lista)
"""

"""
FloatLayout:
    TextInput:
        text: "eXcript"
        height: "30px"
        width: 350
        top: 100
        size_hint: None, None
        pos_hint: {'center_x': 0.5,}
    Button:
        text: "Confirmar"
        height: 30
        top: 60
        size_hint: None, None
        pos_hint: {'center_x': 0.5,}
"""



"""
lista=[4,1,3,2]
listaord=lista[0:]
listaord.sort()
print (listaord)
print (lista)
"""

"""
def ola (nome):
	return ("Olá %s" %nome)
	

print (ola("João"))
"""

"""
print (5)
print (5)
print (5)
print (5)

import math
"""


"""
for i in range (1458):
	for j in range (729):
		if i*j==1457:
			print (i,j)
"""

"""
lista=[(9,3,9),(4,2)]
lista.sort()
print (lista)
"""

"""			
# EH PRIMO?

for m in range (2,10):
	while True:
		n=m#int(input("Digite o numero: "))
		if n<=1:
			print("Deve ser maior ou igual a 1")
		else:
			break


	cont=0
	for i in range (2,n):
		if n%i==0:
			#print (i,"É divisor")
			cont += 1
			continue
		if i==(n-1) and cont==0:
			print (i)#("É primo")	
		#else:
		#print ("É primo")				
"""


"""
for i in range (10):
	print (i)
	
for i in range (5):
	print (i)	
"""


"""
tupla=(1,2,3)
print (tupla[1:])
"""

"""
#PRIMO
for m in range(2,1000):
	n=m
	for i in range (2,n):
		if n%i!=0 and i==(n-1):
			print (n)
		if n%i==0:
			break
"""

		
"""
n=15997

for i in range (n-1):
	for j in range (n-1):
		if i*j==n:
			print (i,j)		
"""

"""
n=15997

for i in range (100):
	for j in range (100):
		if (i*j-int(i*j/100)*100)==(n-int(n/100)*100):
			print (i,j)		
"""


"""
from itertools import permutations
import re

caracteres = ['A', 'B', 'C', 'D']

for i in permutations(caracteres,2): # 2 elementos
    i = re.sub(r'\W',"",str(i)) # Retirando outros caracteres que não sejam letras
    print(i)

print()
for i in permutations(caracteres,3): # 3 Elementos
    i = re.sub(r'\W',"",str(i))
    print(i)

print()
for i in permutations(caracteres,4): # 4 Elementos
    i = re.sub(r'\W',"",str(i))
    print(i)
"""



"""
for i in range (10):
	print (i)
"""








"""
input ("gggg\n")
print (2)
"""




	
"""	
a="teste"
b=a[1:3]
print (b)
"""

"""
print('There\'s a snake in my boot!')
"""


"""
print ("b" not in "abc")

"foo".upper() # FOO
"ALFA".lower() # alfa

"abc".isalpha()  # True
"1fg".isalpha()  # False
"123".isalpha()  # False
"/+)".isalpha()  # False
#Retorna False se a string contiver algum caracter que não seja letras

" sobrando espaços ".strip()      # 'sobrando espaços'
"  sobrando espaços   ".strip()   # 'sobrando espaços'

", ".join("abc")
# 'a, b, c'

"-".join(['flavio', 'alexandre', 'micheletti'])
# 'flavio-alexandre-micheletti'

print("-".join(['flavio', 'alxandre', 'micheletti']))
"""


"""
s = 'n o m e'
print (s.split())
# ['n', 'o', 'm', 'e']
print (s.split(" "))
# ['n', 'o', 'm', 'e'])
#print (s.split("")    # ValueError: empty separator)
"""


"""
r = "vermelho"
g = 3 #"verde"
b = "azul"
print("As cores básicas são: %s, %d e %s" % (r, g, b))
# As cores básicas são: vermelho, verde e azul
"""


"""
>>> print("%.2f" % 5)
5.00
>>> print("%.5f" % 5)
5.00000
"""	


"""
x=3
y=6

soma=0
cont=0
rang=x
passo=x
while cont<(y-1):
	soma=0
	for i in range (rang):
		soma=soma+passo
		
	passo=soma	
	
	cont+=1
	
print (soma)
"""

"""
NAO
for i in range (1,21):
	if i%3!=0 and i%5!=0:
		print (i)
	elif i%3==0:
		print ("fizz")
	elif i%5==0:
		print ("buzz")
	else:
		print ("fizzbuzz")
"""		

#print ("XXXXXXXXXXXXXXXXXXXXXXXXX")

"""
SIM
for i in range (1,21):
	if i%3==0 and i%5==0:
		print ("fizzbuzz")
	elif i%3==0:
		print ("fizz")
	elif i%5==0:
		print ("buzz")
	else:
		print (i)
"""


"""
ano1 = '1980'
ano2 = '1990'
ano3 = '2000'
ano4 = '2010'

texto = "Alterando o valor de sep"
print(texto)
print(ano1, ano2, ano3, ano4, sep='--->')

# pula uma linha
print()

texto = "Alterando o valor de sep e end"
print(texto)
print(ano1, ano2, ano3, ano4, sep='--->', end='...\n')
"""	


"""	
str = 'O filme {0} merece {1} estrelas'
print(str.format('Exterminador do Futuro', 4))

#'O filme Exterminador do Futuro merece 4 estrelas'
"""



"""
texto = '{0} tem {idade} anos de idade'
print('Progama para calcular a idade de uma pessoa')
print()

nome = input('Entre com o nome da pessoa: ')
print()

a1 = int(input("Entre com o ano de nascimento: "))
print()

a2 = int(input("Entre com ano atual: "))
print()
print(texto.format(nome, idade = a2 - a1 ))
"""


"""
# COMANDO FORMAT
#!/usr/bin/env python3
# Programa para testar a função format()

s = 'Adoro Python'

# alinha a direita com 20 espaços em branco
print("{0:>20}".format(s))

# alinha a direita com 20 símbolos #
print("{0:#>20}".format(s))

# alinha ao centro usando 10 espaços em branco a esquerda e 10 a direita
print("{0:^20}".format(s))

# imprime só as primeiras cinco letras
print("{0:.5}".format(s))


table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print('{:10} ==> {:10d}'.format(name,phone))

print('Eu quero o {} e a "{}!"'.format('bolo', 'fruta'))
#Eu quero o bolo e a "fruta!"

print('Eu quero o {0} e a "{1}!"'.format('bolo', 'fruta'))
#Eu quero o bolo e a "fruta!"

print('Eu quero o {comida} e a "{fruta}!"'.format(comida='bolo', fruta='maçã'))
#Eu quero o bolo e a "fruta!"


print('12'.zfill(5))
#'00012'
print('-3.14'.zfill(7))
#'-003.14'
print('3.14159265359'.zfill(5))
#'3.14159265359'

import math
print('The value of pi is approximately %5.3f.' % math.pi)
#The value of pi is approximately 3.142.

fruta='maçã'
nome='joao'
print('Eu gosto de {0} {1}!'.format(fruta, nome))

fruta='maçã'
print('Eu gosto de %s!' %(fruta))




"""

"""
for x in range(1, 11):
	print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
"""

'''
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
'''


"""
Onde as flags são:

Flag	Significado
#	
Prefixa os inteiros com 0, 0o, 0O, 0x, 0X.
o ou O para octais e x ou X hexadecimais

+	Força a saída com sinal.
E os conversores são:

Conversor	Significado
d	Inteiro.
i	Inteiro.
f	Float.
F	Float.
o	Inteiros em octal.
x	Inteiros em hexadecimal minuscula
X	Inteiros em hexadecimal maiúsculas
e	Float em formato exponencial minusculo
E	Float em formato exponencial maiúsculo
g	Mesmo que “e” se expoente é maior do que -4 ou inferior a precisão, “f” de outra forma.
G	Mesmo que “E” se expoente é maior do que -4 ou inferior a precisão, “F” de outra forma.
c	Um único caractere.
s	String (converte qualquer objeto python usando str ()).
Mais alguns exemplos para executar no ambiente iterativo:

>>> print('%+d' % 123)
+123
>>> print('%+4.2f' % 12.3678)
+12.37
>>> print('%x' % 123)
7b
>>> print('%#x' % 123)
0x7b
"""


"""
"{0:4}".format(-123)
'-123'
"{0:4}".format(123)
' 123'
"{0:4.2f}".format(33.3287)
'33.33'
"{0:+4.2f}".format(33.3287)
'+33.33'
"{0:+4.2e}".format(33.3287)
'+3.33e+01'
"{0:b}".format(123)
'1111011'
"""

"""
# Programa para calcular a media de um aluno
print('Programa para calcular a media de um aluno')
print()

nome = input('Entre com o nome do aluno: ')
print()

nota1 = float(input("Entre com a primeira nota: "))
print()

nota2 = float(input("Entre com a segunda nota: "))
print()

media = (nota1 + nota2)/2
print('{0} teve media igual a: {1:4.2f}'.format(nome, media))
"""


"""
frase="o menino é legal"
#transformar em "a menina é legal"

print(frase.replace("o menino", "a menina"))
print(frase.replace("o","a"))

titulo = 'aulas de python'

# Pegando caractere por caractere
print(titulo[0])
print(titulo[4])

# Agora pegando intervalos de caracteres
print(titulo[0:5])
print(titulo[9:15])

# Outros modos:

# Do começo até X
print(titulo[:5])
print(titulo[0:5])

# De X até o fim
print(titulo[9:])
"""

"""
titulo = '     aulas de python     '

print(titulo.strip())
print(titulo.lstrip())
print(titulo.rstrip())
"""

"""
titulo = 'aulas de python'

print(titulo.find('de'))
print(titulo.find('we'))
6
-1
"""


"""
class Pessoa:
	def __init__ (self, nome, idade):
		self.nome=nome
		self.idade=idade
		
	def setNome(nome):
		self.nome=nome
	
	def getNome(self):
		return self.nome
		
p1=Pessoa ("João", 14)
print (p1.getNome())		
"""		


"""	
lista=[1,2,3,4,5]

lista[3-1]=100
print(lista)

lista[5-1]=100
print(lista)
"""


"""
import time
sl=1
time.sleep(sl)


slp=0.2
n=6
for i in range(1,n,2):
	print (5*" ",int((n-i)/2)*" ",i*"*")
	time.sleep(slp)

n=8
for i in range(3,n,2):
	print (4*" ",int((n-i)/2)*" ",i*"*")
	time.sleep(slp)
	
n=16
for i in range(5,n,2):
	print ((int((n-i)/2)+1)*" ",i*"*")
	time.sleep(slp)
	
n=15
n1=3
print (int((n)/2)*" ",n1*"*")
time.sleep(slp)
print (int((n)/2)*" ",n1*"*")
time.sleep(slp)
print (int((n)/2)*" ",n1*"*")
"""


"""
import time
sl=2
time.sleep(sl)

for i in range(1,11):
	print (i)
	time.sleep(sl)
"""

"""
for i in range (10):
	print("yuri")
"""

"""
lista=[1,2,3,4,5]

lista1=lista[1:4]
print(lista)
print(lista1)
"""

"""
while True:
	p=int(input("Digite a tabuada desejada: ('s' para sair)"))
	if p=="s":
		break
	for i in range(1,10):
		print(i,"x",p,"=",i*p)
"""

"""
a=10
numeros=[2,3,4,5]
nome="yuri"
letra="a"
ponto=(2,3)

print(ponto[1])
ponto[1]=10
"""


"""
#matriz=[[],[],[]]
matriz=[[1,2,3],[4,5,6],[7,8,9]]

for i in range(3):
	for j in range(3):
		print (matriz[j][i])
"""

"""
#JOKENPO

pedra=0
tesoura=2
papel=5


j1=("Digite sua opção (0,2,5) -> ")
j2=("Digite sua opção (0,2,5) -> ")

if j1==0 and j2==2:
	print ("Vencedor jogador 1")
elif 

"""





























"""
lista=["1","2","3"]
print("-".join(lista))
"""




"""
lista=["1","X","O","4"]
nova_lista=[]
for i in lista:
	if i=="X":
		i=1
	elif i=="O":
		i=2	
	else:
		i=int(i)	
	nova_lista.append(i)
print (nova_lista)
print(sum(nova_lista))
"""


"""
titulo = 'aulas de python'

# Pegando caractere por caractere
print(titulo[0])
print(titulo[4])

# Agora pegando intervalos de caracteres
print(titulo[0:5])
print(titulo[9:15])

# Outros modos:

# Do começo até X
print(titulo[:5])
print(titulo[0:5])

# De X até o fim
print(titulo[9:])
"""


"""
print(sum(lista))
"""


"""
lista=[1,2,3]
soma1=sum(lista[0:2])
soma2=sum(lista[1:])
print(soma1)
print(soma2)
"""

"""
def tst():
	tst=1
	print (tst)
	

tst()
"""


"""
lista=[1,"a",3]

lista[1]=10
print (lista)
"""

"""
a=int(input("gfgfgf"))
print (a)
"""

"""
print("ola",27,"as")
"""

"""
n1=int(input("Digite o primeiro número: \n"))
n2=int(input("Digite o segundo número: \n"))

media=(n1+n2)/2

print("A média entre",n1,"e",n2,"é",media)
"""

"""
for i in range(1,10000001):
	print(i)
"""


"""
lista=[9,10,8,7,10,9,8,9,7,6]
print(len(lista))
"""


"""
media=sum(lista)/10
print(media)

soma=0
for i in lista:
	soma+=i
	
media1=soma/(len(lista))
print(media1)
"""

"""
n1=int(input("Digite o numero: "))
n2=int(input("Digite o numero: "))
n3=int(input("Digite o numero: "))

maior=0
if n1>n2 and n1>n3:
	maior=n1
elif n2>n3:
	maior=n2
else:
	maior=n3
print()
print(maior)			
"""

"""
while True:
	f=0


	f=int(input("Digite a temperatura em Fahrenheit: "))
	c=(f-32)/9*5
	print ("A temperatura de",f,"Fahrenheit","equivale a",c,"Celsius")
"""

"""
for i in "Kaio":
	print(i)
"""

'''
for i in range (10):
	print (i)
'''


"""
n=input("digite: ")
print (n)
print (n*3)

print ()

n=int(input("digite: "))
print (n)
print (n*3)
"""


"""
n=int(input())
print(int(n/3)*4)



n=int(input())
a=(int(n/3))
print(a*4)
"""


"""
ação=[2,1,4,6]
print (ação)
"""

"""
nome = "João"
peso = 50.3
idade = 30
print ("{} {} {}".format(nome, peso,idade))
print (nome, peso,idade)
print ("Nome: {} Peso:{} Idade: {}".format(nome, peso,idade))
"""

"""
idade=10
idade=30+idade
print (idade)
print ("Idade: {}".format(idade))

"""


"""
nome = input("Digite seu nome: ")
idade = input("Olá {}, agora digite seu nome: ".format(nome))
print("Nome: {}, Idade: {}".format(nome,idade))
"""
"""
def soma(x,y):
	print(x+y)
	return (x+y)
	
a=soma(2,3)
print(a)
"""

"""
preco=list(range(0,3))
print(preco)
"""


"""
numeros = [1,
			2,
			3]

print (numeros)
"""




"""
lista.remove(8)
del lista[2]
print(lista)
"""



"""
n=int(input("Digite o número: "))
if n%2==0:
	print(n, "é par")
else:
	print(n, "é ímpar")
"""

"""
n=(input("Digite o número: "))
if n[len(n)-1] in ["0","2","4","6","8"]:
	print(n, "é par")
else:
	print(n, "é ímpar")
"""


"""
lista=[1,2,3,4,5,6,7,8,9,10]

#print(lista[0]+lista[1]+lista[2]+lista[3]+lista[4])

soma=0
for i in lista:
	soma=soma+i
print(soma)	


soma=0
for i in lista:
	soma+=i
print(soma)	

print(sum(lista))

soma=0
for i in range(2,101,2):
	soma+=i
print(soma)

soma=0
for i in range(101):
	if i%2==0:
		soma+=i
print(soma)
"""


"""	
def main():
	b=int(input("Digite a base: "))
	h=int(input("Digite a altura: "))
	
	area_ret=area(b,h)
	print("A área do retângulo é",area_ret)
	
	
main()		

def area (b,h):
	return b*h
"""

"""
def fatorial(n):
	if n==0:
		return 1
	return n*fatorial(n-1)

print(fatorial(6))
"""


"""
inicio=1
fim=10
linhas=10

for j in range(linhas):
	for i in range (inicio,fim+1):
		print (i, end=" ")
	print("\n")
	inicio+=10
	fim+=10 
"""

"""
x=1

while x<5:
	print (x*"*")
	x+=1
	
while x>0:
	print (x*"*")
	x-=1 	
"""

"""
n=1
soma=0;
while (n<=1000):
	soma=soma+n
	n=n+1
print (soma)	


soma=0
for i in range (1,1001):
	soma=soma+i
print (soma)	
"""

"""
n=1
fat=1

for i in range(1,41):
	fat=fat*i
	print ("fatorial de ",i,"eh",fat)
"""

"""
x=13
while x!=1:
	if x%2==0:
		x=int(x/2)
	else:
		x=3*x+1
	if x!=1:
		print (x,"-> ", end="")	
	else:
		print (x)		
"""

"""
str='teste'
str=str+'c'

print(str)
"""


"""
a='absurdo'

print (a[3:])
"""

"""
numero=45
a="s"
for i in range (2, numero):
	if numero%i==0:
		print ("não eh primo")
		a="n"
		break
if a=="s":
	print (numero,"eh primo")	
"""

"""
palavra="absoluto"
print (palavra[3])

a=5
b=a
a=8
print (b)
print (a)
"""

"""
vogal=""
palavra='abacate'
lista=[]
for vogal in (palavra):
	if vogal not in ["a","e","i","o","u"]:
		pass
		if vogal not in lista:
			lista.append(vogal)
			
			print(vogal)
print (lista)	
"""

"""
a=int(input("Digite o 1o. Numero: "))
b=int(input("Digite o 2o. Numero: "))

maior=0
menor=0

if a>b:
	maior=a
	menor=b
else:
	maior=b
	menor=a

resto=maior%menor		

while resto!=0:
	maior=menor
	menor=resto
	resto=maior%menor
	
print ("O MDC entre",a,"e",b,"eh",menor)
"""


"""
lista=[11,6,2,4,9,3]
lista_ordenada=[]
while 1:
	if len(lista)>=1:
		menor=10000000000
		for i in range (len(lista)):
			if lista[i]<menor:
				menor=lista[i]
				n=i	
		lista_ordenada.append(lista[n])
		del lista[n]
	else:
		break
		
print (lista_ordenada)
"""


"""
def calcula(a):
	return a[0]

#def main():
print (calcula ([4,2]))

#main()		
"""
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


"""
def quadrado (l):
	return l*l
		
def triangulo (b,h):
	return b*h/2
		
def trapezio (B,b,h):		
	return ((B+b)*h)/2

def main():
	figura=input("Digite: 1-Quadrado / 2-Triangulo / 3-Trapezio: \n")
	
	if figura=="1":
		print ("Voce escolheu quadrado")
		l=int(input("Quanto mede o lado: "))
		print ("A area da figura eh",quadrado(l))
	
	if figura=="2":
		b=int(input("Quanto mede a base: "))
		h=int(input("Quanto mede a altura: "))
		print (triangulo(b,h))
	
	if figura=="3":
		B=int(input("Quanto mede a base maior: "))
		b=int(input("Quanto mede a base menor: "))
		h=int(input("Quanto mede a altura: "))
		print (trapezio(B,b,h))

main()	
"""


"""
n=int(input("Tabuada de multiplicação de qual base? "))

for i in range (1,11):
	print (n,"x",i,"=",n*i)
"""




"""
JAVA
class Teste {
	public static void main (String[] args) {
		System.out.println(2);
	}
}

PYTHON
print (2)
"""

"""
class Pessoa:
	def __init__ (self, idade, nome):
		self.idade=idade
		self.nome=nome

p1=Pessoa(23,"joao")
print (p1.idade)		
#print
"""
"""
dados=(input("Digite as temperaturas dia a dia separadas por espaço: \n"))
lista=dados.split(" ")
lista_num=[]

for i in lista:
	lista_num.append(float(i))

menor=lista_num[0]
for j in lista_num:
	if j<menor:
		menor=j
print ("Menor: ", menor)		

maior=lista_num[0]
for k in lista_num:
	if k>maior:
		maior=k
print ("Maior: ", maior)			

soma=0
media=0
cont=0
for l in lista_num:
	soma=soma+l
	cont=cont+1
media=soma/cont
print ("Media: ", media)			

inferior=lista_num[0]
cont1=0
for m in lista_num:
	if m<media:
		cont1=cont1+1
print ("Dia < Media: ", cont1)			
"""

"""
cont=0
cont_acima=0
soma=0
n=int(input("Informe a quantidade de alunos: "))

print ("Informe as notas dos alunos: ")
nota=0
lista_notas=[]
while (cont<n):
	nota=int(input())
	soma=soma+nota
	cont=cont+1
	lista_notas.append(nota)
media=soma/n

for i in lista_notas:
	if i>media:
		cont_acima=cont_acima+1

print ("A media da turma eh",media)
print ("Ficaram acima da media:",cont_acima,"alunos")
"""

# -*- coding: utf-8 -*-
#!/usr/bin/python



"""
soma = 0
for i in range (1,11):
	if (i%2==0):
		soma += i
		print (soma)
		print (i)
"""







"""
cont = 0
print (0*"x")
print (1*"x")
print (2*"x")

cont = 0
for i in "jocelio":
	print (cont*" ",i)
	cont += 1

print ("j")
"""


"""
for i in range (1,4):
	print (i)
	for j in range (6,9):
		print (j)
"""


"""
i=1
fatorial=1

for i in range(1,11):
	fatorial=fatorial*i
	print (fatorial)

print (i)
"""


"""
i=0
while (i<10):
	print (i)
	i+=1
print ("x")
print (i)
"""


"""
from tkinter import *

class Application:
    def __init__(self, master=None):
		self.widget1 = Frame(master)
		self.widget1.pack()
		self.msg = Label(self.widget1, text="Primeiro widget")
		self.msg.pack ()
root = Tk()
Application(root)
root.mainloop()
"""

"""
for i in "jocelio":
	print (i)
print (len("jocelio"))
"""


"""
print (2), print (), print (3)
print ()
"""

""" 
import threading
import time
 
def worker(message):
    for i in range(5):
        print (message)
        time.sleep(1)
 
 
t = threading.Thread(target=worker,args=("thread sendo executada",))
t.start()
while t.isAlive():
    print ("Aguardando thread")
    time.sleep(5)
 
print ("Thread morreu")
print ("Finalizando programa")
"""

"""
def teste1 (a):
	return a[0]+a[1]
	
def teste2 (c,d):
	return c,d #tupla
	
a=teste2(6,8)
print (a)
print ()
print ("x")
print (teste1(teste2(6,8)),"s")
"""

"""
def ex (a):
	return a*10	


print (ex (2))
"""	


"""
a=["a","b","c"]
print (",".join(a))
"""


"""
texto = "Eu quero dinheiro"
txt = []
for i in texto:
	if i=="e":
		txt.append ("8")
	else:
		txt.append (i)

a=",".join(txt)
b=",".join(a)
print (a)		
"""


"""
lista=[2,7,8,5,20,13,16,14]

lisM4=[]

for n in lista:
	if n%4 == 0:
		lisM4.append(n)
lisM4.sort()
print (lisM4)
"""


"""
print (17%9)
"""

'''
n=2
#n=input("Digite o valor: ")
print (n*6)
'''


"""
a=int(input("Digite o primeiro número: "))
b=int(input("Digite o segundo número: "))
	
x=(a-b)/a	

print("O valor de x na equação é:",x)
"""

"""
a="2-j"
b=a.split("+")
print (a)
print (b)
"""

"""
eq=input("Digite a equação: ")
eq1=eq.split("x")
eq2=eq1[1].split("+")
eq3=eq2[1].split("=")

a=int(eq1[0])
b=int(eq3[0])
c=int(eq3[1])


x=(c-b)/a

print("O valor de 'x' na equação é:", x)
"""


"""
a=int(input("Digite o primeiro termo: "))
b=int(input("Digite o segundo termo: "))
c=int(input("Digite o terceiro termo: "))

x=(c-b)/a

print("O valor de 'x' na equação é:", x)
"""


"""
lis=[2,1,3]
lis.sort()
print (lis[0])
"""
"""
op="s"
while 1:
	if op == "n":
		break
	n=int(input("Digite um número: "))
	if n%2==0:
		print ("par")
	else:
		print("impar")
 	
	while 1:	
		op=input("Deseja continuar? (s/n): ")
		if op == "n":
			break
		if op!="n" and op!="s":
			print ("opcao invalida")
			continue
		if op == "s":
			break
"""	
		
	
"""
n=128
a=str(n)
if int(a[len(a)-1]) in [0,2,4,6,8]:
	print ("par")
"""

"""
for i in "123":
	print (i)
"""


"""
def media (n, lista):
   
    soma=0
    medianotas=0
   
    for i in lista:
        soma += float(i)
        
    
    medianotas=soma/n
    return medianotas    
    
def main():
        
	n=0; lista=["5.0","3.0","7.0"];

	n=3
	resultado = media (n, lista)

	print ("%.2f" % resultado)

main()
"""



"""
n=int(input("Digite a quantidade de termos: "))
valor=(input("Digite os termos com espaço entre eles: "))

lista=valor.split()
print(lista)
soma=0

for i in lista:
	soma=soma+int(i)
	
med=soma/n
print("A média é:",med)	
"""	
	 

"""
n=int(input("Digite a quantidade de termos: "))
soma=0
valor=0

for i in range(n):
	valor=int(input("Digite o termo: "))
	soma=soma+valor
	
med=soma/n
print("A média dos termos é",med)	
"""


"""
class tst:
	def __init__ (self,a,b):
		self.a = a
		self.b = b
		
	def preco (self,a):
		return self.a*10
		
	def p2 (self,a):
		return self.b*20
"""		
"""
	def p(self, a, b):
		
		a=5
		b=6
		
		self.p = tst (a,b)
		
		print (p)
		res = self.preco (a)
		print (res)
"""
"""
t1 = tst(5,6)
print (t1.p2(None))
"""


	
"""
a,b=2,3
print (a,b)
lista=[1,2,3]
lista[2]=99
print (lista)
"""


"""
inf=int(input("Digite o valor inferior: "))
sup=int(input("Digite o valor superior: "))

lista=[]
soma=0			

for i in range(inf,sup+1):
	if i%2!=0:
		lista.append(i)
		soma=soma+i

print("A soma dos ímpares entre",inf,"e",sup,"é",soma)			
"""



"""
inf=int(input("Digite o valor inferior: "))
sup=int(input("Digite o valor superior: "))

lista=[]

for i in range(inf,sup+1):
	lista.append(i)

for j in lista:
	if j%2==0:
		lista.remove(j)
soma=0			
for k in lista:
	soma=soma+k

print("A soma dos ímpares entre",inf,"e",sup,"é",soma)				
"""


















"""
tab="cara de peixe morto"
print(len(tab))
print(tab[8])
print(tab.split())
print(tab)
"""










"""
lista=[12,34,664,22,11,3,32]
print(len(lista))
print(lista[3])
lista.sort()
print(lista)
"""









"""
n=int(input("Digite um numero: "))

for i in range(30,n+1,4):
    print(i)
 """













"""
n=int(input("Um numero: "))
print (n*10)
"""






"""
for i in range (91,101,4):
	print (i)
"""


"""
n=int(input("Qual Tabuada você quer: "))
n1=int(input("Tamanho da tabuada: "))
tabuada=[]

for i in range(n1+1):
	tabuada.append(i)
print (tabuada)
"""








"""
tabuada=[0,1,2,3,4,5,6,7,8,9,]
for i in tabuada:
	print (i," x ",n," = ",n*i)
print()
tab=len(tabuada)
dig = 0

while dig<tab:
	print (dig," x ",n," = ",n*dig)
	dig+=1
"""







"""
n=10000000
a=0
while a<n:
	a+=1000
	print (a)
"""



"""
a="Yuritggbdkfhskfhskgshgkhj"
for i in a:
	print (i)
print()
print(len(a))
"""




"""
condicional - compara

laço - enquanto/para
"""





"""
a=2
b=4

a=input("Digite o primeiro valor: ")
b=input("Digite o primeiro valor: ")


if a>b:
	print (a)
else: 
	print (b)
"""







"""
lista = [1,2,3]

(lista[0:])
"""







"""
if lista[0]=="1":
	print (lista[0])
else:
	print ("Não")	
"""






"""
print (len(lista))

cont = 1

for i in range (5):
	cont += 1
	

print (cont)
"""





"""
def a (a):
	print (a)
	return a


print(a(5))
"""





"""
class A:
	pass
	
class A:	
	pass

obj=A()
print (obj)
"""

"""
x=3
y=4

soma=0
cont=0
rang=x
passo=x
while cont<(y-1):
	soma=0
	for i in range (rang):
		soma=soma+passo
		
	passo=soma	
	
	cont+=1
	
print (soma)
"""


"""
from time import *
from datetime import datetime

horario=datetime.now()
print(horario.hour)
print(horario.day)
#(second, month, year,day)
"""

'''
#PEGAR DATA E FORMATAR
data=str(datetime.now())
f='%Y-%m-%d %H:%M:%S.%f'
data_formatada=datetime.strptime(data, f)
print("{}/{}/{}".format(data_formatada.day,data_formatada.month,data_formatada.year))
'''


'''
from datetime import datetime

#Data em formato datetime e usa o strftime para fazer em str
data=(datetime.now())
print(data)#datetime
print(data.strftime("%d/%m/%Y"))#str
#08/10/2020

print()
#PEGAR DATA EM STR E FORMATAR E SAIR COMO DATETIME
data=str(datetime.now())
f='%Y-%m-%d %H:%M:%S.%f'
data_formatada=datetime.strptime(data, f)
print("{}/{}/{}".format(data_formatada.day,data_formatada.month,data_formatada.year))
print(type(data_formatada))#datetime
#8/10/2020

#Pegar só dia, mes, ano, em datetime
print()
data=(datetime.now())
print("{}/{}/{}".format(data.day,data.month,data.year))
print(type(data))#datetime
a="{}".format(data.day)
print(type(print("{}".format(data.day))))#NoneType
#8/10/2020
print(a)



from datetime import datetime
#USAR COMO STR PARA COMPARAR
data=(datetime.now())
print(data)#datetime
a=data.strftime("%d/%m/%Y")
print(a)#str
print(type(a))
#08/10/2020

if a=='08/10/2020':
	print('ok')
	
	
from datetime import datetime
from datetime import date

data_hoje=(date.today())
data_str = data_hoje.strftime('%d/%m/%Y')
print(data_str)
#08/10/2020
print(data_str[0:1])

print(int(data_str[0:2])*2)



#O QUE INTERESSA
from datetime import date

data_hoje=(date.today())
data_str = data_hoje.strftime('%d/%m/%Y')
print(data_str)
#08/10/2020
print(data_str[0:2]*2)
print(int(data_str[0:2])*2)


	

'''




"""
x=17
y=23
a=1

lista=[1,2,3,4,5,6,7,8,9,10]			

for i in lista:
	if (i%3==0):
		print (i)	
	
print(10%2)	
"""


"""
x=10
y=3

def eDivisivel(a,b):
	if a%b==0:
		return True
	else:
		return False	

def eDivisivel(a,b):
	return a%b==0
		
if eDivisivel(x,y):	
	print ("Par de números OK")
else:	
	print ("Par de numeros não serve")
"""

"""
fact=
def soma(a,b):
	return a+b

soma1=lambda a,b:a+b

print (soma(3,6))
print (soma1(3,6))
"""


"""	
msg="adalberto"

if "ld" in msg:
	print ("ok")
	
lista=[2,1,4,5,3]	
print (msg[-1])
print(lista[-1])
"""



"""
relacao=[2,6,1,3,5,9,4]

#print(relacao[-12])
"""

"""
def soma(a,b):
	return a+b

soma2=lambda n1,n2:n1+n2

print(soma(3,4))
print(soma2(5,6))


numeros = [0,2,3,4,5,7]
pares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
# Exibe os números
for par in pares:
    print(par)
    
numeros = [0,2,3,4,5,7]
pares = filter(lambda valor: valor % 2 == 0, numeros)
for par in pares:
    print(par)    
"""


"""
#metodos de listas:
append
insert
pop
sort
reverse
index
count
remove



"""


"""
def' anos(x):
	return x
	
def meses(x):
	return x*12
	
def dias(x):
	return x*30
	
def horas(x):
	return x*24
	
def min(x):
	return x*60
	
def seg(x):
	return x*60
"""


"""
p=3 #dias
p1=90 
r=5 #minutos
resp=""
#p=input("Unidade que você tem (1-anos 2-meses 3-dias 4-horas 5-minutos 6-segundos) -> ")
#p1=input("Quantidade -> ")
print()
#r=input("Unidade que você quer (1-anos 2-meses 3-dias 4-horas 5-minutos 6-segundos) -> ")
print()

lista=[1,2,3,4,5,6]
iind=""
if p in lista:
	iind=lista.index(p)
lista[iind]=p1
jind=""
if r in lista:
	jind=lista.index(r)
lista[jind]=resp

for l in range(len(lista)):
	if l!=iind and l!=jind:
		lista[l]=0



for m in range(len(lista)):
	if lista[m]=="":
		lista_resp=lista[0:m]
		print(lista_resp)
		#print(sum[1,2,3,4])#lista_resp])
orig=[1,12,30,24,60,60]
soma=0

for i in (lista_resp):
	for j in orig:
		soma += i*j 
		orig.remove(j)
		continue
		#lista_resp[0]*1+lista_resp[1]*12+lista[2]*30+lista[3]*24+lista[4]*60+lista[5]*60
		
print(soma)
"""

"""
lista=[1,2,3,4]
for i in lista:
	for j in lista:
		print (i,)	
"""


"""
print(2%3)	

print(2%4)	
print(2%5)	
print(2%6)	
print(1%3)	
print(1%3)	
"""

"""
a=float(5/2)
print (a)
"""


"""
import aiml
import os

os.chdir('C:/Python24/curso/testeAIML') #muda para o diretório que contém os arquivos da AIML standard
ai = aiml.Kernel() #inicialização
ai.learn('std-startup.xml') #abre o arquivo principal da AIML (que faz referências aos outros)
ai.respond('load aiml b') #faz com que os outros arquivos da AIML sejam carregados

while (1==1):
    frase = raw_input('Fale algo ao bot em english:')
    print ("Resposta do bot: %s" % ai.respond(frase))
"""

"""
class Conta:
	def __init__ (self,a,b):
		self.a=a
		self.b=b
			
	def imprimir(self):
		return (self.a*self.b)

a=2;b=5		
obj=Conta(a,b)		
res=obj.imprimir()
print(res)		


class Conta:
	def __init__ (self,a,b):
		self.a=a
		self.b=b
			
	def imprimir(self):
		return (self.a*self.b)

a=2;b=5		
obj=Conta(a,b)		
res=obj.imprimir()
print(res)		
"""



"""
rom
orm
omr

#omr
mor
mro

#mro
rmo
#rom
"""

"""
lista=[[1,2],[1,3],[1,2]]
print(lista.count([1,2]))
"""

"""
lista=[1,2,3,1,4,3,3,5]
lst=[]
cont=0
n=0

a=lista[0]
for j in lista:
	for i in lista:
		if j==i:
			cont+=1
	if j in lst:
		break	
	if cont>1:
		print(j,"está repetido",cont,"vezes")
		lst.append(j)
	cont=0
"""

"""
lista=[1,2,3]
lst=lista[:]
lista[0]=222
print (lst)
"""

"""
a="123"
b=a.split("")
#res=lista.split()
#res=sum(lista)
#print(res)
print(b)
"""

"""
a=2
for i in range(5):
	if a == 2:
		print(33)
		continue
	print(100)	
"""




"""
#PERMUTAÇÃO

seq=input("Digite a sequencia para permutar (Ex: '2345' ou '012' ou 'roma') -> ")
lista_orig=[]
for i in seq:
	lista_orig.append(i)

def fat(n):
	if n==0 or n==1:
		return 1
	return n*fat(n-1)
npermut=fat(len(lista_orig))
elem=len(lista_orig)
conj=int(npermut/len(lista_orig)/(len(lista_orig)-1))

print('INICIO')
print()
n=0
m=0
lista_permut=[]
indj_1=1
indj_2=2
indi_1=2
indi_2=3
indh_1=0
indh_2=1
listan=[]
lista=lista_orig[0:]
for j in range(len(lista_orig)-1):
	for i in range(conj):
		lista_interm=lista[0:]
		for h in range(len(lista_orig)):
			
			print("".join(lista))
			n+=1
			lista_permut.append(lista[0:])
			
			if (indh_2)>(len(lista_orig)-1):
				print('  ')
				indh_1=0
				indh_2=1
				break
			lista[indh_1],lista[indh_2]=lista[indh_2],lista[indh_1]
			indh_1+=1
			indh_2+=1
		if (indi_2)>(len(lista)-1):
			indi_1=2
			indi_2=3
		if len(lista_orig)<4:
			continue	
		lista=lista_interm[0:]	
		lista[indi_1],lista[indi_2]=lista[indi_2],lista[indi_1]
		indi_1+=1
		indi_2+=1
	if (indj_2)>(len(lista_orig)-1):
		lista=lista_orig[0:]
		indj_1=1
		indj_2=2
		break
	lista=lista_orig[0:]	
	lista[indj_1],lista[indj_2]=lista[indj_2],lista[indj_1]
	indj_2+=1

print('FINAL')
print()
lst=[]
for i in range(n):
	lst.append("".join(lista_permut[i]))
print("Lista de permutações: ",lst)
print("Qtde. itens na lista de permutações: ",len(lista_permut))
print("Número de permutações calculado: ",npermut)
print("Número de permutações do 'n': ",n)
"""



"""
print("Olá Francisco\n","estou aqui")
print("Olá Francisco","\n estou aqui")
"""


"""
lista=[2,45,34,6]

for i, valor in enumerate(lista):
	print(i,':',valor)
"""

"""
lista=[1,12,3,40,5]
print(list(reversed(lista)))
print(lista)

a=lista.sort()
print(lista)	
print(a)
"""


"""
a = [1,2,3]
b = [4,5,6]
for i,j in zip(a,b):
	print("Sum of a and b is", i+j)
#Sum of a and b is 5
#Sum of a and b is 7
#Sum of a and b is 9



square_list = [number*number for number in range(1,20) if number%2==0]
print(square_list)
#[4, 16, 36, 64, 100, 144, 196, 256, 324]
"""


"""
No topo dito Python também há muitas bibliotecas externas que possuem um recurso
 melhor do que qualquer linguagem de programação. 
 Estou nomeando algumas das principais bibliotecas abaixo

Numpy
Pandas
Scikit-Learn
Scrapy
Beautiful Soup
OpenCV
Requests
Matplotlib
Pygame
SQLAlchemy
"""

"""
a=2
b=3
c=4

a,c,b=b,a,c
print(a,b,c)
"""


"""
a = [number*number for number in range(1,20) if number%2==0]
print(a)
#[4, 16, 36, 64, 100, 144, 196, 256, 324]
"""


"""
lista_pares = [number for number in range(1,20) if number%2==0]
print(lista_pares)
#[2, 4, 6, 8, 10, 12, 14, 16, 18]
"""


"""
import time, sys
from datetime import datetime

lista_tmp=[]
for i in range(10):
	a=1
	tempo1=str(datetime.now())
	if a==1:
		pass #print (a)
	if a==2:
		print (a)
	if a==3:
		print (a)
	if a==4:
		print (a)
	if a==5:
		print (a)
	if a==6:
		print (a)
	if a==7:
		print (a)
	if a==8:
		print (a)
	if a==8:
		print (a)
	if a==10:
		print (a)
	tempo2=str(datetime.now())
	f='%Y-%m-%d %H:%M:%S.%f'
	dif1=(datetime.strptime(tempo2,f)-datetime.strptime(tempo1,f))
	#print(dif1)

	a=1
	tempo1=str(datetime.now())
	if a==1:
		pass #print (a)
	elif a==2:
		print (a)
	elif a==3:
		print (a)
	elif a==4:
		print (a)
	elif a==5:
		print (a)
	elif a==6:
		print (a)
	elif a==7:
		print (a)
	elif a==8:
		print (a)
	elif a==8:
		print (a)
	else:
		print (a)
	tempo2=str(datetime.now())
	f='%Y-%m-%d %H:%M:%S.%f'
	dif2=(datetime.strptime(tempo2,f)-datetime.strptime(tempo1,f))
	#print(dif2)

	comp=(str(dif1),str(dif2))
	lista_tmp.append(comp)
	
print(lista_tmp)	


print("xxxxxxx")

import time, sys
from datetime import datetime

n=10000
tempo1=str(datetime.now())
for i in range(1,n+1):
	if n%i==0:
		pass #print(i)
tempo2=str(datetime.now())
f='%Y-%m-%d %H:%M:%S.%f'
dif1=(datetime.strptime(tempo2,f)-datetime.strptime(tempo1,f))


print()

tempo3=str(datetime.now())
for i in range(1,n+1):
	if i>(n/2):
		break
	if n%i==0:
		pass #print(i)
#print(n)
tempo4=str(datetime.now())
f='%Y-%m-%d %H:%M:%S.%f'
dif2=(datetime.strptime(tempo4,f)-datetime.strptime(tempo3,f))
print()
print(dif1)
print(dif2)
"""


"""
from datetime import datetime

tempo3=str(datetime.now())
f='%Y-%m-%d %H:%M:%S.%f'
t1=(datetime.strptime(tempo3,f))

from datetime import datetime
tempo4=str(datetime.now())
f='%Y-%m-%d %H:%M:%S.%f'
t2=(datetime.strptime(tempo4,f))

print(t2-t1)
"""

'''
k
'''

"""
input("Pressione ENTER para continuar...")
"""


"""
nome=input('Digite a palavra -> ') #'besteirada'
#print(len(nome))
#print(nome[10])
cont=0
repet=[]
for i in nome:
	for j in nome:
		if j==i:
			cont+=1
	if cont>1:
		if i not in repet:
			repet.append(i)	  
	cont=0
print(repet)		
"""


"""
for i in range(int(3.5)):
	print(i)
"""


"""
#ORDENAÇÕES
from time import *
from datetime import datetime

#ORDENAÇÃO 1
lista=[3,6,1,8,7,5] # DÁ ERRO SE FOR QTDE. ÍMPAR
lista_ord=[0,0,0,0,0,0]
nmenor=0
nmaior=-1
menor=lista[0]
maior=lista[0]	

tempo1=str(datetime.now())
for j in range(len(lista)):
	
	for i in range(len(lista)):
		if lista[i] < menor:
			menor=lista[i]
		if lista[i] > maior:
			maior=lista[i]
	lista_ord[nmenor]=menor
	lista_ord[nmaior]=maior
	lista.remove(menor)
	lista.remove(maior)
	nmenor+=1
	nmaior-=1
	if len(lista)==0:
		break
	menor=lista[0]
	maior=lista[0]

print(lista_ord)	
tempo2=str(datetime.now())
f='%Y-%m-%d %H:%M:%S.%f'
dif12=(datetime.strptime(tempo2,f)-datetime.strptime(tempo1,f))


#ORDENAÇÃO 2
lista=[3,6,1,8,7,5]
lista_ordenada=[]

tempo3=str(datetime.now())
for j in range(len(lista)):
	menor=lista[0]
	for i in lista:
		if i<menor:
			menor=i
	
	lista_ordenada.append(menor)
	lista.remove(menor)

print(lista_ordenada)	
tempo4=str(datetime.now())
f='%Y-%m-%d %H:%M:%S.%f'
dif34=(datetime.strptime(tempo4,f)-datetime.strptime(tempo3,f))


#ORDENAÇÃO 3
lista=[3,6,1,8,7,5]
lista_ordenada=[]

tempo5=str(datetime.now())
for j in range(len(lista)):
	menor=lista[0]
	for i in lista:
		if i in lista_ordenada:
			continue		
		if i<=menor:
			menor=i
	
	lista_ordenada.append(menor)

print(lista_ordenada)	
tempo6=str(datetime.now())
f='%Y-%m-%d %H:%M:%S.%f'
dif56=(datetime.strptime(tempo6,f)-datetime.strptime(tempo5,f))

print(dif12)
print(dif34)
print(dif56)
"""


"""
import msvcrt
print('Pressione qualquer tecla para continuar...')
msvcrt.getch()
"""


"""
from decimal import Decimal

ganhos=5*(Decimal('99.91'))
gastos=3*(Decimal('110.10'))
lucro=gastos-ganhos

print(ganhos)
print(gastos)
print(lucro)
"""


"""
for i in range(1,11):
	print(i)
"""

"""
j=1
while j<11:
	print(j)
	j+=1	
"""


"""
import time
slp=2
time.sleep(slp)
print(123)
"""



"""
nome='rapadura'
print(nome[-4:-1])
"""


"""
class Teste():
	def funcao(self,n):
		print(n*10)

a=16
obj=Teste()

obj.funcao(a)
print(type(a))
print(type(obj))
"""


"""
#METODOS STRINGS
frase='os meus dedos'
print(frase.lower())
print(frase.title())
print(frase.upper())
print('é'.replace('é','eh'))
print('é, é é'.replace('é','eh'))
print('é é é'.replace('é','eh',1))  # só substitui o primeiro
"""


"""
def teste (a,b):
	return (a*b)
"""


"""
#IMPORTAÇÃO
arquivo pessoa.py
classe Pessoa
import pessoa  - vai importar o módulo pessoa. Um arquivo é um módulo
para usar a classe Pessoa teria que fazer: var=pessoa.Pessoa() - do módulo pessoa a classe Pessoa

from pessoa import Pessoa
tá importando apenas a classe Pessoa do módulo pessoa


EXEMPLOS:
from tstt import A  #tstt é um arquivo, "A" é a classe
obj3=A()
print(obj3)


from tstt import *  #tstt é um arquivo, "A" é a classe
obj2=A()
print(obj2)

import tstt   #tstt é um arquivo, "A" é a classe
obj1=tstt.A()
print(obj1)


"""


"""
####from r import * #Teste
####import r
import r.Teste
#res=r.Teste()  # nesse caso usa o arquivo antes da classe para instanciar
res=Teste()
a=res.teste(5,"2")	
print(a)	
print(res.teste(5,"2"))
"""


"""
import r

x=r.Teste() 
y=r.Teste()
z=r.Ttt()

a=x.antes(5,2)	
b=y.novo(5,2)
c=z.moderno(5,2)
print(a)
print(b)
print(c)	
print(x.antes(5,2))
"""

"""
from r import Teste

x=Teste() 
y=Teste()
#z=Ttt()

a=x.antes(5,2)	
b=y.novo(5,2)
#c=z.moderno(5,2)
print(a)
print(b)
#print(c)	
print(x.antes(5,2))
"""
"""
from r import *

x=Teste() 
y=Teste()
z=Ttt()

a=x.antes(5,2)	
b=y.novo(5,2)
c=z.moderno(5,2)
print(a)
print(b)
print(c)	
print(x.antes(5,2))
"""


"""
import json

conhecidos=['will','arnaldo','joao']

memoria = open('teste.json','w')
json.dump(conhecidos,memoria)
memoria.close()

memoria=open('teste.json','r')
print(json.load(memoria))
memoria.close()
"""

"""
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
#jeito errado:
f = open("data.txt", "w")
# codigo usando o arquivo f
f.close()

#jeito certo, sem o with:
try:
   f = open("data.txt", "w")
   # codigo usando o arquivo f
finally:
   f.close()

#jeito certo com o with (recomendado):
with open("data.txt", "w") as f:
   # codigo usando o arquivo f
"""
"""
ABRINDO VÁRIOS ARQUIVOS DE UMA VEZ COM WITH
with open('a.txt') as a, open('b.txt') as b, open('c.txt') as c:
    #faca_algo_aqui

O READLINES ABRE CADA ARQUIVO EM UMA LISTA
conteudo_a = a.readlines()
conteudo_b = b.readlines()
conteudo_c = c.readlines()
"""

"""
arquivo = open('arquivo.txt','r')
#print(arquivo.read())  # usa um jeito ou o da linha abaixo
a=(arquivo.read())
print(a)
arquivo.close()

print(1)

arquivo = open('arquivo.txt','r')
#print(arquivo.readline())
a=(arquivo.readline())
print(a)
arquivo.close()

print(2)

arquivo = open('arquivo.txt','r')
#print(arquivo.readlines())
a=(arquivo.readlines())
print(a)
arquivo.close()

print(3)

arquivo = open('arquivo.txt','r')
for linha in arquivo:
	linha=linha.rstrip() # eliminar as linhas em branco
	print(linha)
arquivo.close()

print(4)

print(arquivo.closed)   # para saber se o arquivo foi fechado True ou False

print(5)

arquivo = open('arquivo.txt','r')
for linha in arquivo:
	linha=linha.rstrip()
	linha=linha.split(' ') # transforma cada linha em uma lista
	print(linha)
arquivo.close()
"""

'''
arquivo = open('nome.txt', 'r')
conteudo = arquivo.readlines()
conteudo.append('Nova linha')  
arquivo.close()

arquivo = open('nome.txt', 'w')
arquivo.writelines(conteudo)  
arquivo.close()

arquivo = open('nome.txt', 'r'
print(arquivo.read())
arquivo.close()
'''





"""
def teste(a,b):
	if (a+b) == 5:
		return True
	else:
		return False

a=4
b=2

"""
"""
if	teste(a,b) == True:
	print('Verdadeiro')
else:
	print('É Falso')	
"""
"""
if teste(a,b):
	print('Verdadeiro')
else:
	print('É falso')	
"""


"""
lista=["1",'2','a',"b",5]
print(lista)
for i in lista:
	print(i,type(i))
"""

"""
a=2
try:
	open('fdfdfd','r')
	print(a)
except NameError:	#FileNotFoundError
	print('a variavel nao foi definida')
	
	
def divide(x,y):
	return x/y
try:
	#a=divide('2',1)
	a=divide(2,1)	
#except (Exception):
#	print('Erro')
except ZeroDivisionError:
	print('Divisão por Zero')
except TypeError:
	print('Tipos não permitidos')	
else:
	print('res:',a)

"""


"""
#DICIONÁRIOS
dic={}
dic['Carro'] = 'azul'
dic['Preço'] = 3000
dic['Ano'] = {'Fabricação': 2015}
print(dic['Ano']['Fabricação'])
"""


"""		
#EVAL - interpreta um código passado para o python em forma de texto
print(eval('1+1'))
print(eval('4<6'))
"""
#não eval('1'+'1')
"""
"não -> print(eval(1+1))"
"""
"""
frase='1+2'
resp=str(eval(frase))
resp1=eval(str(frase))
print(resp,type(resp))
print(resp1,type(resp1))
"""
"""
print(eval('"oi"'))
#oi
"""
"""
frase='oi tudo bem!'
def escuta(frase=None):
	if frase == None:
		frase = input('Digite a frase: ')
	return frase
print(escuta('aaa'))
"""


"""
#abrindo arquivos do sistema operacional
import sys
print(sys.platform) # identifica o SO

import os
os.startfile("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
os.startfile('www.globo.com')



#SE FOR LINUX
import subprocess as s
print(s)
s.Popen('chromium') # não precisa o caminho completo
s.Popen(['xdg-open','http://www.google.com']) # para abrir sites ou arquivos com extensão - programas basta o nome dele
"""

"""
frase='eu quero me trepar no coqueiro'
frase=frase.replace(' coqueiro','')
print(frase)
#aqui tirou o coqueiro e espaço antes por nada.
"""


"""
casos = int(input())

for i in range(casos):
	ncasos_valor=input()
	precos=input()
	lis1=ncasos_valor.split()
	lis2=precos.split()
	for j in range(len(lis1)):
		lis1[j]=int(lis1[j])
	for k in range(len(lis2)):
		lis2[k]=int(lis2[k])
"""


#pip - instalador de pacotes de módulos externos
#sudo pip install telepot - no Linux
# no Windows - 
#    pip install 'nome do módulo'   OU  python -m pip install 'nome do módulo' - sem aspas

"""
lista=['1','2','3']
print(lista)
lista_int=[]
for i in lista:
	i=int(i)
	print(i,type(i))
	lista_int.append(i)

#for i in range(len(lista)):
#	lista[i]=int(lista[i])
	
print(lista_int)
"""


"""
#with (uif) é uma maneira mais simples de lidar com arquivos, streaming, etc
with open('test.txt','w') as arquivo:
	arquivo.write('teste te escrita')
	#não precisa fechar o arquivo

with open('teste.txt','w') as w:
	w.write('novo teste te escrita')
"""


"""
frase1='ola'
frase2='tudo '+"2"+' ok'
frase3='bem'

n=1
while n<=3:
	print(eval('frase'+str(n)))
	n+=1

print(eval('4<6'))
"""


################################################################################# VOZ E TEXTO
#TRANSFORMAR TEXTO EM VOZ - MANEIRAS  # usando pip install e o 'pyttsx'

# o sphinx transforma voz em texto
# o gTTS usa a API do google e sintetiza voz (transforma texto em voz) 
# o pyttsx sintetiza voz (transforma texto em voz)


#######################################
#TRABALHANDO COM TEXTO E VOZ

'''
####IMPORTS GERAIS
import os
import engineio 
import speech_recognition as sr	
import pyttsx3
from gtts import gTTS
from playsound import playsound
####
'''

'''
#PARA CRIAR AUDIOLIVROS	
import pyttsx3
def cria_audio(audio): 
	en = pyttsx3.init()
	en.setProperty('voice',b'brazil')
	en.say(audio)  # en.say('O mais belo Hello'+audio)
	en.runAndWait() 
audio="\
primeiro, bata bem os ovos no liquidificador.\
Acrescente o leite condensado e o leite, e bata novamente.\
"
ou
audio="""
primeiro, bata bem os ovos no liquidificador.\
Acrescente o leite condensado e o leite, e bata novamente.\
"""


cria_audio(audio)
'''


'''
#TRASNFORMA TEXTO EM VOZ
en = pyttsx3.init()
en.say('disse Hello world')
en.say('Nice to meet you')
en.runAndWait()

en = pyttsx3.init()
en.setProperty('voice',b'brazil')
en.say('Olá Hello')
en.runAndWait()
'''


'''
#DIALOGO
def cria_audio(audio): 
	en = pyttsx3.init()
	en.setProperty('voice',b'brazil')
	en.say(audio)  # en.say('O mais belo Hello'+audio)
	en.runAndWait() 

def ouvir_microfone():
	ouvido = sr.Recognizer()
	with sr.Microphone() as source:
		while True:
			ouvido.adjust_for_ambient_noise(source)
			audio = ouvido.listen(source)
			try:
				frase = ouvido.recognize_google(audio,language='pt-BR')
				return frase
			except sr.UnknownValueError:
				cria_audio('Infelizmente não entendi... Repita por, favor')
		
cria_audio('Vamos iniciar um diálogo: ')
frase=''
pede=cria_audio('Olá, tudo bem? Diga o seu nome: ')
nome = ouvir_microfone()
cria_audio('Olá '+nome+','+' diga algo para ver se eu te entendo!')
frase = ouvir_microfone()
cria_audio('Entendi '+nome+', '+'você disse: '+frase+'. Obrigada, depois nos falamos para eu te conhecer mais!')
'''


'''
#PERGUNTA E RESPONDE EM VOZ
import speech_recognition as sr
def ouvir_microfone(): #Funcao responsavel por ouvir e reconhecer a fala
	microfone = sr.Recognizer() #Habilita o microfone para ouvir o usuario
	with sr.Microphone() as source: 
		microfone.adjust_for_ambient_noise(source) #Chama a funcao de reducao de ruido disponivel na speech_recognition
		print("Diga alguma coisa: ") #Avisa ao usuario que esta pronto para ouvir
		audio = microfone.listen(source) #Armazena a informacao de audio na variavel
	try:
		frase = microfone.recognize_google(audio,language='pt-BR') #Passa o audio para o reconhecedor de padroes do speech_recognition
		print("Você disse: " + frase) #Após alguns segundos, retorna a frase falada
		return frase
	except sr.UnknownValueError: #Caso nao tenha reconhecido o padrao de fala, exibe esta mensagem
		print("Não entendi")
ouvir_microfone()
'''






'''
#TRANSFORMAR VOZ EM TEXTO - AGORA EM PORTUGUÊS
import speech_recognition as sr	
rec = sr.Recognizer() # o módulo tem um reconhecedor	
with sr.Microphone() as fala:
	print('Fale agora:')
	frase = rec.listen(fala)
#SE FOSSE  PARA INGLÊS SERIA ABAIXO:
#print(rec.recognize_google(frase))
print(rec.recognize_google(frase, language='pt'))
print('fim')
'''
##################################







"""
#DIGITAR EM VÁRIAS LINHAS
string = "\
uma linha \
outra linha\
"
print (string)

string = '\
uma linha \
outra linha\
'
print (string)

string = ('uma linha '
'outra linha')
print (string)

string = ('uma linha ' +
'outra linha')
print (string)

lista=[1,2,3
,7,9,
10,11]
print(lista)

#uma linha outra linha
"""


"""
#EXCEÇÕES
ZeroDivisionError - dividir por zero
NameError - variável não definida
TypeError - somar int e str

exceções devem ser instâncias de uma classe derivada de BaseException.
Os programadores são incentivados a derivar novas exceções da classe Exception ou de uma de suas subclasses, e não de BaseException.

while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except (Exception): # ou (RuntimeError, TypeError, NameError)
        print("Oops!  That was no valid number.  Try again...")

"""


"""
a=2
print('oi',a)
print('oi ',a)
print('oi'+str(a))
print('oi '+str(a))
"""


'''
a
'''

"""
class Pai():
	def __init__(self):
		pass
		
	def teste1(self,a):	
		print("Imprimindo",a)

#HERANÇA - HERDA OS MÉTODOS DA CLASSE PAI		
class Filha (Pai):
	pass
	
	def teste1(self,b):
		print('Agora imprimindo',b)

#POLIMORFISMO -  MUDA O MÉTODO SÓ ONDE INTERESSA
tst=Pai()
tst.teste1(1)		
tst1=Filha()
tst1.teste1(2)
tst1=Filha()
tst1.teste1(3)


#EXEMPLO DE SUPER

class Pai():
	def __init__(self):
		pass
		
	def teste1(self,a):	
		return "Imprimindo "+str(a)
	
	def tst(self,b):
		return 'Método da classe Pai '+str(b)
	
class Filha (Pai):
	pass
	
	def teste1(self,b):
		if b<10:
			return 'Agora imprimindo '+str(b)
		return super().teste1(b)

tst1=Filha()
res=tst1.teste1(4)
print(res)
res=tst1.teste1(14)
print(res)
res=tst1.teste1(7)
print(res)
res=tst1.teste1(12)
print(res)


"""		

	

"""
a=28
if a==2:
    print('Ok')
else:
	print('Não')    	
"""

"""
a,b=2,3
print(b)
a,b=[2,3]
print(b)
a;b=33
print(a)
print(b)
"""


"""
lista=[None,]
print(lista)
"""

"""
n1=int(input('Digite o primeiro numero: '))
n2=int(input('Digite o segundo numero: '))

if n1>n2:
	print('O maior é',n1)
if n1<n2:
	print('O maior é',n2)	
if n1==n2:
	print('Os valores são iguais')
"""


"""
#t=int(input('Qual tabuada você deseja-> '))
for j in range(1,11):
	print('Tabuada de:',j)
	for i in range(1,11):
		print(i,'x',j,'=',i*j)
	print()
"""	



"""
lista=[1,2,3]
lista_modificada=[x**2 for x in lista]
print (lista_modificada)



a, b, c, d = 1, 2, 3, 4
if a == 1 and b == 2 and c == 3 and d == 4:
    print('all True!')

condicoes = [
    a==1, 
    b==2, 
    c==3, 
    d==4
]

if all(condicoes):
    print('todas as condições eram verdadeiras!')
    
if any(condicoes):
    print('alguma condição era verdadeira!')    


a, b = 10, 5
a, b = b, a


dicionario = {'Maria': '1235'}
try:
    valor = dicionario['chave'] 
except KeyError:
    valor = None
valor = dicionario.get('chave')
print(valor)

valor = dicionario.get('chave', 123)
# caso a chave não exista:
print(valor)



lista = ['a', 'b', 'b', 'c', 'a', 'b']
lista_modificada = [0, 1, 1, 1, 0, 1]
def modifica_valor(lista):
    lista_modificada = []
    for x in lista:
        if x == 'a':
            lista_modificada.append(0)
        else:
            lista_modificada.append(1)

def modifica_valor(x):
    if x == 'a':
        return 0
    return 1       
lista_modificada = []
for x in lista:
    lista_modificada.append(modifica_valor(x))
transform = lambda x: 0 if x == 'a' else 1
# type(transform)
#>>> function
lista_transform = list(map(transform, lista))
# lista_transform
#>>> [0, 1, 1, 1, 0, 1]
"""


"""
numeros = [0,2,3,4,5,7]
pares = filter(lambda valor: valor % 2 == 0, numeros)
for par in pares:
    print(par)   
print(pares)
print(type(pares))

lista = []
for x in lista:
    print('dentro do loop')
else:
    print('dentro do else')
lista = [1, 2]

for x in lista:
    print('dentro do loop')
else:
    print('dentro do else')
# resultado
#'dentro do loop'
#'dentro do loop'
#'dentro do else'
"""

"""
lista=[1,2]
for x in lista:
    print(x)
else:
    print('Terminou')

frase = 'O que? Eu não quero frases com pontuações! Chega!'
frase_sem_pontuacao = ''.join(char for char in frase if char not in [ '!', '?'])
print(frase_sem_pontuacao)
"""

"""
print(isinstance('oi', str))
"""

"""
class A:
	def __init__(self):
		pass
		
	def calcula (self,a):
		return (10*a)
		
obj=A()
print(obj)			
print(obj.calcula(4))
"""






"""
while True:
	try:
		n=int(input('Digite um número: '))
	except:
		print('não deu certo')
		continue
	break	
#print(f'\033[1;33m{n}\033[1;m - \033[1;34m{n}\033[1;m')		
#print(f'\033[1;33m{n}\033[1;m')				
print ('\033[31m'+'Isto eh vermelho'+'\033[0;0m')
"""


"""
#IMPRIMIR COLORIDO NO WINDOWS
import ctypes, sys
for i in range(10):
	std_out_handle = ctypes.windll.kernel32.GetStdHandle(-11)
	ctypes.windll.kernel32.SetConsoleTextAttribute(std_out_handle, i)
		texto = "Imprimindo texto colorido no MS-DOS"		
	print(sys.stdout.write(texto),i)
"""


"""
import ctypes, sys
#RESUMIDO
std_out_handle = ctypes.windll.kernel32.GetStdHandle(-11)
ctypes.windll.kernel32.SetConsoleTextAttribute(std_out_handle, 9)
texto = "Imprimindo texto colorido no MS-DOS"		
sys.stdout.write(texto)
"""


'''
entrada = input("Digite três números") # lendo os números

#quebrando a entrada em tokens separados por espaço (poderia ser outro separador)
numerosComoString = entrada.split(" ")

#criando uma nova lista com a conversão para float de cada número
numeros = [float(numero) for numero in numerosComoString] 

print(numeros)

# atribuindo cada posição da lista a uma variável
a, b, c = numeros

triangulo = (a * c) / 2
print ("TRIANGULO:", ("%.3f" % triangulo))
'''

'''
a,b,c,d=[2,7,3,8]
print(b)
'''


"""
#USANDO A CONTRABARRA
"arquivo = open('C:\\Users\\jocel\\Desktop\\x\\arquivo.txt','w') # funciona"

"arquivo = open('C:/Users/jocel/Desktop/x/arquivo.txt','w') # funciona também"

"arquivo = open(r'C:aqui usa a contrabarra(só uma)\\Users\\jocel\\Desktop\\x\\arquivo.txt','w')"
#funciona também
"""


"""
#CENTRALIZANDO TEXTO
print('jocelio')
print('jocelio'.center(40))
"""

'''
a,w,e=input().split(' ')
a=int(a)
w=int(w)
e=float(e)
print(w)
'''




'''
#VARIÁVEIS GLOBAIS
a=10
def f1():
	print (a)
f1()
#10

def f2():
	a = a ** a
f2()
#Erro - 'a' é leitura

def f3():
	global a
	a = a ** a
f3()
f1()
#10000000000
'''


'''
#!/'usr/bin/env python3
# -*- coding: utf-8 -*-
def f():
    b = 5
    def f1():
        nonlocal b
        b = b ** b
        print("f1 b={}".format(b))
 
    def f2():
        global b
        b = b ** b
        print("f2 b={}".format(b))
 
    f1()
    f2()

b = 10
f()
#f1 b=3125
#f2 b=10000000000
'''



'''
import tst2
#não funciona
a=10
print(b)

import tst2
a=10
print(tst2.b)

from tst2 import *
a=10
print(b)

from tst2 import b
a=10
print(b)



import tst1
b=11
print(a)

from tst1 import *
b=11
print(a)

from tst1 import a
b=11
print(a)
'''


'''
dic={2:1,'b':'nnn','c':'kkk'}
dic_str=json.dumps(dic)
print(type(dic_str))
print(1)
dicionario=json.loads(dic_str)	
print(dicionario)
print(type(dicionario))
'''
'''
import json
dados = {'nome':'Renato Lelis','profissao':'Desenvolvedor de sistemas'}
dados1 = {'n':'Re Lelis','p':'Des de sistemas'}
with open('dados.json', 'a') as json_file:
	json.dump(dados, json_file)
	json.dump(dados1, json_file)
	json_file.write('\n')
'''




"""
print('t', end="")
print('e', end="")
print('s', end="")
print('t', end="")
print('e')

#teste
"""




"""
#FORMATAÇÃO DE NÚMEROS

print('texto {:.2f} texto1 {:.2f} texto2 {:.2f}'.format(0,1,2.3333))
print('texto %.2f' %0, 'texto1 %.2f' %1, 'texto2 %.2f' %2.3333)
b=format(a, '.2f')
print(b)
print('texto',format(a, '.2f'),'texto')

pi = 3.141592653589793
print('O valor de pi formatado é {:.2f}'.format(pi),1)

'''
pi = 3.141592653589793
print(f'O valor de pi formatado é {pi:.2f}',2)
'''

print(round(3.141592653589793, 2),3)

a="%.2f" %3.141592653589793
print(a,4)

def trunc(num, digits):
   sp = str(num).split('.')
   return '.'.join([sp[0], sp[:digits]])
   
n1= 1.9999999999999
t =3 # Numero de casas
d = int(n1 * 10**t)/10**t
print('Truncado', d)
print('Arredondado', round(n1,t)) 




x = 123456789
"{:,}".format(x).replace(",",".")
# returns
"123.456.789"
"""

'''
format(1123000,",d")
"1,123,000"
'''

"""
import uuid
id=str(uuid.uuid4())
print(id)
"""



'''

import json

dic={'a':1,'b':2}
with open('arquivo_teste.txt', "a") as arq:
	dic_str=json.dumps(dic)
	arq.write(dic_str+'\n')			
	print()

dic1={'c':'3','d':'4'}
with open('arquivo_teste1.txt', "a") as arq1:
	dic_str1=json.dumps(dic1)
	arq1.write(dic_str1+'\n')			
	print()

with open('arquivo_teste.txt', "r") as arqr:
	for linha in arqr:
		dic_dic=json.loads(linha)
		print(dic_dic['a']*2)

with open('arquivo_teste1.txt', "r") as arqr1:
	for linha in arqr1:
		dic_dic1=json.loads(linha)
		print(dic_dic1['c']*2)

'''				



'''
dic={'a':1,'b':2}

with open('arquivo_teste.txt', "a") as arq:
	dic_str=json.dumps(dic)
	arq.write(dic_str+'\n')			
	print()

dic1={'c':'3','d':'4'}
with open('arquivo_teste1.txt', "a") as arq1:
	dic_str1=json.dumps(dic1)
	arq1.write(dic_str1+'\n')			
	print()
'''
'''
with open('arquivo_teste.txt', "r") as arqr:
	for linha in arqr:
		dic_dic=json.loads(linha)
		print(dic_dic['a']*2)

with open('arquivo_teste1.txt', "r") as arqr1:
	for linha in arqr1:
		dic_dic1=json.loads(linha)
		print(dic_dic1['c']*2)
'''				


'''
dic={'a':1,'b':2,'c':3}
for chave in dic:
	print(chave,dic[chave])
for chave, valor in dic.items():
	print(chave, valor)

d = {'x': 1, 'y': 2, 'z': 3} 
for i, (key, value) in enumerate(d.items()):
   print(i, key, value)


'''



'''
lista1=[11,1,22,222,33]
lista2=['11','1','22','222','33']
lista3=['011','001','022','222','033']

print(lista1)
print(lista2)
print(lista3)

print()

lista1.sort()
lista2.sort()
lista3.sort()

print(lista1)
print(lista2)
print(lista3)
'''



'''
from datetime import datetime
import time

n1=int(input('Digite n1: '))
n2=int(input('Digite n2: '))

tempo1=str(datetime.now())
def	fatorial(n):
	if n == 0 or n == 1:
		return 1
	else:
		return n*fatorial(n-1)	
print(fatorial(n1)/fatorial(n2)/fatorial(n1-n2))	
time.sleep(2)
tempo2=str(datetime.now())
f='%Y-%m-%d %H:%M:%S.%f'
dif1=(datetime.strptime(tempo2,f)-datetime.strptime(tempo1,f))
print(dif1)
print()

tempo1=str(datetime.now())
res1=1
res2=1
res3=1
for i in range(1,n1+1):
	res1=res1*i
for i in range(1,n2+1):
	res2=res2*i
for i in range(1,(n1-n2)+1):
	res3=res3*i
print(res1,res2,res3)	
print((res1)/(res2)/(res3))		
time.sleep(2)
tempo2=str(datetime.now())
f='%Y-%m-%d %H:%M:%S.%f'
dif1=(datetime.strptime(tempo2,f)-datetime.strptime(tempo1,f))
print(dif1)
print()

tempo1=str(datetime.now())
res1=1
cont1=1
res2=1
cont2=1
res3=1
cont3=1
while cont1<=n1:
	res1=res1*cont1
	cont1+=1
while cont2<=n2:
	res2=res2*cont2
	cont2+=1
while cont3<=(n1-n2):
	res3=res3*cont3
	cont3+=1
print((res1)/(res2)/(res3))		
time.sleep(2)
tempo2=str(datetime.now())
f='%Y-%m-%d %H:%M:%S.%f'
dif1=(datetime.strptime(tempo2,f)-datetime.strptime(tempo1,f))
print(dif1)
'''




'''
print()
lista_de_clientes=[10,20,30,40]
print('Lista de clientes: ',lista_de_clientes)
cont=0
while True:
	if cont==5:
		print('Seu acesso foi finalizado devido muitas tentativas')
		break
	senha=input("Digite sua senha: ")
	if senha == '0123':
		n=int(input("Qual valor você quer retirar? "))
		lista_de_clientes.remove(n)
		print()
		print('A lista de clientes agora é:',lista_de_clientes)
		break
	else:
		print('Sua senha não permite excluir valores!')	
		print('Tente novamente...')
		print()
	cont+=1	
'''




'''

lista = [20, 10, 50, 30]
lista_ordenada=[]

for j in  range(len(lista)):
	#for i in lista:
	a=min(lista)
	lista_ordenada.append(a)
	lista.remove(a)
	print(a)
	print(j)
	print(lista)
	#break
	
		
print(lista_ordenada)
'''


'''
#ARVORE DE NATAL

import time
sl=1
time.sleep(sl)

print()
slp=0.1
n=16
for i in range(1,n,2):
	print (8*" ",int((n-i)/2)*" ",i*"*")
	time.sleep(slp)

n=24
for i in range(3,n,2):
	print (4*" ",int((n-i)/2)*" ",i*"*")
	time.sleep(slp)
	
n=32
for i in range(5,n,2):
	print ((int((n-i)/2)+1)*" ",i*"*")
	time.sleep(slp)
	
n=30
n1=3
print (int((n)/2)*" ",n1*"*")
time.sleep(slp)
print (int((n)/2)*" ",n1*"*")
time.sleep(slp)
print (int((n)/2)*" ",n1*"*")

'''



'''

number_1 = int(input('Enter your first number: '))
number_2 = int(input('Enter your second number: '))

print('{} + {} = '.format(number_1, number_2))
print(number_1 + number_2)


print(number_1,'+',number_2,"=")
print(number_1 + number_2)
'''





'''
dic={'Calçados':10,'Camisas':20,'Botas':30,'Sapatos':40,'Camisetas':50,
'Brinquedos':60,'Luvas':70,'Ferramentas':80,'Campainha':90}



while True:
	procura_codigo=input('Digite o início do produto: ')
	for key in dic:
		if key[0:len(procura_codigo)] == procura_codigo:
			print(key,':',dic[key])
	print()		
	resposta=input('Achou? (S/N) ->')
	print()
	if resposta == 'S' or resposta == 's':
		break
codigo=input('Digite o código do produto: ')
print()
'''



'''
PARA APAGAR ARQUIVO TXT
with open('arquivo_t.txt', "w") as arq:
	#dic_str=json.dumps(dic3)
	arq.write('') #(dic_str+'\n')			
'''
	
'''
with open('arquivo_t.txt','w'): pass
'''

'''
open('arquivo_t.txt', 'w').close()
'''




'''
REESCREVER ARQUIVO
import json

dic1={'a':'1','cod':'2','c':'3'}
dic2={'d':'4','cod':'5','f':'6'}
dic3={'g':'7','cod':'8','i':'9'}

'''

'''
with open('arquivo_t.txt', "a") as arq:
	dic_str=json.dumps(dic3)
	arq.write(dic_str+'\n')			
'''


'''
lista=[]
with open('arquivo_t.txt', "r") as arqr:
	for linha in arqr:
		dic_dic=json.loads(linha)
		lista.append(dic_dic)
print(lista)	
	
for item in lista:
	if item['cod'] == '5':
		item['cod'] = '1000'

print(lista)

with open('arquivo_t.txt','w'): pass

with open('arquivo_t.txt', "a") as arq:
	for item in lista:
		dic_str=json.dumps(item)
		arq.write(dic_str+'\n')			
'''




'''
ganhos_julho = 99.91 * 5
print(ganhos_julho)

gastos_julho = 110.1 * 3
print(gastos_julho)
#Olha os resultados que obtive:
#499.54999999999995
#330.29999999999995


from decimal import Decimal

ganhos_julho = Decimal('99.91') * 5
print(ganhos_julho)

gastos_julho = Decimal('110.1') * 3
print(gastos_julho)
#Dessa vez, olha o resultado:
#499.55
#330.3
'''


'''
import os

for i in range(15):
	print(i*" "+'X')
	print(i*" "+str(i))
	clear=lambda: os.system('clear')
	clear()
'''


'''
print(0b101111)
47
print(int("101111",2))
47


print(0xff)
255
print(int("ff",16))
255


print(int("b",16))
11


print(bin(47))
0b101111

print(bin(3))
0b11

print(True + True)
2
print(True + False)
1
print(False + False)
0

a=4+3j
print(type(a))

print((2-3j)/(-2+2j))
(-1.25+0.25j)

a=1,2,3,4
print(a)
print(type(a))
tuple


print((1, 2) + (3, 4))  # Expansão de tuplas
(1, 2, 3, 4)
print((1, 2) * 3)  # Repetição
(1, 2, 1, 2, 1, 2)


x = 0
while x < 10:
    print(x)
    x += 1
else:
    print("fim while")
'''



'''
import os

n=input('Digite 4 número de 1 a 10 separados por espaço: ')
lista=n.split()
lista_int=[]
for i in lista:
	i=int(i)
	lista_int.append(i)

clear=lambda: os.system('clear')
clear()
		
print()
while True:
	n1=input('Usuário digita um numero de 1 a 10: ')
	n1=int(n1)
	if n1 not in [1,2,3,4,5,6,7,8,9,10]:
		print('Número invalido... Digite novamente')
		continue
	break
print()
print('Os números do programador foram:',lista_int)
if n1 in lista_int:
	print('O usuário acertou !')
else:
	print('O usuário errou !')	
'''	


'''
ARREDONDAMENTO E MOEDA E REPLACE
n=round(12.4593681,2)
n1=round(12.4553681,2)
n2=round(12.4543681,2)
print(n,n1,n2)
#12.46 12.46 12.45
a=str(n).replace(".",",")
print(a)
#12,46



import locale 

locale.setlocale(locale.LC_MONETARY, 'en_US.UTF-8')

a=locale.currency(15000, grouping=True)
print(a)
#$15,000.00
'''



'''
import time

a=3
lista=[2]
status='s'
while True:
	for i in lista:
		if a%i==0:
			status='n'
			break
	if status =='n':
		a += 1
	else:
		lista.append(a)
		print(a)	
	if a == 100000:
		break
	status='s'

'''

'''
lista = [111,333,555,444]
print(lista.index(555))
'''


'''
import getpass
#ESCONDER/OCULTAR ENTRADA DE DADOS DO USUÁRIO
nome = input('Entre com o seu nome: ')
#senha = input('Digite a sua senha: ')
senha = getpass.getpass('Digite a sua senha: ')

print(senha)
'''




'''
CORES NO LINUX
print('\033[1;33;44mOlá Mundo!')
'''
'''
#estilo(negrito,..)/texto/cor de fundo = background
0 sem estilo 
1 negrito
4 sublinhar
7 inverte configuração letra e fundo

30 branco
31 vermelho
32 verde
33 amarelo
34 azul
35 magenta
36 ciano
37 cinza

40 branco
41 vermelho
42 verde
43 amarelo
44 azul
45 magenta
46 ciano
47 cinza
'''


'''
#CORES NO WINDOWS
import colorama
from colorama import Fore
from colorama import Style

colorama.init()
print(Fore.BLUE + Style.BRIGHT + "This is the color of the sky" + Style.RESET_ALL)
print(Fore.GREEN + "This is the color of grass" + Style.RESET_ALL)
print(Fore.BLUE + Style.DIM + "This is a dimmer version of the sky" + Style.RESET_ALL)
print(Fore.YELLOW + "This is the color of the sun" + Style.RESET_ALL)
'''




'''
nome = 'alan'
print(id(nome))
novo_nome = 'h'+nome
print(novo_nome)
print(id(novo_nome))

print()

nome = 'alan'
print(id(nome))
nome = 'h'+nome
print(nome)
print(id(nome))
'''



'''
import time, sys
from datetime import datetime

numero = int(input("Digite o numero: "))

tempo1=str(datetime.now())
lista = []
for i in range (1,numero+1):
	if numero%i == 0:
		lista.append(i)
print(lista)		
tempo2=str(datetime.now())
f='%Y-%m-%d %H:%M:%S.%f'
dif1=(datetime.strptime(tempo2,f)-datetime.strptime(tempo1,f))

tempo3=str(datetime.now())
lista = []
for i in range (1,int(numero/2)+1):
	if numero%i == 0:
		lista.append(i)
lista.append(numero)		
print(lista)		
tempo4=str(datetime.now())
f='%Y-%m-%d %H:%M:%S.%f'
dif2=(datetime.strptime(tempo4,f)-datetime.strptime(tempo3,f))

print(dif1)
print(dif2)
'''


'''
import time, sys
from datetime import datetime

numero = int(input("Digite o numero: "))
print()

tempo1=str(datetime.now())
lista1 = []
for i in range (1,numero+1):
	if numero%i == 0:
		lista1.append(i)
tempo2=str(datetime.now())

tempo3=str(datetime.now())
lista2 = []
for i in range (1,int(numero/2)+1):
	if numero%i == 0:
		lista2.append(i)
lista2.append(numero)		
tempo4=str(datetime.now())

f='%Y-%m-%d %H:%M:%S.%f'
dif1=(datetime.strptime(tempo2,f)-datetime.strptime(tempo1,f))

f='%Y-%m-%d %H:%M:%S.%f'
dif2=(datetime.strptime(tempo4,f)-datetime.strptime(tempo3,f))
print(lista1)		
print(lista2)		
print()
print(dif1)
print(dif2)
'''




'''
a=10

if a == 10:
	print("dez")
else:
	print("nao")	


print("dez" if a == 10 else "nao") 
'''

 


'''
#ITERAR DICIONÁRIO	
parametros = {4:6,8:2,5:4,2:9}
for valores,k in parametros.items():
	print(area_retangulo(valores,k))
	#print(area_retangulo(valores,parametros[valores]))
'''



"""

#CRIAR EXECUTÁVEL
import pandas as pd
import win32com.client as win32
#pip install pandas   e   pywin32   e   openpyxl
#    e    pyinstaller  - se não tiver    


#comando para executável -> pyinstaller --onefile -w (esse w só se o programa abrir janelas)
#aparece pasta build=deleta   arquivo  .spec=deleta
 
#a
#b
#c
"""





'''
#INPUT COMPOSTO
i=10
n= input(f'Digite o {i}° numero: ')

i=10
n= input('Digite o '+str(i)+'° numero: ')
'''



"""
Sobre o Método format()
Primeiramente, o método format() em python serve basicamente para criar uma string que contém campos entre chaves que são substituidos pelos argumentos de format.

Logo abaixo, vou deixar um exemplo executado no ambiente interativo do terminal python:

>>> str = 'O blog {0} merece {1} estrelas'
>>> str.format('Programador Viking', 5)
'O blog Programador Viking merece 5 estrelas'
>>>
Portanto, repare que os campos de substituição na string que estão entre chaves ‘{}’ estão associadas aos parâmetros do método format().

Vale ressaltar que a numeração dos parâmetros na string inicia pelo numero zero para o primeiro parâmetro, 1 para o segundo parâmetro e assim por diante.

Mas nada impede de usar um parâmetro mais de uma vez e em fora de ordem como no exemplo abaixo:

>>> str = '{0} é um {1} companheiro, {1} companheiro é o {0}, ninguém pode negar'
>>> str.format('David', 'bom')
'Paulo é um bom companheiro, bom companheiro é o Paulo, ninguém pode negar'
>>> str.format('José', 'ótimo')
'João é um ótimo companheiro, ótimo companheiro é o João, ninguém pode negar'
>>>
Ou seja, também é possível usar campos nomeados, porém esses campos devem vir depois dos parâmetros simples no método format.

Para exemplificar, criei o programa idade.py conforme o código abaixo:

exto = '{0} tem {idade} anos de idade'
print('Progama para calcular a idade de uma pessoa',end='\n\n')

nome = input('Entre com o nome da pessoa: \n')

a1 = int(input('Entre com o ano de nascimento: \n'))

a2 = int(input('Entre com ano atual: \n'))

print(texto.format(nome, idade = a2 - a1 ))
Logo depois, dentro dos campos a serem substituídos podemo especificar formatações numéricas ou para strings usando as seguintes regras:

Leia também: Os 7 Melhores Livros Para Aprender Python Sozinho

Usando format com strings:
Primeiramente, vamos conhecer a estrutura base:

:[preencher][alinhar][largura].[precisão]

Logo depois com o seguinte esquema:

preencher	alinhar	largura	precisão
Qualquer caractere	< esquerda> direita^ centro	largura miníma do campo	largura máxima do campo
Ou seja, executando o programa test_format.py, onde o código pode ser encontrado logo abaixo.

Logo depois, podemos ver várias formas de saída usando format() com largura e precisão:

# Programa para testar a função format()

s = 'Eu Adoro Python'

# alinha a direita com espaços em branco
print("{0:>20}".format(s))

# alinha a direita com símbolos #
print("{0:#>20}".format(s))

# alinha ao centro usando espaços em branco a esquerda e a direita
print("{0:^20}".format(s))

# imprime só as primeiras oito letras
print("{0:.8}".format(s))
telegram programador viking - Descubra Como Utilizar o Método format() em Python
Usando format com números:
Primeiramente, antes de iniciarmos a explicação de como formatar números, vamos ver como podemos fazer essa formatação sem o uso do método format().

Atenção:
Portanto, esse tipo de formatação era usado até a versão 2 do python e estou explicando apenas para fins didáticos. Portanto, prefira sempre utilizar o método format().

Ou seja, a estrutura base é:

%[flag][tamanho].[precisão][conversor]

Logo depois vamos conhecer as flags, que são:

Flag	Significado
#	Prefixa os inteiros com 0, 0o, 0O, 0x, 0X.
o ou O para octais e x ou X hexadecimais
+	Força a saída com sinal.
Logo depois vamos conhecer os conversores, que são:

Conversor	Significado
d	Inteiro.
i	Inteiro.
f	Float.
F	Float.
o	Inteiros em octal.
x	Inteiros em hexadecimal minuscula
X	Inteiros em hexadecimal maiúsculas
e	Float em formato exponencial minusculo
E	Float em formato exponencial maiúsculo
g	Mesmo que “e” se expoente é maior do que -4 ou inferior a precisão, “f” de outra forma.
G	Mesmo que “E” se expoente é maior do que -4 ou inferior a precisão, “F” de outra forma.
c	Um único caractere.
s	String (converte qualquer objeto python usando str ()).
Logo depois, mais alguns exemplos para executar no ambiente iterativo:

>>> print('%+d' % 123)
+123
>>> print('%+4.2f' % 12.3678)
+12.37
>>> print('%x' % 123)
7b
>>> print('%#x' % 123)
0x7b
Agora vamos ver como format() trabalha com os números, a sua estrutura base é:

:[preencher][alinhar][sinal][largura].[precisão][tipo]

Primeiramente vamos entender o seguinte esquema:

preencher	alinhar	largura	precisão
Qualquer caractere	< esquerda> direita^ centro	largura miníma do campo	largura máxima do campo
Logo depois, vou deixar alguns exemplos para testar no ambiente iterativo:

>>> "{0:4}".format(-123)
'-123'
>>> "{0:4}".format(123)
' 123'
>>> "{0:4.2f}".format(33.3287)
'33.33'
>>> "{0:+4.2f}".format(33.3287)
'+33.33'
>>> "{0:+4.2e}".format(33.3287)
'+3.33e+01'
>>> "{0:b}".format(123)
'1111011'

Por fim, vamos alterar o programa media.py para termos uma saída dos dados melhorada:

# Programa para calcular a media de um aluno
print('Programa para calcular a media de um aluno', end='\n\n')

nome = input('Entre com o nome do aluno: \n')

nota1 = float(input("Entre com a primeira nota: \n"))

nota2 = float(input("Entre com a segunda nota: \n"))

media = (nota1 + nota2) / 2
print('{0} teve media igual a: {1:4.2f}'.format(nome, media))
Se executarmos novamente o programa com as mesmas entradas, podemos perceber que a saída fica de acordo com o esperado.

Conclusão
Em conclusão, neste artigo vimos como funciona o método format() em Python, um ótimo recurso para utilizarmos em nossos programas.

Ou seja, se você quer formatar um conteúdo essa é uma excelente opção.

Você quer se tornar tornar um Programador Python e faturar alto utilizando essa excelente linguagem de programação?

Portanto, se a resposta for sim, recomendo dar uma olhada neste link aqui:

>> CURSO COMPLETO DE PYTHON <<

Enfim, muito obrigado por acompanhar o blog e lhe desejo muito sucesso em sua jornada!

 Post Views: 7.027
"""





'''
#A função Map pega uma lista e a transforma numa nova lista,
# executando algum tipo de operação em cada elemento.
#  No exemplo abaixo, a função passa por cada elemento e mapeia
#   o resultado de si mesma para uma nova lista.
#    Note que a função List simplesmente converte a saída para o tipo de lista.

numeros = [1, 2, 3, 4, 5]
output = list(map(lambda var: var**2, numeros))
print(output)
#>>> [1, 4, 9, 16, 25]

#A função Filter pega uma lista e aplica uma regra, onde compara
# cada elemento da lista contra a regra de filtragem booleana.
# Uma vez aplicada a condição, retorna um subconjunto da lista original.
numeros = [1, 2, 3, 4, 5]
output = list(filter(lambda x: x >= 3, numeros))
print(output)
#>>> [3, 4, 5]


#A função reduce , disponível no módulo built-in functools ,
# serve pra "reduzir" um iterável (como uma lista) a um único valor.
# É um paradigma um pouco mais comum em linguagens funcionais,
# mas que também é bastante útil em linguagens
# imperativas/orientadas a objetos como o Python.
from functools import reduce
lista = [4,1,5,2,8,7]
maior = reduce((lambda x,y: x if (x>y) else y),lista)
print(maior)
'''













