# Teoria: lógica condicional em Python

[Voltar ao início](../README.md) · [Ir para os desafios](desafios.md)

## O que é lógica condicional?

É a forma de fazer um programa **tomar decisões**. Ele verifica uma condição que resulta em `True` (verdadeiro) ou `False` (falso) e executa o bloco correspondente. Exemplo: se a idade é de pelo menos 18 anos, a pessoa é maior de idade; caso contrário, é menor.

```python
# Entrada
idade = 17

# Processamento: escolher um caminho
if idade >= 18:
    mensagem = "Maior de idade"
else:
    mensagem = "Menor de idade"

# Saída
print(mensagem)  # Menor de idade
```

Como `17 >= 18` é `False`, o programa executa o bloco do `else`. O recuo de quatro espaços indica quais linhas pertencem a cada bloco. Troque `idade` por `18` e execute de novo.

## `if`, `elif` e `else`

`if` inicia a decisão. `elif` testa outra regra se as anteriores falharem. `else` cobre os casos restantes. Numa mesma cadeia, apenas o primeiro ramo verdadeiro é executado.

```python
# Entrada
numero = 0

# Processamento
if numero > 0:
    classificacao = "Positivo"
elif numero < 0:
    classificacao = "Negativo"
else:
    classificacao = "Zero"

# Saída
print(classificacao)  # Zero
```

## Comparar valores

| Operador | Significado | Exemplo verdadeiro |
| --- | --- | --- |
| `==` | Igual | `5 == 5` |
| `!=` | Diferente | `5 != 3` |
| `>` | Maior | `5 > 3` |
| `<` | Menor | `3 < 5` |
| `>=` | Maior ou igual | `5 >= 5` |
| `<=` | Menor ou igual | `3 <= 5` |

Não confunda `=` com `==`: `idade = 18` **atribui** um valor; `idade == 18` **compara** valores.

## Combinar regras com `and`, `or` e `not`

- `and`: todas as condições precisam ser verdadeiras.
- `or`: basta uma condição verdadeira.
- `not`: inverte o resultado de uma condição.

### Acesso com duas exigências (`and`)

```python
idade = 20                  # Entrada
tem_ingresso = True
if idade >= 18 and tem_ingresso:  # Processamento
    mensagem = "Entrada permitida"
else:
    mensagem = "Entrada negada"
print(mensagem)             # Saída: Entrada permitida
```

Ter apenas a idade mínima ou apenas o ingresso não basta: ambas as regras são necessárias.

### Desconto por uma de duas regras (`or`)

```python
idade = 20
estudante = True
if idade < 18 or estudante:
    print("Tem desconto")
else:
    print("Sem desconto")
```

Nesse caso, uma pessoa de 20 anos recebe o desconto porque é estudante.

### Inverter uma resposta (`not`)

```python
esta_chovendo = False
if not esta_chovendo:
    print("Pode sair sem guarda-chuva")
```

Quando combinar várias regras, use parênteses para deixar a intenção clara: `(idade >= 18 and tem_ingresso) or tem_autorizacao`.

## Usar dados digitados

`input()` sempre devolve texto. Converta a idade antes de compará-la e transforme uma resposta `s`/`n` em um valor booleano:

```python
# Entrada
idade = int(input("Idade: "))
resposta = input("Possui ingresso? (s/n): ").strip().lower()
tem_ingresso = resposta == "s"

# Processamento e saída
if idade >= 18 and tem_ingresso:
    print("Entrada permitida")
else:
    print("Entrada negada")
```

Condições servem também para classificar notas, verificar saldo para uma compra e escolher mensagens para situações diferentes. Antes de programar, escreva a regra em uma frase, identifique os dados necessários e traduza a frase para uma comparação. Depois, pratique nos [desafios de condicionais](desafios.md).
