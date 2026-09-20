# int significa número inteiro: sem casas decimais e sem aspas.
# Um int pode participar de contas e comparações numéricas.
idade = 18

print("=== Números inteiros (int) ===")
print("Idade:", idade)
print("Tipo da idade:", type(idade))

# Pergunta: o que acontece se trocarmos 18 por 17?
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

# Aqui 2 é um número: o resultado da soma é 20.
print("Idade daqui a dois anos:", idade + 2)
