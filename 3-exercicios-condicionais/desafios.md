# Desafios: condições e operadores lógicos em Python

Condições permitem que o programa escolha o que fazer a partir de uma resposta `True` (verdadeiro) ou `False` (falso). Pratique os desafios na ordem, começando por uma comparação e chegando à combinação de várias regras.

## Entrada, processamento e saída

1. **Entrada:** obtenha os dados em variáveis ou com `input()`.
2. **Processamento:** compare valores e use `if`, `elif` e `else` para decidir o caminho.
3. **Saída:** mostre com `print()` a mensagem correspondente à decisão.

```python
# Entrada
idade = 18

# Processamento e saída
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")
```

O bloco dentro do `if` só é executado quando a condição é verdadeira. `elif` testa outra condição se as anteriores falharem; `else` cobre os demais casos. O recuo (indentação) define quais linhas pertencem a cada bloco.

### Comparações: produzem `True` ou `False`

| Operador | Significado | Exemplo | Resultado |
| --- | --- | --- | --- |
| `==` | Igual a | `5 == 5` | `True` |
| `!=` | Diferente de | `5 != 3` | `True` |
| `>` | Maior que | `5 > 3` | `True` |
| `<` | Menor que | `5 < 3` | `False` |
| `>=` | Maior ou igual a | `5 >= 5` | `True` |
| `<=` | Menor ou igual a | `5 <= 3` | `False` |

`=` guarda um valor; `==` compara dois valores. Por exemplo, `idade = 18` atribui o número, enquanto `idade == 18` verifica se ele é igual a `18`.

### Operadores lógicos: combinam condições

| Operador | Quando o resultado é `True` | Exemplo |
| --- | --- | --- |
| `and` | Todas as condições são verdadeiras | `idade >= 18 and tem_documento` |
| `or` | Pelo menos uma condição é verdadeira | `dia == "sábado" or dia == "domingo"` |
| `not` | A condição é falsa | `not esta_chovendo` |

```python
idade = 20
tem_documento = True
print(idade >= 18 and tem_documento)  # True
print(idade < 18 or tem_documento)    # True
print(not tem_documento)              # False
```

Em expressões combinadas, Python avalia `not` antes de `and`, e `and` antes de `or`. Use parênteses para deixar a intenção clara: `(idade >= 18 and tem_documento) or tem_autorizacao`. Python também pode parar a avaliação de `and` quando encontra `False`, ou de `or` quando encontra `True`.

**Dados digitados:** `input()` devolve texto. Para comparar números, converta: `idade = int(input("Idade: "))`. Para respostas como `s` e `n`, compare o texto digitado explicitamente: `resposta = input("Possui documento? (s/n): ").strip().lower()` e `tem_documento = resposta == "s"`. A string `"False"` não é o booleano `False`.

## Lista de exercícios

### 1. Primeira comparação

- **Entrada:** crie `a = 10` e `b = 5`.
- **Processamento:** guarde o resultado de `a > b` em `a_e_maior`.
- **Saída:** mostre o valor de `a_e_maior`. Para esses números, deve aparecer `True`.

### 2. Igual ou diferente

- **Entrada:** crie duas variáveis numéricas com o mesmo valor.
- **Processamento:** compare-as com `==` e `!=`, guardando os resultados em variáveis.
- **Saída:** mostre os dois resultados. Com valores iguais, devem ser `True` e `False`. Depois, mude um valor e observe a saída.

### 3. Maioridade

- **Entrada:** leia a idade do usuário como inteiro.
- **Processamento:** use `if` e `else` para verificar se a idade é maior ou igual a `18`.
- **Saída:** mostre `Maior de idade` ou `Menor de idade`. Teste `17` e `18`.

### 4. Número positivo, negativo ou zero

- **Entrada:** leia um número com `float()`.
- **Processamento:** use `if`, `elif` e `else` para distinguir os três casos.
- **Saída:** mostre `Positivo`, `Negativo` ou `Zero`. Teste `3`, `-2` e `0`.

### 5. Número par ou ímpar

- **Entrada:** leia um número inteiro.
- **Processamento:** calcule `numero % 2` e compare o resto com `0`.
- **Saída:** mostre `Par` ou `Ímpar`. Teste `8` e `9`.

### 6. Acesso com duas exigências (`and`)

- **Entrada:** leia a idade como inteiro e se a pessoa possui documento (`s` ou `n`).
- **Processamento:** permita o acesso quando `idade >= 18` **e** `tem_documento` forem verdadeiros.
- **Saída:** mostre `Acesso permitido` ou `Acesso negado`. Teste os dois requisitos separadamente e juntos.

### 7. Desconto por uma de duas regras (`or`)

- **Entrada:** leia a idade e se a pessoa é estudante (`s` ou `n`).
- **Processamento:** conceda desconto quando a idade for menor que `18` **ou** a pessoa for estudante.
- **Saída:** mostre `Tem desconto` ou `Sem desconto`. Teste uma pessoa de `20` anos que estuda e outra de `20` anos que não estuda.

### 8. Pode sair? (`not`)

- **Entrada:** leia se está chovendo (`s` ou `n`).
- **Processamento:** crie o booleano `esta_chovendo` e use `not esta_chovendo` na condição.
- **Saída:** mostre `Pode sair` se não estiver chovendo; caso contrário, `Leve um guarda-chuva`.

### 9. Aprovação por média e frequência

- **Entrada:** leia duas notas e a frequência em porcentagem como números.
- **Processamento:** calcule a média e aprove somente se `media >= 7` **e** `frequencia >= 75`.
- **Saída:** mostre a média e `Aprovado` ou `Reprovado`. Teste as notas `7` e `9` com frequências `80` e `70`.

## Para conferir seu aprendizado

Teste valores de fronteira, como idade `18`, média `7` e frequência `75`. Antes de rodar cada programa, escreva qual saída você espera e explique qual comparação ou operador lógico determina o resultado.
