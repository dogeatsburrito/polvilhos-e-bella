from Pessoa import Pessoa
class Professor(Pessoa):
    def __init__(self, nome, endereco, formacao, Disciplinas, segmentos, Turmas, usuario, email, senha):
        super().__init__(nome, endereco, usuario, email, senha)
        self.ativa= True
        self.formacao= formacao
        self.disciplinas= Disciplinas
        self.segmento = segmentos
        self.turma = Turmas

    def desativar(self):
        if not self.ativa:
            print(f"O professor {self.nome} já está desativo")
        else:
            self.ativa = False  # Marca o professor como desativada
            print(f"Professor {self.nome} foi desativado.")

    def ativar(self):
        if self.ativa:
            print(f"O professor {self.nome} já está ativo.")
        else:
            self.ativa = True  # Marca professor como ativa novamente
            print(f"Professor {self.nome} foi reativado.")

    def editarProfessor(self):
        while True:
            print("\nO que você deseja editar?")
            print("1. Formação")
            print("2. Segmento")
            print("3. Turma")
            print("4. Disciplinas")
            print("5. Encerrar edição")
            escolha = input("Digite o número da opção desejada: ").strip()

            if escolha == "1":  # Editar formação
                nova_formacao = input("Qual será a formação? ").strip()
                if nova_formacao.lower() == "cancelar":
                    print("Operação cancelada.")
                    continue
                self.formacao = nova_formacao
                print(f"A formação foi alterada para '{self.formacao}'.")

            elif escolha == "2":  # Editar segmento
                novo_segmento = input("Qual será o novo segmento? ").strip()
                if novo_segmento.lower() == "cancelar":
                    print("Operação cancelada.")
                    continue
                self.segmento = novo_segmento
                print(f"O nome do segmento foi alterado para '{self.segmento}'.")

            elif escolha == "3":  # Editar turma
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
                                print(f"Você deseja adicionar {turma.nome} ao professor {self.nome}? (Digite 'sim' para confirmar ou 'cancelar' para encerrar)")
                                confirmacao = input().strip().lower()
                                if confirmacao == "sim":
                                    self.turmas.append(turma)
                                    print(f"Turma {turma.nome} adicionado ao professor {self.nome}.")
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
                                    print(f"Turma {turma_excluir.nome} removido do professor.")
                                    break
                                elif confirmacao == "cancelar":
                                    print("Operação cancelada.")
                                    break
                            else:
                                print("Nome inválido. Tente novamente.")
                        except ValueError:
                            print("Entrada inválida. Tente novamente.")

            elif escolha == "4":  # Editar disciplinas
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
                            if isinstance(professor, Disciplina):
                                print(f"Você deseja adicionar {disciplina.descricao} ao professor {self.nome}? (Digite 'sim' para confirmar ou 'cancelar' para encerrar)")
                                confirmacao = input().strip().lower()
                                if confirmacao == "sim":
                                    self.disciplinas.append(professor)
                                    print(f"Disciplina {disciplina.descricao} adicionada ao professor {self.nome}.")
                                    break
                                elif confirmacao == "cancelar":
                                    print("Operação cancelada.")
                                    break
                            else:
                                print("O objeto fornecido não é uma disciplina válida. Tente novamente.")
                        except Exception as e:
                            print(f"Erro ao adicionar disciplina: {e}")
                
                elif acao == "2":  # Excluir disicplina
                    while True:
                        print("Lista de disciplinas:")
                        for i, disciplina in enumerate(self.disciplinas, 1):
                            print(f"{i}. {disciplina.descricao}")
                        escolha_disciplina = input("Digite o número da professor que deseja excluir (ou 'cancelar' para encerrar): ").strip()
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
                                    print(f"Disciplina {disciplina_excluir.descricao} removida do professor.")
                                    break
                                elif confirmacao == "cancelar":
                                    print("Operação cancelada.")
                                    break
                            else:
                                print("Descrição inválida. Tente novamente.")
                        except ValueError:
                            print("Entrada inválida. Tente novamente.")

            elif escolha == "5":  # Encerrar edição
                print("Edição encerrada.")
                break

            else:
                print("Opção inválida. Tente novamente.")
                
def excluirProfessor(lista_professores):
    if not lista_professores:  # Verifica se a lista está vazia
        print("Não há professores disponíveis para exclusão.")
        return

    while True:
        print("\nLista de professores disponíveis:")
        for i, professor in enumerate(lista_professores, 1):
            print(f"{i}. {professor.nome} - Formacao: {professor.formacao}, Disciplina: {professor.disciplina}, Segmento: {professor.segmento}")

        escolha = input("\nDigite o nome do professor que deseja excluir (ou 'cancelar' para encerrar): ").strip()

        if escolha.lower() == "cancelar":
            print("Operação cancelada.")
            break

        try:
            indice = int(escolha) - 1  # Converte a escolha para índice
            if 0 <= indice < len(lista_professores):
                professor_selecionado = lista_professores[indice]
                confirmacao = input(f"Tem certeza que deseja excluir o professor '{professor_selecionado.nome}'? (Digite 'sim' para confirmar ou 'não' para cancelar): ").strip().lower()

                if confirmacao == "sim":
                    lista_professores.pop(indice)  # Remove o professor da lista
                    print(f"O professor '{professor_selecionado.nome}' foi excluída com sucesso.")
                    break
                elif confirmacao == "não":
                    print("Exclusão cancelada. Voltando ao menu.")
                else:
                    print("Entrada inválida. Operação não concluída.")
            else:
                print("Nome inválido. Por favor, escolha uma disciplina válida.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um nome correspondente a um professor.")
