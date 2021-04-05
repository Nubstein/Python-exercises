#Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado.
# Por exemplo: 127 -> 721.

def numReverso (a1):
  s=str(a1)     #transformar em string
  rev=s[::-1]    #fatiar a string de tras para frente
  return (rev)

numReverso (987)