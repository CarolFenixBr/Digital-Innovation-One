"""função : escopo e global"""

salario = 2500

def salario_bonus(bonus, lista):
    global salario

    lista_aux = lista.copy()
    lista_aux.append(2)
    print(f"lista auxiliar = {lista_aux}")

    salario += bonus
    return salario

lista = [1]
novo_salario = salario_bonus(600, lista)
print(novo_salario)
print(lista)
