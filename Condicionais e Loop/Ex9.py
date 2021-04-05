#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores
#e lhe contraram para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério,
# baseado no salário atual:

#Informe na tela
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.

#salários até R$ 280,00 (incluindo) : aumento de 20%
print()
print()
s=int(input("Insira seu salário atual: "))
if s<=280:
    sn=(0.2*s)+s
    print ("Seu salário atual é ", s, "você terá 20% de aumento \n Correpondente á ",(0.2*s),"reais, logo seu novo salário é ", sn, "reais")

#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
if 280<=s<=700:
  sn=(0.15*s)+s
  print ("Seu salário atual é ", s, "você terá 15% de aumento \n Correpondente á ",(0.15*s),"reais, logo seu novo salário é ", sn, "reais")

#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
if 700<=s<=1500:
  sn=(0.1*s)+s
  print ("Seu salário atual é ", s, "você terá 10% de aumento \n Correpondente á ",(0.1*s),"reais, logo seu novo salário é ", sn, "reais")

#salários de R$ 1500,00 em diante : aumento de 5%
if s>=1500:
  sn=(0.05*s)+s
  print ("Seu salário atual é ", s, "você terá 5% de aumento \n Correpondente á ",(0.05*s),"reais, logo seu novo salário é ", sn, "reais")