class Carro:

    def __init__ (self, modelo, cor, marca, preco):
        self.modelo = modelo
        self.cor = cor
        self.marca = marca
        self.preco = preco

    def Ligar_Carro(self):
        print("Ligando o carro...")

    def Acelerar_Motor_Carro(self):
        print("Acelerando motor...")
    
    def Parar_Motor_Carro(self):
        print("Parando motor...")

carro_1 = Carro('Onix', 'Branco', 'Chevrolet', 20000)
carro_1.Ligar_Carro()
carro_1.Acelerar_Motor_Carro()
carro_1.Parar_Motor_Carro()
