enunciado = """
### 4. Valor de pi com duas casas decimais

Guarde `3.14159` na variável `pi`. Arredonde esse valor para **duas casas decimais** e guarde o resultado em `pi_arredondado`. Depois, imprima a frase `O valor arredondado de pi é: {pi_arredondado}`, substituindo o trecho entre chaves pelo valor da variável.

Saída esperada:
--> O valor arredondado de pi é: 3.14
"""

print(enunciado)

pi = 3.14159;
pi_rounded = round(pi, 2)

print(f"O valor arredondado do pi é: {pi_rounded}")