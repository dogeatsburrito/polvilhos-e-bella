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
        self.lista_turmas = []
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

    def editarEstudante(self):
        while True:
            print("\nO que você deseja editar?")
            print("1. Nome do estudante")
            print("2. Endereço ")
            print("3. Responsável")
            print("4. Email do Responsável")
            print("5. Segmento")
            print("6. Turma")
            print("7. Curso")
            print("8. Usuário")
            print("9. E-mail")
            print("10. Senha")
            escolha = input("Digite o número da opção desejada: ").strip()

            if escolha == "1":  # Editar nome
                novo_nome = input("Qual será o novo nome do estudante? ").strip()
                if novo_nome.lower() == "cancelar":
                    print("Operação cancelada.")
                    continue
                self.nome = novo_nome
                print(f"O nome do estudante foi alterado para '{self.nome}'.")

            elif escolha == "2":  # Editar endereço
                novo_endereco = input("Qual será o novo endereço? ").strip()
                if novo_endereco.lower() == "cancelar":
                    print("Operação cancelada.")
                    continue
                self.endereco = novo_endereco
                print(f"O nome do ednereco foi alterado para '{self.endereco}'.")
                
            elif escolha == "3":  # Editar responsável
                novo_responsavel = input("Qual será o novo responsável? ").strip()
                if novo_responsavel.lower() == "cancelar":
                    print("Operação cancelada.")
                    continue
                self.responsavel = novo_responsavel
                print(f"O nome do responsável foi alterado para '{self.responsavel}'.")
                
            elif escolha == "4":  # Editar email do responsável
                novo_emailresponsavel = input("Qual será o novo email do responsável? ").strip()
                if novo_emailresponsavel.lower() == "cancelar":
                    print("Operação cancelada.")
                    continue
                self.emailresponsavel = novo_emailresponsavel
                print(f"O email do responsável foi alterado para '{self.emailresponsavel}'.")
                
            elif escolha == "5":  # Editar segmento
                novo_segmento = input("Qual será o novo segmento? ").strip()
                if novo_segmento.lower() == "cancelar":
                    print("Operação cancelada.")
                    continue
                self.segmento = novo_segmento
                print(f"O nome do segmento foi alterado para '{self.segmento}'.")
                
            elif escolha == "6":  # Editar turma
                print("Deseja adicionar ou excluir turmas?")
                print("1. Adicionar")
                print("2. Excluir")
                acao = input("Digite o número da ação desejada: ").strip()

                if acao == "1":  # Adicionar turma
                    while True:
                        turma = input("Insira o objeto da turma a ser adicionada (ou digite 'cancelar' para encerrar): ").strip()
                        if turma.lower() == "cancelar":
                            print("Operação cancelada.")
                            break
                        try:
                            # Aqui você valida o objeto da turma (exemplo: verificar se é uma instância de Turma)
                            if isinstance(turma, Turma):
                                print(f"Você deseja adicionar {turma.nome} ao estudante {self.nome}? (Digite 'sim' para confirmar ou 'cancelar' para encerrar)")
                                confirmacao = input().strip().lower()
                                if confirmacao == "sim":
                                    self.turmas.append(turma)
                                    print(f"Turma {turma.nome} adicionado ao estudante {self.nome}.")
                                    break
                                elif confirmacao == "cancelar":
                                    print("Operação cancelada.")
                                    break
                            else:
                                print("O objeto fornecido não é uma turma válida. Tente novamente.")
                        except Exception as e:
                            print(f"Erro ao adicionar turma: {e}")
                
                elif acao == "2":  # Excluir turma
                    while True:
                        print("Lista de turmas:")
                        for i, turma in enumerate(self.turmas, 1):
                            print(f"{i}. {turma.nome}")
                        escolha_turma = input("Digite o nome da turma que deseja excluir (ou 'cancelar' para encerrar): ").strip()
                        if escolha_turma.lower() == "cancelar":
                            print("Operação cancelada.")
                            break
                        try:
                            indice = int(escolha_turma) - 1
                            if 0 <= indice < len(self.turmas):
                                turma_excluir = self.turmas[indice]
                                print(f"Você deseja excluir {turma_excluir.nome}? (Digite 'sim' para confirmar ou 'cancelar' para encerrar)")
                                confirmacao = input().strip().lower()
                                if confirmacao == "sim":
                                    self.turmas.pop(indice)
                                    print(f"Turma {turma_excluir.nome} removido do estudante.")
                                    break
                                elif confirmacao == "cancelar":
                                    print("Operação cancelada.")
                                    break
                            else:
                                print("Nome inválido. Tente novamente.")
                        except ValueError:
                            print("Entrada inválida. Tente novamente.")
                            
            elif escolha == "7":  # Editar curso
                novo_curso = input("Qual será o novo curso? ").strip()
                if novo_curso.lower() == "cancelar":
                    print("Operação cancelada.")
                    continue
                self.curso = novo_curso
                print(f"O nome do curso foi alterado para '{self.curso}'.")
                
            elif escolha == "8":  # Editar usuario
                novo_usuario = input("Qual será o novo usuario? ").strip()
                if novo_usuario.lower() == "cancelar":
                    print("Operação cancelada.")
                    continue
                self.usuario = novo_usuario
                print(f"O nome do usuario foi alterado para '{self.usuario}'.")
                
            elif escolha == "9":  # Editar email
                novo_email = input("Qual será o novo email? ").strip()
                if novo_email.lower() == "cancelar":
                    print("Operação cancelada.")
                    continue
                self.email = novo_email
                print(f"O nome do email foi alterado para '{self.email}'.")
                
            elif escolha == "10":  # Editar senha
                nova_senha = input("Qual será a nova senha? ").strip()
                if nova_senha.lower() == "cancelar":
                    print("Operação cancelada.")
                    continue
                self.senha = nova_senha
                print(f"O nome do senha foi alterado para '{self.senha}'.")
                
            else:
                print("Opção inválida. Tente novamente.")
                
def excluirEstudante(lista_estudantes):
    if not lista_estudantes:  # Verifica se a lista está vazia
        print("Não há estudantes disponíveis para exclusão.")
        return

    while True:
        print("\nLista de estudantes disponíveis:")
        for i, estudante in enumerate(lista_estudantes, 1):
            print(f"{i}. {estudante.nome} - Responsável: {estudante.responsavel}, Turma: {estudante.turma}, Curso: {estudante.curso}")

        escolha = input("\nDigite o nome do estudante que deseja excluir (ou 'cancelar' para encerrar): ").strip()

        if escolha.lower() == "cancelar":
            print("Operação cancelada.")
            break

        try:
            indice = int(escolha) - 1  # Converte a escolha para índice
            if 0 <= indice < len(lista_estudantes):
                estudante_selecionado = lista_estudantes[indice]
                confirmacao = input(f"Tem certeza que deseja excluir o estudante '{estudante_selecionado.nome}'? (Digite 'sim' para confirmar ou 'não' para cancelar): ").strip().lower()

                if confirmacao == "sim":
                    lista_estudantes.pop(indice)  # Remove o estudante da lista
                    print(f"O estudante '{estudante_selecionado.nome}' foi excluída com sucesso.")
                    break
                elif confirmacao == "não":
                    print("Exclusão cancelada. Voltando ao menu.")
                else:
                    print("Entrada inválida. Operação não concluída.")
            else:
                print("Nome inválido. Por favor, escolha um estudante válido.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um nome correspondente a um estudante.")
