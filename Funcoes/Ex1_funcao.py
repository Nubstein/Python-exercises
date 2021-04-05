#para um n informado pelo usuário.
# Use uma função que receba um valor n inteiro imprima até a n-ésima linha.

def imprimir(valor):
    if isinstance(valor, int):   #isinstance serve para identificar se se o valor digitado é numero inteiro neste caso
        x = 1                    #contador para o while
        while x <= valor:
            y = 1
            texto = ''
            while y <= x:
                texto += str(y) + str(y)
                y += 1
            print (texto)
            x += 1
imprimir(5)
