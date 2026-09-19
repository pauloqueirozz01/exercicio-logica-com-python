# Teoria: lógica aritmética em Python

[Voltar ao início](../README.md) · [Ir para os desafios](desafios.md)

## O que é lógica aritmética?

É uma sequência de passos para transformar números em um resultado. Por exemplo, calcular o preço de uma compra exige conhecer o preço unitário e a quantidade, multiplicá-los e mostrar o total. Chamamos essas etapas de **entrada, processamento e saída**.

```python
# Entrada: valores disponíveis
a = 10
b = 5

# Processamento: cálculo
soma = a + b

# Saída: resultado apresentado
print("Soma:", soma)  # Soma: 15
```

`a`, `b` e `soma` são variáveis que guardam valores. O sinal `=` atribui o resultado da expressão à variável à esquerda. Para receber números digitados, use `input()` e converta o texto para `int` (inteiro) ou `float` (decimal):

```python
a = float(input("Primeiro número: "))
b = float(input("Segundo número: "))
print("Soma:", a + b)
```

## Operadores

| Símbolo | Operação | Exemplo | Resultado |
| --- | --- | --- | --- |
| `+` | Adição | `8 + 3` | `11` |
| `-` | Subtração | `8 - 3` | `5` |
| `*` | Multiplicação | `8 * 3` | `24` |
| `/` | Divisão comum | `8 / 2` | `4.0` |
| `//` | Divisão arredondada para baixo | `8 // 3` | `2` |
| `%` | Resto da divisão | `8 % 3` | `2` |
| `**` | Potência | `8 ** 2` | `64` |

Dividir por zero causa erro. Os parênteses mudam a ordem do cálculo: `(2 + 3) * 4` é `20`, enquanto `2 + 3 * 4` é `14`. Use parênteses quando a ordem da operação for importante.

## Exemplos de aplicação

### Total de uma compra

```python
# Entrada
preco = 12.50
quantidade = 3

# Processamento
total = preco * quantidade

# Saída
print("Total: R$", total)  # Total: R$ 37.5
```

### Converter minutos em horas e minutos

```python
minutos_totais = 135        # Entrada
horas = minutos_totais // 60  # Processamento
restante = minutos_totais % 60
print(horas, "horas e", restante, "minutos")  # Saída: 2 horas e 15 minutos
```

### Calcular uma média

```python
nota1 = 6
nota2 = 8
media = (nota1 + nota2) / 2
print("Média:", media)  # Média: 7.0
```

Os parênteses fazem as duas notas serem somadas antes da divisão. Agora resolva os [desafios de aritmética](desafios.md), começando pelas variáveis `a`, `b` e `soma`.
