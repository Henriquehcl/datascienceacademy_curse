# Exercício 8 - Transforme o resultado desta função range em uma lista: range(5, 45, 2)
nums = range(5, 45, 2)
lista = []
for n in nums:
    lista.append(n)
print(lista)

# outra forma
nums = range(5, 45, 2)
print(list(nums))