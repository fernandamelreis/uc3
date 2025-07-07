class Pessoa:
    def __init__(self, nome, idade, CPF, genero, email, senha):
        self.nome = nome
        self.idade = idade
        self.CPF = CPF
        self.genero = genero
        self.email = email
        self.senha = senha
        
    def Info_Pessoa(self):
        
        print("---- INFORMAÇÕES PESSOAIS ----")
        print("Nome: ", self.nome)
        print("Idade: ", self.idade)
        print("CPF: ", self.CPF)
        print("Gênero:" , self.genero)
        print("E-mail:" , self.email)
        print("Senha: *******")
        print("-----------------------------")
        
pessoa_1 = Pessoa('Fernanda', '28 anos', '111.111.111-11', 'Feminino', 'fernanda.reis@pe.senac.br', '12345678')
pessoa_1.Info_Pessoa()

