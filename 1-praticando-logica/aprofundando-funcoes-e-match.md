# Aprofundando funções com `match`

No [exemplo de funções](praticando_functions.py), `somar(a, b)` recebe dois valores e executa uma tarefa. No [`app.py`](../app.py), funções como `show_option()` organizam as ações de um menu. Vamos usar essa ideia para criar um menu de estudos: cada opção chama uma função, e `match` escolhe qual função executar.

> **Requisito:** `match` está disponível a partir do **Python 3.10**. Confira sua versão com `python3 --version` (ou `python --version`/`py --version` no Windows). Se ela for anterior, siga o [tutorial de instalação](../instalando-python.md) para obter uma versão atual.

## Recapitulando: o que uma função faz?

Uma **função** é um bloco de código com nome. `def` define a função; chamar seu nome com parênteses executa o bloco:

```python
def mostrar_boas_vindas():
    print("Bem-vindo aos exercícios de lógica!")

mostrar_boas_vindas()
```

Nesse exemplo, a saída é `Bem-vindo aos exercícios de lógica!`. Definir uma função não a executa automaticamente: a última linha é a **chamada**. O recuo de quatro espaços indica quais instruções pertencem à função.

Uma função também pode receber um **parâmetro** (valor usado dentro dela) e **retornar** um resultado com `return`:

```python
def criar_mensagem(tema):
    return f"Vamos estudar {tema}!"

mensagem = criar_mensagem("variáveis")
print(mensagem)  # Vamos estudar variáveis!
```

`tema` é o parâmetro. `"variáveis"` é o **argumento**, o valor passado na chamada. `return` entrega o resultado para quem chamou; `print()` mostra algo na tela. Por isso, podemos guardar o resultado em `mensagem` e mostrá-lo depois.

## Escolhendo uma função com `if`, `elif` e `else`

Suponha que o menu ofereça três assuntos. Uma cadeia de condições pode decidir o que mostrar:

```python
def estudar_variaveis():
    print("Estude como guardar valores em variáveis.")

def estudar_aritmetica():
    print("Pratique contas com números.")

def estudar_condicionais():
    print("Pratique decisões com if e else.")

opcao = input("Escolha: Variáveis, Aritmética ou Condicionais: ").strip().lower()

if opcao == "variáveis":
    estudar_variaveis()
elif opcao == "aritmética":
    estudar_aritmetica()
elif opcao == "condicionais":
    estudar_condicionais()
else:
    print("Opção inválida.")
```

`input()` recebe texto; `.strip()` remove espaços no início e no fim, e `.lower()` transforma letras maiúsculas em minúsculas. Assim, `" Variáveis "` também corresponde a `"variáveis"`. Os acentos continuam importantes: `"variaveis"` ainda é um texto diferente de `"variáveis"`.

## A mesma escolha com `match`

Quando queremos comparar **um valor** com várias opções específicas, podemos escrever:

```python
match opcao:
    case "variáveis":
        estudar_variaveis()
    case "aritmética":
        estudar_aritmetica()
    case "condicionais":
        estudar_condicionais()
    case _:
        print("Opção inválida.")
```

Leia como “compare `opcao` com cada `case`”. Python executa o **primeiro** caso que combina. `case _:` aceita qualquer valor restante, como o `else` do exemplo anterior. Coloque-o por último. Aqui, `match` é uma **instrução de decisão**, não uma função; as funções são as ações chamadas dentro dos casos.

O `case` compara o texto recebido. Por exemplo, `"variáveis"` combina com `case "variáveis":`, mas `"Variáveis"` só combinará depois de `.lower()`. Em exemplos simples com valores fixos, `match` e `if`/`elif` podem resolver o mesmo problema. Para regras como `idade >= 18`, `if` costuma ser a escolha mais direta, pois a regra é uma comparação, não uma opção fixa do menu.

## Exemplo completo para executar

O arquivo [`praticando_match.py`](praticando_match.py) reúne as funções e o menu. Execute a partir da raiz do projeto:

```bash
python3 1-praticando-logica/praticando_match.py
```

No Windows, use `python` ou `py` no lugar de `python3`, conforme sua instalação. Experimente digitar `Variáveis`, `Aritmética`, `Condicionais`, `Sair` e uma opção desconhecida. O programa faz uma escolha por execução; execute novamente para testar outra resposta.

No arquivo, `escolher_acao(opcao)` recebe o texto digitado como argumento. Cada `case` chama uma função. `mostrar_menu()` só apresenta as opções; `main()` reúne os passos na ordem: mostrar o menu, ler a resposta e escolher a ação. Essa separação ajuda a entender qual parte faz cada trabalho.

## Preveja antes de executar

1. Se a pessoa digitar ` ARITMÉTICA `, qual função será chamada? **Resposta:** `estudar_aritmetica()`, pois `.strip().lower()` produz `"aritmética"`.
2. Se digitar `Remover`, o programa encerrará? **Resposta:** não. Essa opção não existe no menu; o `case _:` mostra `Opção inválida.`
3. Se removermos `case _:` e a entrada for `Remover`, o que acontecerá? **Resposta:** nenhum bloco `case` será executado; a função terminará sem mostrar uma mensagem para essa opção.
4. Qual é a diferença entre `estudar_variaveis` e `estudar_variaveis()`? **Resposta:** o primeiro é o nome da função; os parênteses fazem a chamada que executa seu código.

Para aprofundar, consulte a documentação oficial sobre [funções e `match`](https://docs.python.org/3/tutorial/controlflow.html#match-statements) e a [introdução da instrução no Python 3.10](https://docs.python.org/3.10/whatsnew/3.10.html#pep-634-structural-pattern-matching). Depois pratique as condições em [teoria de condicionais](../3-exercicios-condicionais/teoria.md).
