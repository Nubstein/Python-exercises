# Classe Quadrado: Crie uma classe que modele um quadrado:
# Atributos: Tamanho do lado
# Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

class Quadrado():
    def __init__(self, lado):
        self.lado = lado
        print("Objeto Criado!")

    def area (self):
        area = self.lado ** 2
        print("A area do seu quadrado é: ", area)

    def setLado(self, novo_lado):
        self.lado = novo_lado

    def getLado(self):
        print("Nova medida de lado: ", self.lado)
        return self.lado

# Instanciando objeto:

q1 = Quadrado(4)
print(q1.area())

#Chamar Método Mudar Valor do Lado

q1.setLado(8)
q1.getLado()
q1.area()