#Classe Pessoa: Crie uma classe que modele uma pessoa:
#Atributos: nome, idade, peso e altura
#Métodos: Envelhecer, engordar, emagrecer, crescer.
# #Obs: Por padrão, a cada ano que nossa pessoa envelhece,
# #sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.

class Pessoa():
    def __init__(self,nome,idade,peso,altura):
        self.nome=nome
        self.idade=idade
        self.peso=peso
        self.altura=altura
        print(" Você instanciou um objeto na classe Pessoa! ")

    def setIdade(self,anos_passados):
        self.idade=self.idade+anos_passados

    def setAltura(self,crescimento):
        self.altura=self.altura+crescimento

    def Crescer(self,anos_passados):
        crescimento = anos_passados*0.05
        self.setAltura(crescimento)

    def Envelhecer(self,anos_passados):
        if(self.idade>=21):
            self.setIdade(anos_passados)
            print(" Agora %s tem  %s anos e tem %s de altura" % (self.nome, self.idade,self.altura))
        else:
            self.Crescer(anos_passados)
            self.setIdade(anos_passados)
            print("Passaram-se %s anos, %s agora tem %s de idade, e %s de altura"%(anos_passados,\
            self.nome,self.idade,self.altura))

    def setPeso(self,ganho_peso):
        self.peso = self.peso+ganho_peso

    def Engordar(self,ganho_peso):
        self.setPeso(ganho_peso)
        print("%s ganhou %s e agora pesa %s"%(self.nome,ganho_peso,self.peso))

    def Emagrecer(self,perda_peso):
        self.setPeso(-(perda_peso))
        print("%s perdeu %s e agora pesa %s" % (self.nome,perda_peso, self.peso))



p1=Pessoa("Nubia",18,50,1.00)
p1.Envelhecer(3)
print(p1.altura)