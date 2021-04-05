#Data por extenso. Faça um programa que solicite a data de nascimento
# (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.

meses_ext= ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
data=input(" Insira uma data em formato dd/mm/aaaa: ")
data2=data.split("/")  #Split para fazer com que cada numero separadado por / barra, seja um elemento da lista data2
print(data2)
print(data2[0],"de",meses_ext[int(data2[1])-1],"de",data2[2])

#sabendo que lista data2 tem 3 elementos, pedi para imprimir o primeiro elemnto [0],
#o segundo elemento foi formado pelo segundo elemento da data2[1]-1,
#pois assim consigo uma correspondencia respectiva entre as duas listas data2 e meses_ext considerando q python indexa aparti de zero