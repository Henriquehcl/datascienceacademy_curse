# Exercício 3 - Crie uma tupla de 4 elementos, multiplique cada elemento da tupla por 2 e guarde os resultados em uma
# lista

tupla1 = (1, 2, 3, 4)
lista = []
for elemento in tupla1:
    multiplicar = elemento * 2
    lista.append(multiplicar)
    print(lista)