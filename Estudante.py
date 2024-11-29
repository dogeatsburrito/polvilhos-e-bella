from Pessoa import Pessoa
class Estudante(Pessoa):
    def __init__(self, nome, endereco, responsavel, emailresponsavel, registro, segmento, Turma, curso, usuario, email, senha):
        super().__init__(nome, endereco, usuario, email, senha)
        cursos_em = ["mecatrônica", "eletromecânica", "informática"]
        cursos_formatados = "mecatrônica, eletromecânica, informática"
        cursos_es = ["bacharel em ciências da computação", "bacharel em pedagogia"]
        cursos_es_formatados = "mecatrônica, eletromecânica, informática"
        if segmento =="Ensino Superior":
            if not curso or curso.lower() not in cursos_es:
                raise ValueError(
                    f"Estudantes do Ensino Superior devem estar em um dos cursos: {cursos_es_formatados}. "
                    f"O curso fornecido foi: '{curso}'."     
                )
        elif segmento == "Ensino Médio":
            if not curso or curso.lower() not in cursos_em:
                raise ValueError(
                    f"Estudantes do Ensino Médio devem estar em um dos cursos: {cursos_formatados}. "
                    f"O curso fornecido foi: '{curso}'."
                )
        return curso.lower() if curso else None
        self.ativa= True
        self.responsavel = responsavel
        self.emailresponsavel = emailresponsavel
        self._registroacademico = registro
        self.segmento = segmento
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

    def desativar(self):
        if not self.ativa:
            print(f"O estudante {self.nome} já está desativo")
        else:
            self.ativa = False  # Marca o estudante como desativada
            print(f"Estudante {self.nome} foi desativado.")

    def ativar(self):
        if self.ativa:
            print(f"O estudante {self.nome} já está ativo.")
        else:
            self.ativa = True  # Marca estudante como ativa novamente
            print(f"Estudante {self.nome} foi reativado.")
