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
