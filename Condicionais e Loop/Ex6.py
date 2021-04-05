#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
#sabendo que a decisão é sempre pelo mais barato.

p1=float(input("Insira o preco do produto 1: R$ "))
p2=float(input("Insira o preco do produto 2: R$ "))
p3=float(input("Insira o preco do produto 3: R$ "))

if p1<p2 and p1<p3:
  print(" O menor preço é: ", p1, "R$")
elif p2<p3 and p2<p1:
  print("O menor preço é: ", p2, "R$")
elif p3<p2 and p3 <p1:
  print("O menor preço é: ", p3, "R$")