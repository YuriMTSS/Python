""" class Aluno:
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
                "\nNota: "+ str(self.nota) + 
                "\n")

class Turma:
    def __init__(self, alunos = []):
        self.alunos = alunos

    def adiciona_aluno(self, aluno):
        self.alunos.append(aluno)
    
    #def adiciona_alunos(self, alunos):
     #   for aluno in alunos:
      #      self.adiciona_aluno(alunos)


    def imprime_aluno(self):
        for aluno in self.alunos:
            print(aluno)
    
    def imprime_aprovados(self):
        for aluno in self.alunos:
            if aluno.aprovado():
                print(aluno)
    
    def imprime_reprovados(self):
        for aluno in self.alunos:
            if not aluno.aprovado():
                print(aluno)
    
    
turma = Turma()
ana = Aluno('Ana', 123456, 'Veterinaria', 10.0)
yuri = Aluno('Yuri', 654321, 'Análise e Desenvolvimento de Sistemas', 10.0)
ezequiel = Aluno('Ezequiel', 784398, 'Análise e Desenvolvimento de Sistemas', 1.0)
rebeca = Aluno('Rebeca', 765123, 'Veterinária', 0.0)

#turma.adiciona_alunos([ana, yuri, ezequiel, rebeca])
turma.adiciona_aluno(ana)
turma.adiciona_aluno(yuri)
turma.adiciona_aluno(ezequiel)
turma.adiciona_aluno(rebeca)


print('====== Todos os alunos ======')
turma.imprime_aluno()
print()
print('====== Aprovados ======')
turma.imprime_aprovados()
print('====== Reprovados ====')
turma.imprime_reprovados() """

# Usando Encapsulamento ======================================================================
""" class Aluno:
    def __init__(self, nome, RA, curso, p1, p2, p3):
        self._nome = nome
        self._RA = RA
        self._curso = curso
        self._p1 = p1
        self._p2 = p2
        self._p3 = p3

    @property
    def nota(self):
        return (self._p1 + self._p2 + self._p3) / 3.0

    def aprovado(self):
        return self.nota >= 5.0

    def __str__(self):
       return ("Nome: "+ str(self._nome) +
               "\nRA: "+ str(self._RA) +
               "\nCurso: "+ str(self._curso) +
               "\nNota: "+ str(self.nota) + 
               "\n")
    

class Turma:
    def __init__(self, alunos = []):
        self._alunos = alunos

    def adiciona_aluno(self, aluno):
        self._alunos.append(aluno)
    
    #def adiciona_alunos(self, alunos):
     #   for aluno in alunos:
      #      self.adiciona_aluno(alunos)


    def imprime_aluno(self):
        for aluno in self._alunos:
            print(aluno)
    
    def imprime_aprovados(self):
        for aluno in self._alunos:
            if aluno.aprovado():
                print(aluno)
    
    def imprime_reprovados(self):
        for aluno in self._alunos:
            if not aluno.aprovado():
                print(aluno)
    
    
turma = Turma()
ana = Aluno('Ana', 123456, 'Veterinaria', 10.0, 9.8, 9.9)
yuri = Aluno('Yuri', 654321, 'Análise e Desenvolvimento de Sistemas',10.0,10.0,9.9)
ezequiel = Aluno('Ezequiel', 784398, 'Análise e Desenvolvimento de Sistemas',0.0,0.4,2.0)
rebeca = Aluno('Rebeca', 765123, 'Veterinária',0.0,0.0,0.0)

#turma.adiciona_alunos([ana, yuri, ezequiel, rebeca])
turma.adiciona_aluno(ana)
turma.adiciona_aluno(yuri)
turma.adiciona_aluno(ezequiel)
turma.adiciona_aluno(rebeca)


print('====== Todos os alunos ======')
turma.imprime_aluno()
print()
print('====== Aprovados ======')
turma.imprime_aprovados()
print('====== Reprovados ====')
turma.imprime_reprovados()
 """

# Herança ====================================================================================================
from pygame import init


class Retangulo:
    def __init__(self, largura, altura):
        self._altura = altura
        self._largura = largura
    
    def area(self):
        return self._altura * self._largura
    
    def perimetro(self):
        return 2 * self._largura + 2 * self._altura
    
    def __str__(self):
        return ("Retângulo: " + str(self._largura) +
        "x" + str(self._altura))

class Quadrado(Retangulo): # Quadrado herda retangulo
    def __init__(self, lado):
        # super representa o objeto mae
        super().__init__(lado, lado)

    @property
    def lado(self):
        return self._largura # Lemos o atributo da classe mae
    
    @lado.setter
    def lado(self, lado):
        self._largura = lado # alteramos o atributo da classe mae
        self._altura = lado
    
    def __str__(self):
        return "Quadrado de lado " + str(self.lado)

q = Quadrado(4)
print(q)
print(q.area(), q.perimetro())


""" 
r = Retangulo(10,5)
print(r)
 """