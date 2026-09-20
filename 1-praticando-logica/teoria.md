# Teoria: primeiros passos em lógica com Python

## Por que começar por esta pasta?

Lógica de programação é organizar passos para chegar a um resultado. Antes de resolver problemas com contas ou condições, precisamos entender como um programa recebe dados, guarda informações e mostra uma resposta. Por isso, `1-praticando-logica/` é a primeira etapa do repositório: aqui podemos experimentar cada linha com calma, observar o terminal e corrigir nossas próprias tentativas.

Os arquivos `praticando_*.py` são pequenos espaços de estudo. Leia os comentários, execute o código, mude uma coisa por vez e execute novamente. A intenção é compreender **por que** cada linha existe, além de reconhecer o resultado que ela produz. Depois dessa prática, siga para [os quatro desafios](desafios.md) e, então, para os exercícios de aritmética e condicionais.

## Como executar e investigar

Abra o terminal na raiz do repositório e execute:

```bash
python3 1-praticando-logica/praticando_print.py
python3 1-praticando-logica/praticando_variaveis.py
```

O segundo programa fará perguntas; digite uma resposta e pressione Enter para cada uma. Em cada exemplo, tente responder: **qual dado entra, o que o programa faz com ele e o que aparece na tela?** Antes de executar uma mudança, anote sua previsão. Se surgir um erro, leia a linha indicada na mensagem e compare-a com o exemplo.

## Etapa 1: mostrar uma mensagem com `print()`

Veja a ideia central de `praticando_print.py`:

```python
print("Olá, seja bem-vindo ao nosso programa!")
```

- `print` é uma função que mostra algo no terminal.
- Os parênteses `()` contêm o valor que será mostrado.
- O texto entre aspas é uma **string**: uma sequência de caracteres.
- Ao chegar nessa linha, Python mostra a frase e passa para a próxima. `print()` já termina a saída com uma quebra de linha.

No arquivo há também `\n` dentro de algumas strings. Esse símbolo acrescenta outra quebra de linha; junto com a quebra que `print()` já faz, ele deixa uma linha em branco. Experimente remover `\n` e compare a saída. O `;` no fim de algumas linhas do arquivo é opcional em Python; uma linha por comando é suficiente.

Linhas que começam com `#` são comentários para quem lê o código. Python não as executa. Elas ajudam a registrar a intenção de um passo, como “mostrar uma saudação”.

Para mostrar uma letra em cada linha, você pode usar vários `print()` ou escrever `\n` entre as letras dentro de uma única string. Teste as duas formas antes de fazer o desafio da palavra `UNINASSAU`.

## Etapa 2: guardar valores em variáveis

Quando uma informação pode mudar, guarde-a em uma variável:

```python
nome = "Ana"
idade = 20
print(f"Meu nome é {nome} e tenho {idade} anos")
```

Leia o programa linha por linha:

1. `nome = "Ana"` guarda a string `Ana` sob o nome `nome`. O sinal `=` faz uma **atribuição**.
2. `idade = 20` guarda o número inteiro `20` sob o nome `idade`. Sem aspas, é um número; `"20"` seria texto.
3. A letra `f` antes das aspas cria uma **f-string**. Dentro dela, `{nome}` e `{idade}` são substituídos pelos valores das variáveis.
4. `print(...)` mostra `Meu nome é Ana e tenho 20 anos`.

Troque `Ana` e `20` por outros valores. A frase muda sem que você precise reescrevê-la. Isso será útil em apresentações, recibos e mensagens que usam dados diferentes para cada pessoa.

## Etapa 3: receber texto e combinar informações

`praticando_variaveis.py` pede nome, sobrenome, idade e ano de nascimento. Este é o trecho que forma o nome completo:

```python
name = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
nome_completo = name + " " + sobrenome
print(f"Seu nome completo é: {nome_completo}")
```

1. `input("Digite seu nome: ")` mostra uma pergunta e espera que alguém digite uma resposta. O texto digitado é guardado em `name`.
2. A segunda linha faz o mesmo e guarda o sobrenome em `sobrenome`.
3. `+` junta as três strings: nome, um espaço (`" "`) e sobrenome. O resultado fica em `nome_completo`.
4. A última linha usa o valor já montado para apresentar a pessoa.

`input()` sempre devolve texto. Assim, a idade e o ano digitados no arquivo servem para compor uma mensagem, mas ainda não para fazer contas. Nos exercícios de aritmética você aprenderá a converter textos para números. No desafio 2 desta pasta, os valores são definidos diretamente em variáveis; você pode praticar `input()` depois, como uma experiência adicional.

O restante do arquivo repete esse caminho com novos dados:

```python
age = input("Digite sua idade: ")
print(f"Sua idade é: {age}")
year_of_birth = input("Digite o ano de nascimento: ")
print(f"Ano de nascimento: {year_of_birth}")
print(f"Olá, {nome_completo}, você tem {age} anos e nasceu em {year_of_birth}. Que legal!")
```

Cada `input()` guarda uma nova resposta; os dois `print()` intermediários confirmam o que foi digitado. O último `print()` reúne três valores já guardados. Repare que a ordem importa: se tentar usar `year_of_birth` antes da linha que o cria, Python não saberá qual valor mostrar.

## Etapa 4: transformar um valor antes de mostrá-lo

Às vezes existe um pequeno processamento entre guardar um dado e imprimi-lo. O desafio de pi usa `round()`:

```python
pi = 3.14159
pi_arredondado = round(pi, 2)
print(f"O valor arredondado de pi é: {pi_arredondado}")
```

1. `pi` guarda um número decimal. O ponto separa a parte inteira da parte decimal em Python.
2. `round(pi, 2)` arredonda o valor de `pi` para duas casas decimais e o resultado é guardado em outra variável. `pi` continua com o valor original.
3. `print()` mostra o valor calculado dentro da frase: `O valor arredondado de pi é: 3.14`.

Aqui aparecem três passos que voltam em todo o repositório: **entrada** (o valor de `pi`), **processamento** (o arredondamento) e **saída** (a frase no terminal).

## Como saber se pode avançar

Você está pronto para [a lista desta pasta](desafios.md) quando consegue prever a saída de um `print()`, explicar a diferença entre texto e número, guardar um valor em uma variável e usá-lo em outra linha. Resolva os quatro desafios na ordem. Depois, altere os valores e confira se ainda entende cada resultado; esse hábito será a base para os exercícios seguintes.
