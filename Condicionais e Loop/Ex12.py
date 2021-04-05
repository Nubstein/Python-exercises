#Faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
# As perguntas são:
# "Telefonou para a vítima?
# " Esteve no local do crime?
# " Mora perto da vítima?
# Devia para a vítima?"
# "Já trabalhou com a vítima?

#O programa deve no final emitir uma classificação sobre a participação da pessoa no crime
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
# Caso contrário, ele será classificado como "Inocente".

p1=input("Telefonou para a vítima? ")
p2=input("Esteve no local do crime? ")
p3=input("Mora perto da vítima? ")
p4=input("Devia para a vítima? ")
p5=input("Já trabalhou com a vítima? ")

p1=p1.lower()
p2=p2.lower()
p3=p3.lower()
p4=p4.lower()
p5=p5.lower()

lista=[p1,p2,p3,p4,p5]
lista2=lista.count("sim")
print ()
if lista2==5:
  print("ASSASSINO")
elif lista2==2:
  print("SUSPEITO")
elif lista2==3 or lista2==4:
  print("CUMPLICE")
else:
  print("INOCENTE")