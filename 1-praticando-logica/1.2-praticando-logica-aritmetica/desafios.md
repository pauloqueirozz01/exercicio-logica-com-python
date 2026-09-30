# Praticando lógica aritmética

[Voltar para praticando lógica](../desafios.md) · [Consultar a teoria](../../2-exercicios-aritmeticos/teoria.md) · [Ir para lógica condicional](../1.1-praticando-logica-condicional/desafios.md)

Nesta lista, você transformará dados de entrada em resultados usando operadores aritméticos. Resolva os exercícios **na ordem** e crie um arquivo `.py` para cada um nesta pasta.

Antes de escrever o código, identifique:

1. **Entrada:** quais valores serão usados?
2. **Processamento:** qual cálculo deve ser realizado?
3. **Saída:** o que será mostrado no terminal?

Comece com valores definidos no próprio código. Quando o enunciado pedir dados ao usuário, lembre-se de que `input()` retorna texto e faça a conversão com `int()` ou `float()`.

## 1. Quatro operações

- **Entrada:** defina `a = 12` e `b = 4`.
- **Processamento:** calcule soma, subtração, multiplicação e divisão.
- **Saída:** mostre cada resultado com um rótulo.

Resultados esperados: `16`, `8`, `48` e `3.0`.

## 2. Ordem das operações

- **Entrada:** defina `a = 2`, `b = 3` e `c = 4`.
- **Processamento:** calcule `a + b * c`, `(a + b) * c` e `a ** b`.
- **Saída:** mostre `14`, `20` e `8`.

Explique em um comentário por que os dois primeiros resultados são diferentes.

## 3. Divisão, quociente e resto

- **Entrada:** use `17` como dividendo e `5` como divisor.
- **Processamento:** calcule os resultados de `/`, `//` e `%` em variáveis diferentes.
- **Saída:** mostre `3.4`, `3` e `2`, identificando cada operação.

Depois, troque o dividendo por `20` e tente prever os três resultados antes de executar.

## 4. Média de três notas

- **Entrada:** leia três notas usando `float(input(...))`.
- **Processamento:** some as notas e divida o total por `3`.
- **Saída:** mostre a média com uma casa decimal.

As entradas `6`, `7` e `8` devem produzir `Média: 7.0`.

## 5. Conversor de tempo

- **Entrada:** leia uma quantidade total de segundos como inteiro.
- **Processamento:** use `//` e `%` para separar o total em horas, minutos e segundos.
- **Saída:** para `3672`, mostre `1 hora, 1 minuto e 12 segundos`.

Dica: depois de descobrir as horas, calcule o restante que ainda precisa ser convertido.

## 6. Área e perímetro

- **Entrada:** leia a largura e o comprimento de um terreno como números decimais.
- **Processamento:** calcule a área com `largura * comprimento` e o perímetro com `2 * (largura + comprimento)`.
- **Saída:** mostre os dois resultados com duas casas decimais.

Para largura `5` e comprimento `8`, a área é `40.00` e o perímetro é `26.00`.

## 7. Compra e troco

- **Entrada:** leia o preço unitário, a quantidade comprada e o valor pago.
- **Processamento:** calcule o subtotal e o troco.
- **Saída:** mostre subtotal e troco com duas casas decimais.

Preço `12.50`, quantidade `2` e pagamento `30` devem produzir subtotal `25.00` e troco `5.00`. Neste exercício, considere que o pagamento sempre é suficiente.

## 8. Desconto percentual

- **Entrada:** leia o preço de um produto e o percentual de desconto.
- **Processamento:** transforme o percentual em uma fração, calcule o desconto e subtraia-o do preço.
- **Saída:** mostre preço original, valor do desconto e preço final com duas casas decimais.

Preço `200` e desconto de `15%` devem produzir desconto de `30.00` e preço final de `170.00`.

## 9. Reajuste de salário

- **Entrada:** leia o salário atual e o percentual de reajuste.
- **Processamento:** calcule o valor do aumento e o novo salário.
- **Saída:** mostre os dois valores com duas casas decimais.

Salário `1500` e reajuste de `8%` devem produzir aumento de `120.00` e novo salário de `1620.00`.

## 10. Consumo de combustível

- **Entrada:** leia a distância percorrida em quilômetros e a quantidade de combustível utilizada em litros.
- **Processamento:** calcule o consumo médio em quilômetros por litro.
- **Saída:** mostre o resultado com duas casas decimais.

Uma viagem de `420 km` que consumiu `35 litros` deve resultar em `12.00 km/l`. Considere, por enquanto, que a quantidade de litros é maior que zero.

## Desafio final — Divisão de uma conta

Um grupo quer dividir a conta de um restaurante e deixar uma gorjeta.

- **Entrada:** leia o valor da conta, o percentual de gorjeta e a quantidade de pessoas.
- **Processamento:** calcule a gorjeta, o total com a gorjeta e o valor que cada pessoa pagará.
- **Saída:** mostre todos os valores com duas casas decimais.

Para uma conta de `180`, gorjeta de `10%` e `3` pessoas, mostre:

```text
Gorjeta: R$ 18.00
Total: R$ 198.00
Valor por pessoa: R$ 66.00
```

Considere que a quantidade de pessoas é maior que zero. A validação desse dado será praticada na lista de lógica condicional.

## Confira seu aprendizado

Antes de executar cada programa, anote o resultado esperado. Depois, altere as entradas e confirme se o cálculo continua correto. Mostre temporariamente os valores intermediários com `print()` quando precisar descobrir em qual etapa um resultado mudou.
