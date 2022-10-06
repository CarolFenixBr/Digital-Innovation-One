"""in"""

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "2155-2221"},"james@gmail.com": {"nome": "James", "telefone": "3107-2121"},"caroline@gmail.com": {"nome": "Caroline", "telefone": "2101-0993"},"harry@gmail.com": {"nome": "Harry", "telefone": "3107-7777"},
}


resultado = "caroline@gmail.com" in contatos
print(resultado)

resultado = "guilherme@gmail.com" in contatos
print(resultado)

resultado = "idade" in contatos ["caroline@gmail.com"]
print(resultado)

resultado = "telefone" in contatos ["caroline@gmail.com"]
print(resultado)