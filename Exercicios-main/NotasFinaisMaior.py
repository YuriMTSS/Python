""" O usuário vai digitar uma sequência de notas finais dos alunos. O sistema deve responder qual é a maior nota. """

primeira_nota = float(input("Digite a Nota: "))
maior = primeira_nota

for _ in range(5):
    numero = int(input("Digite a nota: "))
    if numero > maior:
        maior = numero
    
print("Maior: ", maior)



