import random; # importar as funcoes do random
random.seed(); # inicializar o contador
sorteados = []; # lista de numeros sorteados
digitados = []; # lista de numeros digitados
# realização dos sorteios
for i in range(1,7):
    sorteio = random.randint(1,60); #sortear um numero
    sorteados.append(sorteio); #adicionar na lista

# digitação dos números
for i in range(1,7):
    numero = input ("informe a %dª dezena: "%i);
    digitados.append(numero);

#1- verificação dos acertos: exatamente na sequencia
print ("---- 1 verificação ---------")
acertos = [];
for i in range(0,6):
    if digitados[i] == sorteados[i]:
        acertos.append(digitados[i]);
if len(acertos) == 6: ## sorteados.len
    print ("parabéns.... você é um milionário")
else:
    sorteados.sort()
    acertos.sort()
    print ("vc foi roubado. Os numeros sorteados foram:")
    print (sorteados)
    print ("os numeros acertados foram: ")
    print (acertos)