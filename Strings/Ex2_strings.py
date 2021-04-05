#Nome ao contrário em maiúsculas.
# Faça um programa que permita ao usuário digitar o seu nome
# e em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas.
# Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.

#string[inicio:fim:passo]
#print(variável[::-1])

s=input("Insira seu nome ")
maiusculo=s.upper()

print(maiusculo[::-1])
