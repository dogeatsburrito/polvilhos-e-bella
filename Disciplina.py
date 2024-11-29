class Disciplina:
    def __init__(self, id, descricao, segmento, Professores):
        self.ativa= True
        self.id= id
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
