#Classe Bola: Crie uma classe que modele uma bola:
#Atributos: Cor, circunferência, material
#Métodos: trocaCor e mostraCor

class Bola():
    def __init__(self, cor, circunferencia, material):
        self.cor=cor
        self.circunferencia=circunferencia
        self.material=material
        print("Objeto criado!")

    def setCor (self, nova_cor):
        self.cor= nova_cor

    def getCor (self):
        print("A nova cor é ", self.cor)
        return self.cor


b1=Bola("amarela", "redonda", "couro")
b1.setCor("vermelha")
b1.getCor()





