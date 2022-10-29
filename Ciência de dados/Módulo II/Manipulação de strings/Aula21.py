"""
Manipulação de strings com Python

"""
nome = "cAroLinE"

print(nome.upper())
print(nome.lower())
print(nome.title())

texto= "  Olá sou Caroline!      "

print(texto + ".")
print(texto.strip() + ".")
print(texto.rstrip() + ".")
print(texto.lstrip() + ".")

menu = "Python"

print("####" + menu + "####")
print(menu.center(14))
print(menu.center(20, "#"))
print("P-y-t-h-o-n")
print("-".join(menu))
