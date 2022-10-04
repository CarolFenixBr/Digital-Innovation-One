"""Métodos da classe list copy"""
lista = [1, "Python", [50,65,10]]

l2 = lista.copy()

print(lista)

print(id(l2), id(lista))

l2[0] = 2

print(l2)
print(lista)