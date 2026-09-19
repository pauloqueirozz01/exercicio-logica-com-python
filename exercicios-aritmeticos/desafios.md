# Desafios: operadores aritméticos em Python

Esta lista começa com valores definidos no código e avança até valores digitados pelo usuário. Resolva os desafios na ordem: cada um acrescenta uma ideia nova.

## Como pensar em cada programa

1. **Entrada:** quais valores o programa precisa? Eles podem ser atribuídos a variáveis (`a = 10`) ou digitados com `input()`.
2. **Processamento:** qual conta transforma esses valores no resultado desejado?
3. **Saída:** o que deve aparecer na tela? Use `print()` para mostrar o resultado.

Em Python, `=` **atribui** um valor a uma variável. Por exemplo, `soma = a + b` calcula `a + b` e guarda o resultado em `soma`.

```python
# Entrada
a = 10
b = 5

# Processamento
soma = a + b

# Saída
print("Soma:", soma)  # Soma: 15
```

### Operadores principais

| Operador | Operação | Exemplo | Resultado |
| --- | --- | --- | --- |
| `+` | Adição | `10 + 3` | `13` |
| `-` | Subtração | `10 - 3` | `7` |
| `*` | Multiplicação | `10 * 3` | `30` |
| `/` | Divisão comum | `10 / 3` | `3.333...` (número decimal) |
| `//` | Divisão pelo piso | `10 // 3` | `3` |
| `%` | Resto da divisão | `10 % 3` | `1` |
| `**` | Potência | `10 ** 3` | `1000` |

**Atenção:** com números negativos, `//` arredonda para baixo: `-10 // 3` resulta em `-4`. O operador `%` devolve o resto correspondente: `-10 % 3` resulta em `2`. Dividir por zero causa erro.

`*`, `/`, `//` e `%` são calculados antes de `+` e `-`; `**` tem prioridade maior. Use parênteses quando quiser deixar a ordem explícita: `(2 + 3) * 4` resulta em `20`, enquanto `2 + 3 * 4` resulta em `14`.

`input()` devolve texto. Para fazer contas com valores digitados, converta-os:

```python
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
```

Use `int()` se o exercício pedir apenas números inteiros. Para executar um arquivo, use `python3 nome-do-arquivo.py` na pasta correspondente.

## Lista de exercícios

### 1. Primeira soma

- **Entrada:** crie `a = 8` e `b = 4`.
- **Processamento:** crie `soma` para receber `a + b`.
- **Saída:** mostre `Soma: 12`.

### 2. Diferença e produto

- **Entrada:** crie `a = 15` e `b = 6`.
- **Processamento:** guarde `a - b` em `diferenca` e `a * b` em `produto`.
- **Saída:** mostre os dois resultados com rótulos. Para esses valores, devem ser `9` e `90`.

### 3. Três tipos de divisão

- **Entrada:** use os inteiros `a = 17` e `b = 5`.
- **Processamento:** calcule `a / b`, `a // b` e `a % b` em variáveis separadas.
- **Saída:** mostre `3.4`, `3` e `2`, identificando cada operação.

### 4. Potência e ordem das operações

- **Entrada:** crie `a = 2`, `b = 3` e `c = 4`.
- **Processamento:** calcule `a + b * c`, `(a + b) * c` e `a ** b`.
- **Saída:** mostre `14`, `20` e `8`. Explique em um comentário por que os dois primeiros resultados diferem.

### 5. Soma digitada pelo usuário

- **Entrada:** leia dois números com `input()` e converta-os com `float()`.
- **Processamento:** some os números em uma variável `soma`.
- **Saída:** mostre o resultado. Exemplo: entradas `2.5` e `3` devem produzir `5.5`.

### 6. Média de três notas

- **Entrada:** leia três notas com `float(input(...))`.
- **Processamento:** some as notas e divida o total por `3`.
- **Saída:** mostre a média. Exemplo: `6`, `7` e `8` produzem `7.0`.

### 7. Minutos em horas

- **Entrada:** leia um total de minutos como inteiro.
- **Processamento:** use `//` para obter as horas completas e `%` para obter os minutos restantes.
- **Saída:** para `135`, mostre `2 horas e 15 minutos`.

### 8. Conta de compras

- **Entrada:** leia o preço unitário de um produto (`float`), a quantidade (`int`) e o valor pago (`float`).
- **Processamento:** calcule o total com multiplicação e o troco com subtração.
- **Saída:** mostre total e troco. Exemplo: preço `12.50`, quantidade `2` e pagamento `30` produzem total `25.0` e troco `5.0`. Considere, por enquanto, que o valor pago é suficiente.

## Para conferir seu aprendizado

Antes de executar, tente prever a saída de cada programa. Depois, altere os valores de entrada e veja se o resultado continua correto. Em contas com divisão, experimente também um divisor diferente de `1` para perceber a diferença entre `/`, `//` e `%`.
