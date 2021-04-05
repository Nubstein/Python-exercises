#Faça um programa que peça 10 números inteiros,
# calcule e mostre a quantidade de números pares e a quantidade de números impares.

cpar=0
cimpar=0
i=0             #definir todas as variaveis. O contador é só uma variável que muda de valor a cada loop
while i <10:
    n=int(input("Insira 10 numeros: "))
    if n%2==0:
        cpar+=1
    else:
        cimpar+=1
    i+=1
print ("foram digitados", cpar, "números pares e", cimpar,"números impares")