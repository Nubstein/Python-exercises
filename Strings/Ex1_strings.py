#Tamanho de strings.
# Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento.
# Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

#Compara duas strings
#String 1: Brasil Hexa 2006
#String 2: Brasil! Hexa 2006!
#Tamanho de "Brasil Hexa 2006": 16 caracteres
#Tamanho de "Brasil! Hexa 2006!": 18 caracteres
#As duas strings são de tamanhos diferentes.
#As duas strings possuem conteúdo diferente.

#len para verificar comprimento da string;
#if else para comparar ==

s1= "chora não"
s2="coleguinha!"
print ("O conteúdo das strings é: ",s1,s2,)
print ("s1 tem ", len(s1), "caracteres, e s2 tem ",len(s2)," caracteres ")
print()
if len(s1)==len(s2):
  print ("As duas strings possuem o mesmo comprimento ")
else:
  print("As strings possuem comprimentos diferentes ")

if "s1"=="s2":
  print("As duas strings possuem conteúdos iguais")
else:
  print ("As duas strings possuem conteúdos diferentes")
