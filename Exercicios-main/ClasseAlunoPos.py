class Aluno:
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
    
    @property
    def nota(self):
        return (self._p1 + self._p2 + self._p3) / 3.0

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

class AlunoPos(Aluno):
    def __init__(self, nome, RA, curso, p1, p2, p3):
        super().__init__(nome, RA, curso, p1, p2, p3)
    
    @property
    def conceito(self):
        if self.nota >= 8.5:
            return "A"
        elif self.nota >= 7:
            return "B"
        elif self.nota >= 5:
            return "C"
        else:
            return "D"

    def __str__(self):
       return ("Nome: "+ str(self._nome) +
               "\nRA: "+ str(self._RA) +
               "\nCurso: "+ str(self._curso) +
               "\nConceito: "+ str(self.conceito) + 
               "\n")
    
ana  = AlunoPos('Ana', 123456, 'Veterinaria', 10,9,8)
print(ana)
