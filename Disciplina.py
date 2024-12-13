class Disciplina:
    def __init__(self, id, descricao, segmento, Professores):
        self.ativa= True
        self.descricao= descricao
        self.segmento= segmento
        self.professores= Professores

    def desativar(self):
        if not self.ativa:
            print(f"A disciplina {self.nome} já está desativa")
        else:
            self.ativa = False  # Marca a disciplina como desativada
            print(f"Disciplina {self.nome} foi desativada.")

    def ativar(self):
        if self.ativa:
            print(f"A disciplina {self.nome} já está ativa.")
        else:
            self.ativa = True  # Marca a disciplina como ativa novamente
            print(f"Disciplina {self.nome} foi reativada.")

    def editarDisciplina(self):
        while True:
            print("\nO que você deseja editar?")
            print("1. Descricao")
            print("2. Professores")
            print("3. Segmento")
            print("4. Encerrar edição")
            escolha = input("Digite o número da opção desejada: ").strip()

            if escolha == "1":  # Editar descricao
                nova_descricao = input("Qual será a nova descrição da turma? ").strip()
                if nova_descricao.lower() == "cancelar":
                    print("Operação cancelada.")
                    continue
                self.descricao = nova_descricao
                print(f"O nome da turma foi alterado para '{self.descricao}'.")


            elif escolha == "2":  # Editar professores
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
                                print(f"Você deseja adicionar {professor.nome} à disciplina {self.nome}? (Digite 'sim' para confirmar ou 'cancelar' para encerrar)")
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

            elif escolha == "3":  # Editar segmento 
                novo_segmento = input("Qual será o novo segmento? ").strip()
                if novo_segmento.lower() == "cancelar":
                    print("Operação cancelada.")
                    continue
                self.segmento = novo_segmento
                print(f"O nome do segmento foi alterado para '{self.segmento}'.")

            elif escolha == "4":  # Encerrar edição
                print("Edição encerrada.")
                break

            else:
                print("Opção inválida. Tente novamente.")
                
def excluirDisciplina(lista_disciplinas):
    if not lista_disciplinas:  # Verifica se a lista está vazia
        print("Não há disciplinas disponíveis para exclusão.")
        return

    while True:
        print("\nLista de disciplinas disponíveis:")
        for i, disciplina in enumerate(lista_disciplinas, 1):
            print(f"{i}. {disciplina.nome} - Id: {disciplina.id}, Descricao: {disciplina.descricao}, Segmento: {disciplina.segmento}")

        escolha = input("\nDigite o número da disciplina que deseja excluir (ou 'cancelar' para encerrar): ").strip()

        if escolha.lower() == "cancelar":
            print("Operação cancelada.")
            break

        try:
            indice = int(escolha) - 1  # Converte a escolha para índice
            if 0 <= indice < len(lista_disciplinas):
                disciplina_selecionada = lista_disciplinas[indice]
                confirmacao = input(f"Tem certeza que deseja excluir a disciplina '{disciplina_selecionada.nome}'? (Digite 'sim' para confirmar ou 'não' para cancelar): ").strip().lower()

                if confirmacao == "sim":
                    lista_disciplina.pop(indice)  # Remove a disciplina da lista
                    print(f"A disciplina '{disciplina_selecionada.nome}' foi excluída com sucesso.")
                    break
                elif confirmacao == "não":
                    print("Exclusão cancelada. Voltando ao menu.")
                else:
                    print("Entrada inválida. Operação não concluída.")
            else:
                print("Número inválido. Por favor, escolha uma disciplina válida.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número correspondente a uma disciplina.")
