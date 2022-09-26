"""Interpolação de variáveis"""

nome =  "Caroline"
idade = 29
profissão = "Estudante"
linguagem = "Python"
saldo = 15.356

dados= {"nome": "Caroline", "idade": 29}

print("Nome: %s, idade: %d" % (nome, idade))

print("Nome: {}, idade: {}".format(nome,idade))

print("Nome: {1}, idade: {0}".format(idade,nome))
print("Nome: {1}, idade: {0}, Nome:{1} {1}".format(idade, nome))

print("Nome: {nome}, idade: {idade}".format(nome = nome, idade =idade))
print("Nome: {name}, idade: {age}".format(age= idade, name =nome))
print("Nome: {nome}, idade: {idade}".format(**dados))

print(f"Nome: {nome}, idade: {idade}")
print(f"Nome: {nome}, idade: {idade}, saldo: {saldo:.2f}")
print(f"Nome: {nome}, idade: {idade}, saldo: {saldo:10.1f}")
