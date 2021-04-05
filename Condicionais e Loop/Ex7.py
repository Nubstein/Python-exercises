#Faça um Programa que leia três números e mostre-os em ordem decrescente.

lista=[]
for n in range (3):
  n=int(input("Insira um numero "))
  lista.append(n)
lista.sort()
print("Ordem crescente ",lista)
print()
print("Ordem decrescente ", lista[2:1:0])