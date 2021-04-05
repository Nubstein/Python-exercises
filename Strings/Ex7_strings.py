#Conta espaços e vogais.
# Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco),
# conte:
#quantos espaços em branco existem na frase.     count ( ) contando o numero de vezes que o espaço aparece
#quantas vezes aparecem as vogais a, e, i, o, u. count (a,e,i,o,u)
#placeholder de string é %S e de numeros é %d
#escreva tudo entre""", nao use virgula antes de apontar o vetor do placeholder

frase=input("Insira uma frase: ")
espaco=frase.count(" ")
vogais = 0
for caracter in frase:
  if caracter in 'aeiou':
    vogais = vogais + 1
print("A sua frase possui %d espaços em branco e %d vogais" % (espaco,vogais))