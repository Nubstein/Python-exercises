#Meses com 31 dias: 1, 3, 5, 7, 8, 10 ou mês 12
#Meses com 30 dias: 4, 6, 9 e o mês 11.
#algo errado no código abaixo

d=int(input("Insira o dia: "))
m=int(input("Insira o mês: "))
a=int(input("Insira o ano: "))

if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:    #meses com 31 dias
  if d<=31:
    valida=True
if m==4 or m==6 or m==9 or m==11:  #Meses com 30 dias
  if d<=30:
    valida=True
if m==2:
  if (a%4==0 and a%100!=0) or (a%400==0):      #Ano bissexto
    if(dia<=29):
      valida = True
    elif(dia<=28):
      valida = True
if (valida):
  print("Data Valida")
else:
  print("Data Inválida")