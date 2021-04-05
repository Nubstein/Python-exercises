#Faça um programa que use a função valorPagamento para determinar o valor a ser pago
# por uma prestação de uma conta.
# O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso
# e passar estes valores para a função valorPagamento,
# que calculará o valor a ser pago e devolverá este valor ao programa que a chamou.
# O programa deverá então exibir o valor a ser pago na tela.
# Após a execução o programa deverá voltar a pedir outro valor de prestação
# e assim continuar até que seja informado um valor igual a zero para a prestação.
# Neste momento o programa deverá ser encerrado, exibindo o relatório do dia,
# que conterá a quantidade e o valor total de prestações pagas no dia.
# O cálculo do valor a ser pago é feito da seguinte forma.
# Para pagamentos sem atraso, cobrar o valor da prestação.
# Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.

def valorAtualizado(valorPrest, diasAtraso):
    if diasAtraso >= 1:
        juros = (diasAtraso * 0.01) * valorPrest
        multa = valorPrest * 0.03
        valor_atual = valorPrest + multa + juros


valorcorrigido = []
valorPrest = 0
diasAtraso = 0
quantParcelas = 0
valorTotal = 0

while True:
    quantParcelas += 1
    valorPrest = float(input("Informe o valor da prestação: "))
    diasAtraso = int(input("Informe a quantidade de dias em atraso: "))
    juros = (diasAtraso * 0.01) * valorPrest
    multa = valorPrest * 0.03
    valor_atual = valorPrest + multa + juros
    print(
        "Sua parcela de R$ %d,00 está em %d dias em atraso\nO valor corrigido R$ %d,00 sendo juros de R$ %d,00,  e multa de R$ %d,00 " % (
        valorPrest, diasAtraso, valor_atual, juros, multa))
    print()
    if valorPrest == 0:
        break
    valor.append(valorAtualizado(valorPrest, diasAtraso))

quantParcelas -= 1
for i in range(quantParcelas):
    valorTotal += valor[i]

print('Relatorio do dia: foram pagas %d prestacoes no valor total de R$ %d,00' % (quantParcelas, valor))
print('Valor total de prestacoes pagas: ', valortotal)