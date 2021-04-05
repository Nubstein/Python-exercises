# Exercício 3 - Crie uma tupla de 4 elementos, multiplique cada elemento da tupla por 2 e guarde os resultados em uma
# lista

tupla = (4, 6, 8, 10)  # Lembrar de criar lista vazia;
lista = []  # Lembrar de criar variáve;
for i in tupla:  # Lembrar sempre dos : quando usar for in
    novo_valor = i * 2  # Lembrar da função appende para atualizar lista vazia com os itens da nova variável
    lista.append(novo_valor)  # Se o print estiver identado embaixo da lista.append ira imprimir mais que uma lista
print(lista)