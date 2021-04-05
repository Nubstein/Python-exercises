#Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
# Imprima os três vetores.

#Delimitar o máximo de entradas, o (20) determina que sao 20 entradas
#Exceto a variável digito, que é um numero inteiro
# Em listas não se usa +=, o método correto é append ou remove

numero = []
par = []
impar = []

for i in range (20):
        digito = int ( input ( "Digite um número: " ) )
        numero.append ( digito )
        if ( digito % 2 ) == 0:
          par.append ( digito )
        else:
          impar.append ( digito )
print()
print ("Vetor",numero )
print ( "Números pares do vetor",par )
print ( "Números impares do vetor",impar )