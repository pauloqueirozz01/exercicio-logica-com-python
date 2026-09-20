# Primeiro, convertemos um texto definido no próprio programa.
ano_nascimento_texto = "2000"
ano_nascimento_numero = int(ano_nascimento_texto)

print("=== Conversão de um valor conhecido ===")
print("Valor original:", ano_nascimento_texto, "| tipo:", type(ano_nascimento_texto))
print("Valor convertido:", ano_nascimento_numero, "| tipo:", type(ano_nascimento_numero))
print("Ano seguinte:", ano_nascimento_numero + 1)

# input() sempre devolve str, mesmo que a pessoa digite apenas números.
print("\n=== Agora é sua vez ===")
ano_digitado = input("Digite seu ano de nascimento (exemplo: 2000): ")
print("Valor digitado: ", ano_digitado, "| tipo: ", type(ano_digitado))

# int() aceita textos que representam números inteiros, como "2000".
# Se o texto não puder ser convertido, mostramos uma orientação em vez de
# encerrar o programa com uma mensagem de erro difícil de entender.
try:
    ano_convertido = int(ano_digitado)
except ValueError:
    print("Digite apenas um ano inteiro, usando algarismos, como 2000.")
else:
    print("Valor convertido:", ano_convertido, "| tipo:", type(ano_convertido))
    print("No ano seguinte ao seu nascimento, o ano era", ano_convertido + 1)
