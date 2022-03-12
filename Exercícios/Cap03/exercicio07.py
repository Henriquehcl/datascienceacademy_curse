# Exercício 7 - Crie uma lista vazia e uma variável com valor 4. Enquanto o valor da variável for menor ou igual a 20,
# adicione à lista, apenas os valores pares e imprima a lista

lista = []
n = 4

while n <= 20:
    pares = n % 2
    if pares == 0:
        lista.append(n)
    n += 1
print(lista)
