# calculadora Python
print()
print("---> Python Calculator <---")
print()
print("1=Soma\n2=Subtração\n3=Multiplicação\n4=Divisão\n")

operacao=int(input("Escolha o número da operação desejada: "))

def soma(a,b):
    return a+b
def subtracao(a,b):
    return a-b
def multiplicacao(a,b):
    return a*b
def divisao(a,b):
    return a/b

n1=int(input("Digite o primeiro número: "))
n2=int(input("Digite o segundo número: "))


if operacao==1:
    print("n1" "+" "n2" "=", soma(n1,n2))  #chamar funcao soma
if operacao==2:
    print("%d - %d =" %(n1,n2),subtracao(n1,n2)) #chamar função substracao
if operacao==3:
    print("%d x %d = " %(n1,n2),multiplicacao(n1,n2))
if operacao==4:
    print("%d / %d = " %(n1,n2), divisao(n1,n2))

else:
    print("operação inválida")