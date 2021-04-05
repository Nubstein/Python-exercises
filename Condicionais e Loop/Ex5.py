#Faça um Programa que leia três números e mostre o maior e o menor deles

n1=float(input("Insira um numero "))
n2=float(input("Insira outro numero "))
n3=float(input("Insira mais um numero "))
lista=[n1,n2,n3]
print("Você informou os números: ",lista)
print("O maior número é: ",max(lista))
print("O menor número é: ",min(lista))