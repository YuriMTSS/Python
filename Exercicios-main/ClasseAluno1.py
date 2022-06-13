class Aluno:
    def __init__(self, nome, RA, curso, nota):
        self.nome = nome
        self.RA = RA
        self.curso = curso
        self.nota = nota
    
    def aprovado(self):
        return self.nota >= 5.0
    def __str__(self):
        return ("Nome: "+ str(self.nome) +
                "\nRA: "+ str(self.RA) +
                "\nCurso: "+ str(self.curso) +
                "\nNota: "+ str(self.nota))

""" def imprimir(self):
        print("Nome: ", self.nome,
              "\nRA: ", self.RA,
              "\nCurso: ", self.curso,
              "\nNota: ", self.nota)
"""


aluno1 = Aluno('Ana', 123456, 'Veterinaria', 10.0)
#aluno1.imprimir()
print(aluno1)
if aluno1.aprovado():
    print(aluno1.nome ,'está aprovado')
else:
    print(aluno1.nome, 'está reprovado')
