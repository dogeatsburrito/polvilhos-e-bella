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
        if not valor.isnum() or len(valor)==11:
            self._cpf = valor
        else:
            raise ValueError("Você não digitou o cpf corretamente!")
        
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

class Professor(Pessoa):
    def __init__(self, nome, endereco, formacao, Disciplinas, segmentos, Turmas, usuario, email, senha):
        super().__init__(nome, endereco, usuario, email, senha)
        self.formacao= formacao
        self.disciplinas= Disciplinas
        self.segmento = segmentos
        self.turma = Turmas

class Disciplina:
    def __init__(self, id, descricao, segmento, Professores):
        self.id= id
        self.descricao= descricao
        self.segmento= segmento
        self.professores= Professores

class Turma:
    def __init__(self, nome, segmento, Curso, anoescolar, Alunos, Professores, Disciplinas):
        if segmento == "Ensino Médio" and len(Alunos) < 20:
            raise ValueError("A turma de Ensino Médio deve ter no mínimo 20 alunos!")
        elif segmento == "Ensino Superior" and len(Alunos) < 5:
            raise ValueError("A turma de Ensino Superior deve ter no mínimo 5 alunos!")

        self.ativa= True
        self.nome = nome
        self.segmento = segmento
        self.curso = Curso
        self.ano = anoescolar
        self.alunos = Alunos
        self.professores = Professores
        self.disciplinas = Disciplinas
        
    def __str__(self):
       if not self.ativa:
           print("Você não pode acessar uma turma desativada")
       alunos_str = ', '.join([aluno.nome for aluno in self.alunos]) if isinstance(self.alunos, list) else self.alunos.nome
       professores_str = ', '.join([professor.nome for professor in self.professores]) if isinstance(self.professores, list) else self.professores.nome
       disciplinas_str = ', '.join([disciplina.descricao for disciplina in self.disciplinas]) if isinstance(self.disciplinas, list) else self.disciplinas.descricao

       return (f"A turma {self.nome} do curso {self.curso} do {self.segmento} foi iniciada em {self.ano}.\nALUNOS PARTICIPANTES:\n{alunos_str}\nPROFESSORES PARTICIPANTES:\n{professores_str}\nGRADE CURRÍCULAR:\n{disciplinas_str}\n")

    def editarTurma(self):
        while True:
            print("\nO que você deseja editar?")
            print("1. Nome da turma")
            print("2. Alunos")
            print("3. Professores")
            print("4. Disciplinas")
            print("5. Encerrar edição")
            escolha = input("Digite o número da opção desejada: ").strip()

            if escolha == "1":  # Editar nome
                novo_nome = input("Qual será o novo nome da turma? ").strip()
                if novo_nome.lower() == "cancelar":
                    print("Operação cancelada.")
                    continue
                self.nome = novo_nome
                print(f"O nome da turma foi alterado para '{self.nome}'.")

            elif escolha == "2":  # Editar alunos
                print("Deseja adicionar ou excluir alunos?")
                print("1. Adicionar")
                print("2. Excluir")
                acao = input("Digite o número da ação desejada: ").strip()

                if acao == "1":  # Adicionar aluno
                    while True:
                        aluno = input("Insira o objeto do aluno a ser adicionado (ou digite 'cancelar' para encerrar): ").strip()
                        if aluno.lower() == "cancelar":
                            print("Operação cancelada.")
                            break
                        try:
                            # Aqui você valida o objeto do aluno (exemplo: verificar se é uma instância de Estudante)
                            if isinstance(aluno, Estudante):
                                print(f"Você deseja adicionar {aluno.nome} à turma {self.nome}? (Digite 'sim' para confirmar ou 'cancelar' para encerrar)")
                                confirmacao = input().strip().lower()
                                if confirmacao == "sim":
                                    self.alunos.append(aluno)
                                    print(f"Aluno {aluno.nome} adicionado à turma {self.nome}.")
                                    break
                                elif confirmacao == "cancelar":
                                    print("Operação cancelada.")
                                    break
                            else:
                                print("O objeto fornecido não é um aluno válido. Tente novamente.")
                        except Exception as e:
                            print(f"Erro ao adicionar aluno: {e}")
                
                elif acao == "2":  # Excluir aluno
                    while True:
                        print("Lista de alunos:")
                        for i, aluno in enumerate(self.alunos, 1):
                            print(f"{i}. {aluno.nome}")
                        escolha_aluno = input("Digite o número do aluno que deseja excluir (ou 'cancelar' para encerrar): ").strip()
                        if escolha_aluno.lower() == "cancelar":
                            print("Operação cancelada.")
                            break
                        try:
                            indice = int(escolha_aluno) - 1
                            if 0 <= indice < len(self.alunos):
                                aluno_excluir = self.alunos[indice]
                                print(f"Você deseja excluir {aluno_excluir.nome}? (Digite 'sim' para confirmar ou 'cancelar' para encerrar)")
                                confirmacao = input().strip().lower()
                                if confirmacao == "sim":
                                    self.alunos.pop(indice)
                                    print(f"Aluno {aluno_excluir.nome} removido da turma.")
                                    break
                                elif confirmacao == "cancelar":
                                    print("Operação cancelada.")
                                    break
                            else:
                                print("Número inválido. Tente novamente.")
                        except ValueError:
                            print("Entrada inválida. Tente novamente.")

            elif escolha == "3":  # Editar professores (similar a alunos)
                print("Deseja adicionar ou excluir professores?")
                print("1. Adicionar")
                print("2. Excluir")
                acao = input("Digite o número da ação desejada: ").strip()

                if acao == "1":  # Adicionar professor
                    while True:
                        professor = input("Insira o objeto do professor a ser adicionado (ou digite 'cancelar' para encerrar): ").strip()
                        if professor.lower() == "cancelar":
                            print("Operação cancelada.")
                            break
                        try:
                            # Aqui você valida o objeto do professor (exemplo: verificar se é uma instância de Professor)
                            if isinstance(professor, Professor):
                                print(f"Você deseja adicionar {professor.nome} à turma {self.nome}? (Digite 'sim' para confirmar ou 'cancelar' para encerrar)")
                                confirmacao = input().strip().lower()
                                if confirmacao == "sim":
                                    self.professores.append(professor)
                                    print(f"Professor {professor.nome} adicionado à turma {self.nome}.")
                                    break
                                elif confirmacao == "cancelar":
                                    print("Operação cancelada.")
                                    break
                            else:
                                print("O objeto fornecido não é um professor válido. Tente novamente.")
                        except Exception as e:
                            print(f"Erro ao adicionar professor: {e}")
                
                elif acao == "2":  # Excluir professor
                    while True:
                        print("Lista de professores:")
                        for i, professor in enumerate(self.professores, 1):
                            print(f"{i}. {professor.nome}")
                        escolha_professor = input("Digite o número do professor que deseja excluir (ou 'cancelar' para encerrar): ").strip()
                        if escolha_professor.lower() == "cancelar":
                            print("Operação cancelada.")
                            break
                        try:
                            indice = int(escolha_professor) - 1
                            if 0 <= indice < len(self.professores):
                                professor_excluir = self.professores[indice]
                                print(f"Você deseja excluir {professor_excluir.nome}? (Digite 'sim' para confirmar ou 'cancelar' para encerrar)")
                                confirmacao = input().strip().lower()
                                if confirmacao == "sim":
                                    self.professores.pop(indice)
                                    print(f"Professor {professor_excluir.nome} removido da turma.")
                                    break
                                elif confirmacao == "cancelar":
                                    print("Operação cancelada.")
                                    break
                            else:
                                print("Número inválido. Tente novamente.")
                        except ValueError:
                            print("Entrada inválida. Tente novamente.")

            elif escolha == "4":  # Editar disciplinas (similar a alunos)
                print("Deseja adicionar ou excluir disciplinas?")
                print("1. Adicionar")
                print("2. Excluir")
                acao = input("Digite o número da ação desejada: ").strip()

                if acao == "1":  # Adicionar disciplina
                    while True:
                        disciplina = input("Insira o objeto disciplina a ser adicionado (ou digite 'cancelar' para encerrar): ").strip()
                        if disciplina.lower() == "cancelar":
                            print("Operação cancelada.")
                            break
                        try:
                            # Aqui você valida o objeto disciplina (exemplo: verificar se é uma instância de Disciplina)
                            if isinstance(disciplina, Disciplina):
                                print(f"Você deseja adicionar {disciplina.descricao} à turma {self.descricao}? (Digite 'sim' para confirmar ou 'cancelar' para encerrar)")
                                confirmacao = input().strip().lower()
                                if confirmacao == "sim":
                                    self.disciplinas.append(disciplina)
                                    print(f"Disciplina {disciplina.descricao} adicionada à turma {self.descricao}.")
                                    break
                                elif confirmacao == "cancelar":
                                    print("Operação cancelada.")
                                    break
                            else:
                                print("O objeto fornecido não é uma disciplina válida. Tente novamente.")
                        except Exception as e:
                            print(f"Erro ao adicionar disciplina: {e}")
                
                elif acao == "2":  # Excluir disciplina
                    while True:
                        print("Lista de disciplinas:")
                        for i, disciplina in enumerate(self.disciplinas, 1):
                            print(f"{i}. {disciplina.descricao}")
                        escolha_disciplina = input("Digite o número da disciplina que deseja excluir (ou 'cancelar' para encerrar): ").strip()
                        if escolha_disciplina.lower() == "cancelar":
                            print("Operação cancelada.")
                            break
                        try:
                            indice = int(escolha_disciplina) - 1
                            if 0 <= indice < len(self.disciplinas):
                                disciplina_excluir = self.disciplinas[indice]
                                print(f"Você deseja excluir {disciplina_excluir.descricao}? (Digite 'sim' para confirmar ou 'cancelar' para encerrar)")
                                confirmacao = input().strip().lower()
                                if confirmacao == "sim":
                                    self.disciplinas.pop(indice)
                                    print(f"Disciplina {disciplina_excluir.descricao} removida da turma.")
                                    break
                                elif confirmacao == "cancelar":
                                    print("Operação cancelada.")
                                    break
                            else:
                                print("Número inválido. Tente novamente.")
                        except ValueError:
                            print("Entrada inválida. Tente novamente.")

            elif escolha == "5":  # Encerrar edição
                print("Edição encerrada.")
                break

            else:
                print("Opção inválida. Tente novamente.")

    def desativar(self):
        if not self.ativa:
            print(f"A turma {self.nome} já está desativada.")
        else:
            self.ativa = False  # Marca a turma como desativada
            print(f"Turma {self.nome} foi desativada.")

    def ativar(self):
        if self.ativa:
            print(f"A turma {self.nome} já está ativa.")
        else:
            self.ativa = True  # Marca a turma como ativa novamente
            print(f"Turma {self.nome} foi reativada.")
