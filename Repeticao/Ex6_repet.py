#Numa eleição existem três candidatos.
# Faça um programa que peça o número total de eleitores.
# Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

eleitores=int(input("Digite o número total de eleitores "))
c1=0
c2=0
c3=0
votantes=0

while votantes < eleitores:
  voto=int(input("Digite:\n13 para o candidato LULA\n17 para o candidato BOZO \n45 para o candidato MORO \n"))

  if  voto==13:
    c1+=1
  elif voto==17:
    c2+=1
  elif voto==45:
    c3+=1
  else:
    print("voto nulo")

  votantes+=1

print()

print ("RESULTADO: \nCandidato LULA: ",c1, "votos \n" "Candidato BOZO ", c2,"votos \nCandidato MORO ", c3,"votos" )