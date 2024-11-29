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
