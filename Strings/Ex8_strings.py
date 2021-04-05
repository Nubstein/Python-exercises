#Verificação de CPF.
# Desenvolva um programa que solicite a digitação de um número de CPF
# no formato xxx.xxx.xxx-xx e indique se é um número válido ou inválido
# através da validação dos dígitos verificadores edos caracteres de formatação.

cpf=input(" Insira o numero de cpf no formato xxx.xxx.xxx-xx ")
if (cpf[3]!=".") or (cpf[7]!=".") or (cpf[11]!="-"):
  input(" O cpf deve estar no formato xxx.xxx.xxx-xx ")
else:
  print (" O cpf está no formato correto")