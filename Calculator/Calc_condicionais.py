
print("1=Soma\n2=Subtração\n3=Multiplicação\n4=Divisão\n")

operacao = int(input("Selecione o número da operaçao desejada: "))
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

if operacao == 1:
    print(" A soma dos dois numeros é: ", (n1 + n2))
elif operacao == 2:
    print(" A Substração dos dois números é: ", (n1 - n2))
elif operacao == 3:
    print(" A Multiplicação dos dois números é: ", (n1 * n2))
elif operacao == 4:
    print(" A divisão dos dois números é: ", (n1 / n2))

