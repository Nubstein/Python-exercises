# Exercício 3 - Crie a classe Smartphone com 2 atributos, tamanho e interface e
# crie a classe MP3Player com os
# atributos capacidade. A classe MP3player deve herdar os atributos da classe Smartphone.

class Smartphone():
    def __init__(self,tamanho, interface):
        self.tamanho=tamanho
        self.interface=interface

    def daroi(self):
        print("oi")

class Mp3Player(Smartphone):
    def __init__(self,capacidade, tamanho, interface):
        super().__init__(tamanho, interface)
        self.capacidade=capacidade
    def __str__(self):
        return "Capacidade %s, Tamanho: %s, Interface: %s" % (self.capacidade,self.tamanho,self.interface)

teste=Mp3Player(30,20,"b")
print(teste)
teste.daroi()
