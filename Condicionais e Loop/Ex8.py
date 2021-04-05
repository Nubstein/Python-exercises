#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
#mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
x=input("Qual turno você estuda? ")
x=x.upper()
if x=="MATUTINO" or x=="MANHÃ" or x=="M":
  print("Bom dia!")
elif x=="VESPERTINO" or x=="TARDE" or "T":
  print ("Boa Tarde!")
elif x=="NOITE" or x=="NOTURNO" or x=="N":
  print("Boa Noite!")
else:
  print("Valor Inválido")