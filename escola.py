class Pessoa:
    def __init__(self, nome, cpf, endereco, usuario, email, senha, ocupacao):
        self.nome= nome
        self._cpf= cpf
        self._endereco= endereco
        self.usuario= usuario
        self.email= email
        self._senha= senha
        self.ocupacao= ocupacao

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, valor):
        if not valor.isnum() or len(valor)>11:
            self._cpf = valor
        else:
            raise ValueError("Digite o cpf corretamente!")
        
    @property
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self, valor):
        self._endereco= valor

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, valor):
        self._senha = valor

class Estudante(Pessoa):
    def __init__(self, nome, endereco, responsavel, emailresponsavel, registro, Segmento, Turma, curso, usuario, email, senha):
        if segmento.nome == "Ensino Médio" and curso not in segmento.cursos_validos:
            raise ValueError(f"Curso '{curso}' não é válido para o segmento Ensino Médio. Os cursos válidos são: {', '.join(segmento.cursos_validos)}")
        super().__init__(nome, endereco, usuario, email, senha)
        self.responsavel = responsavel
        self.emailresponsavel = emailresponsavel
        self._registroacademico = registro
        self.segmento = Segmento
        self.turma = Turma
        self.curso = curso

    @property
    def registroacademico(self):
        return self._registroacademico

    @registroacademico.setter
    def registroacademico(self, valor):
        self._registroacademico = valor

    def transferirCurso(self, nova_turma, novo_curso):
        if isinstance(self.curso, list):
            print("Alunos inseridos em 2 cursos não podem efetuar a transferência")
        elif hasattr(nova_turma, 'curso') and nova_turma.curso == novo_curso:
            self.turma = nova_turma
            self.curso = novo_curso
            print(f"{self.nome} foi transferido para o curso {novo_curso} na turma {nova_turma.nome}.")
        else:
            print(f"Erro: O curso de '{novo_curso}' não está disponível na turma '{nova_turma.nome}'.")

    def __str__(self):

        cursos_str = ' e '.join(self.curso)
        turmas_str = ', '.join([turma.nome for turma in self.turmas])

        return(f"O estudante {self.nome} faz parte da(s) turma(s) {turmas_str} e curso(s) {cursos_str} do {self.segmento.nome}\nInformações
                adicionais:\nUsuário:{self.usuario}\nEmail:{self.email}\nResponsável: {self.responsavel}\nEmail do Responsável: {self.emailresponsavel}")

class Professor(Pessoa):
    def __init__(self, nome, endereco, formacao, Disciplinas, Segmentos, Turmas, usuario, email, senha):
        super().__init__(nome, endereco, usuario, email, senha)
        self.formacao= formacao
        self.disciplinas= Disciplinas
        self.segmento = Segmentos
        self.turma = Turmas

    def __str__(self):
    
        disciplinas_str = ', '.join([disciplina.descricao for disciplina in self.disciplinas]) if isinstance(self.disciplinas, list) else self.disciplinas.descricao
        turmas_str = ', '.join([turma.nome for turma in self.turmas]) if isinstance(self.turmas, list) else self.turmas.nome
        segmentos_str = ', '.join([segmento.nome for segmento in self.segmentos]) if isinstance(self.segmentos, list) else self.segmentos.nome

        return (f"O professor {self.nome} da(s) disciplina(s) {disciplinas_str} "
                f"realiza sua aula na(s) turma(s) {turmas_str} "
                f"no(s) segmento(s) {segmentos_str}.\nInformações adicionais:\nUsuário: {self.usuario}\nEmail: {self.email}\n")

class Disciplina:
    def __init__(self, id, descricao, Segmento, Professores):
        self.id= id
        self.descricao= descricao
        self.segmento= Segmento
        self.professores= Professores

class Turma:
    def __init__(self, nome, Segmento, Curso, anoescolar, Alunos, Professores, Disciplinas):
        if Segmento == "Ensino Médio" and len(Alunos) < 20:
            raise ValueError("A turma de Ensino Médio deve ter no mínimo 20 alunos!")
        elif Segmento == "Ensino Superior" and len(Alunos) < 5:
            raise ValueError("A turma de Ensino Superior deve ter no mínimo 5 alunos!")

        self.nome = nome
        self.segmento = Segmento
        self.curso = Curso
        self.ano = anoescolar
        self.alunos = Alunos
        self.professores = Professores
        self.disciplinas = Disciplinas

    def __str__(self):
       alunos_str = ', '.join([aluno.nome for aluno in self.alunos]) if isinstance(self.alunos, list) else self.alunos.nome
       professores_str = ', '.join([professor.nome for professor in self.professores]) if isinstance(self.professores, list) else self.professores.nome
       disciplinas_str = ', '.join([disciplina.descricao for disciplina in self.disciplinas]) if isinstance(self.disciplinas, list) else self.disciplinas.descricao

       return (f"A turma {self.nome}")

class SegmentoEnsino:
    def __init__(self, nome, Cursos, Disciplinas, Turmas):
        self.nome= nome
        self.cursos_validos = cursos_validos
        self.cursos= Cursos
        self.disciplinas= Disciplinas
        self.turmas= Turmas
        
    def adicionarcurso (self,cursos):
        if curso not in self.cursos_validos:
            raise ValueError(f"O curso '{curso}' não é uma opção válida para o segmento {self.nome}.")
            
        if curso in self.cursos:
            raise ValueError(f"O curso '{curso}' já está registrado no segmento {self.nome}.")
            
        self.cursos.append(curso)
        print(f"O curso '{curso}' foi adicionado ao segmento {self.nome}.")

    def listarcursos(self):
        return self.cursos
    
