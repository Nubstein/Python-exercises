# Exercício 4 - Crie uma função que receba um argumento formal e uma possível lista de elementos. Faça duas chamadas
# à função, com apenas 1 elemento e na segunda chamada com 4 elementos

def fformal(*a):
    lista = []
    for item in a:
        lista.append(item)
    return lista


# Chamar a função

fformal("Nubia", "Vini", 3, 8, 5.9)
