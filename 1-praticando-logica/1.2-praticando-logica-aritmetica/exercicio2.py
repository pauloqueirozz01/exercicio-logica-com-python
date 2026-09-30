# 2. Ordem das operações

# - **Entrada:** defina `a = 2`, `b = 3` e `c = 4`.
# - **Processamento:** calcule `a + b * c`, `(a + b) * c` e `a ** b`.
# - **Saída:** mostre `14`, `20` e `8`.

# Explique em um comentário por que os dois primeiros resultados são diferentes.
print("Ordem das operações.")

a = 2
b = 3
c = 4

primeiro_calculo = (a + b * c)
print(f"Resultado do calculo (a + b * c) = {primeiro_calculo}")
# Nesse caso, seguindo a lógica de expresssões numéricas, a multiplicação e divisão vêm antes. 
# b * c = 3 * 4 = 12 + a -> 12 + 2 = 14

segundo_calculo = (a + b) * c
print(f"Resultado do calculo ( (a + b) * c) = {segundo_calculo}")
# Neste calculo, pegamos ( a soma do que há dentro de parênteses ) e multiplicamos o resultado por C
# Neste caso, 
# (2 + 3) * 4
# 5 * 4 = 20

terceiro_calculo = a ** b
print(f"Resultado do calculo (a ˆ b) = {terceiro_calculo}")
# No terceiro calculo, estamos fazendo a operação de potencia, estamos elevando o numero a ao numero b
# Processo bem conhecimento, com 2ˆ3 = 8
# Se lê, 2 elevado a 3 é igual a 8