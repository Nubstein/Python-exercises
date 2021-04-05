#Faça um programa para a leitura de duas notas parciais de um aluno.
# O programa deve calcular a média alcançada por aluno e apresentar: A mensagem "Aprovado",
# se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

nota1=float(input("Insira a primeira nota: "))
nota2=float(input("Insira a segunda nota: "))
media=float(nota1+nota2)/2
print ("Sua média é: ",media )
if 7<=media<=9.9:
  print("Aprovado!")
elif media==10:
  print ("Aprovado com Distinção!")
elif media>10:
  print("Confira as notas inseridas, pois algo de errado não está certo ")
else:
  print("Reprovado!")
