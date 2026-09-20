# Praticando `str` e `int`

Nesta etapa, você vai descobrir por que `18` e `"18"` parecem iguais na tela, mas se comportam de maneiras diferentes. Comece com [`int.py`](int.py), siga para [`str.py`](str.py) e termine com [`manipulando_int_str.py`](manipulando_int_str.py).

Na raiz do repositório, execute um arquivo por vez:

```bash
python3 1-praticando-logica/1.3-praticando-variaveis-str-int/int.py
python3 1-praticando-logica/1.3-praticando-variaveis-str-int/str.py
python3 1-praticando-logica/1.3-praticando-variaveis-str-int/manipulando_int_str.py
```

No Windows, troque `python3` por `python` ou `py`, conforme o comando que funcionou no [tutorial de instalação](../../instalando-python.md). **Execute os arquivos como indicado**, sem entrar na pasta e iniciar o interpretador interativo: o arquivo `str.py` tem o nome de um tipo interno do Python e, em alguns contextos, arquivos locais com esse nome podem atrapalhar importações.

## 1. O que é `int`?

`int` é o tipo usado para **números inteiros**, como `18`, `0` e `-5`. Em [`int.py`](int.py), a idade é um número:

```python
idade = 18
print(type(idade))  # <class 'int'>
print(idade + 2)     # 20
```

`type()` revela o **tipo** de um valor. A saída `<class 'int'>` significa que Python reconhece `idade` como um inteiro. Com esse tipo, `+` soma e `>=` compara números. A expressão `idade >= 18` pergunta se a idade é **maior ou igual a** 18.

**Antes de executar:** se você trocar `idade = 18` por `idade = 17`, qual mensagem aparecerá na condição? Execute e confira.

## 2. O que é `str`?

`str` é o tipo usado para **texto**, também chamado de *string*. As aspas fazem diferença: `"18"` contém os caracteres `1` e `8`, mas ainda é texto. Em [`str.py`](str.py):

```python
idade_texto = "18"
print(type(idade_texto))  # <class 'str'>
print(idade_texto + "2") # 182
```

Com dois textos, `+` **junta** os caracteres: `"18" + "2"` vira `"182"`. O resultado aparece sem aspas no `print()`, mas continua sendo texto. As aspas no código indicam como o valor foi criado; `type()` permite confirmar seu tipo.

**Antes de executar:** `"18" + "2"` mostra `20` ou `182`? E `18 + 2`? Teste nos dois arquivos.

## 3. Uma pergunta clássica: qual é a saída?

Leia sem executar primeiro:

```python
idade = "18"
if idade < 18:
    print("Você é menor de idade.")
else:
    print("Você é maior de idade.")
```

**Resposta:** nenhuma das duas frases aparece. Python mostra um `TypeError`, porque não consegue comparar o texto `"18"` com o número `18` usando `<`. A comparação falha antes de entrar no `if` ou no `else`.

Para comparar idades, converta o texto em número:

```python
idade = int("18")
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
```

Agora a saída é `Você é maior de idade.`. O critério `>= 18` inclui quem tem exatamente 18 anos. Lembre-se: em Python, `if` e `else` terminam com `:`; as linhas dentro de cada bloco precisam de recuo (indentação).

## 4. Convertendo texto recebido de uma pessoa

Em [`manipulando_int_str.py`](manipulando_int_str.py), primeiro convertemos o texto `"2000"` com `int("2000")`. Depois perguntamos o ano de nascimento com `input()`. Mesmo se a pessoa digitar `2000`, `input()` devolve `str`:

```python
ano_digitado = input("Digite seu ano de nascimento: ")
print(type(ano_digitado))  # <class 'str'>
ano_convertido = int(ano_digitado)
print(type(ano_convertido))  # <class 'int'>
```

O programa completo usa `try` e `except ValueError`: **tenta** converter o que foi digitado e, se receber algo como `abc`, mostra uma orientação. `int()` não transforma qualquer texto em número. Ele aceita, por exemplo, `"2000"`, mas não `"dois mil"` ou `"20,5"`.

## Confira o que aprendeu

1. Qual é a saída de `print("10" + "5")`? **Resposta:** `105`, pois junta dois textos.
2. Qual é a saída de `print(10 + 5)`? **Resposta:** `15`, pois soma dois inteiros.
3. Qual é o tipo de `input("Idade: ")`, se a pessoa digitar `18`? **Resposta:** `str`.
4. O que acontece com `int("abc")`? **Resposta:** ocorre `ValueError`, porque `abc` não representa um inteiro.

Experimente mudar os valores nos três arquivos e prever a saída antes de executar. Depois continue com a [teoria de aritmética](../../2-exercicios-aritmeticos/teoria.md).
