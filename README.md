# Exercícios de Lógica com Python

Este repositório reúne explicações e desafios progressivos para aprender lógica de programação com Python. Cada assunto tem uma leitura teórica e uma lista de atividades para praticar.

**Está começando do zero?** Siga o [tutorial de instalação do Python](instalando-python.md) para preparar Windows, macOS ou Ubuntu, aprender os termos básicos e testar seu primeiro programa antes dos exercícios.

## Como estudar

1. Leia a **teoria** do assunto e execute os exemplos, alterando os valores para observar o resultado.
2. Resolva os **desafios** na ordem, dos mais simples aos mais elaborados.
3. Em cada atividade, identifique **entrada** (dados necessários), **processamento** (cálculo ou decisão) e **saída** (resultado apresentado).
4. Confira a saída com os exemplos do enunciado e teste outros valores.

As listas trazem os problemas e resultados esperados; a implementação fica como prática para quem está estudando.

## Conteúdo

| Tema | Explicação | Atividades |
| --- | --- | --- |
| Primeiros passos: `print()` e variáveis | [Teoria e exemplos](1-praticando-logica/teoria.md) | [Praticando lógica](1-praticando-logica/desafios.md) |
| Tipos `str` e `int`, entrada e conversão | [Guia com perguntas e respostas](1-praticando-logica/1.3-praticando-variaveis-str-int/README.md) | [Exemplos para executar](1-praticando-logica/1.3-praticando-variaveis-str-int/manipulando_int_str.py) |
| Funções e escolhas com `match` (Python 3.10+) | [Aprofundamento com explicações](1-praticando-logica/aprofundando-funcoes-e-match.md) | [Menu para praticar](1-praticando-logica/praticando_match.py) |
| Operadores aritméticos | [Teoria de aritmética](2-exercicios-aritmeticos/teoria.md) | [Desafios de aritmética](2-exercicios-aritmeticos/desafios.md) |
| Condições e operadores lógicos | [Teoria de condicionais](3-exercicios-condicionais/teoria.md) | [Desafios de condicionais](3-exercicios-condicionais/desafios.md) |

```text
.
├── README.md
├── app.py                         # Exemplo inicial de variáveis e saída
├── 1-praticando-logica/
│   ├── teoria.md                  # Explicação dos primeiros conceitos
│   ├── desafios.md                # Primeira lista de prática
│   ├── praticando_print.py        # Exemplos de impressão no terminal
│   ├── praticando_variaveis.py    # Exemplos de variáveis
│   ├── praticando_functions.py    # Primeiro exemplo de função
│   ├── aprofundando-funcoes-e-match.md # Funções e escolhas com match
│   ├── praticando_match.py        # Menu com funções e match
│   ├── 1.3-praticando-variaveis-str-int/
│   │   ├── README.md              # Guia sobre str, int e conversão
│   │   ├── int.py                 # Exemplos com números inteiros
│   │   ├── str.py                 # Exemplos com textos
│   │   └── manipulando_int_str.py # Conversão e entrada do usuário
│   ├── praticando_tupla.py        # Exemplo adicional
│   └── nomes.py                   # Outro exemplo com nomes
├── 2-exercicios-aritmeticos/
│   ├── teoria.md                  # Conceitos e exemplos
│   ├── desafios.md                # Lista progressiva de exercícios
│   ├── desafio-aritmetico1.py     # Arquivos para praticar
│   └── desafio-aritmetico2.py
└── 3-exercicios-condicionais/
    ├── teoria.md
    ├── desafios.md
    ├── desafio-condicional.py
    └── desafio-condicional2.py
```

Os arquivos de desafios em Python são espaços para escrever soluções. Crie novos arquivos conforme avançar na lista.

## Como executar

Instale o Python 3 seguindo o [tutorial passo a passo](instalando-python.md) e clone o projeto:

```bash
git clone https://github.com/pauloqueirozz01/exercicio-logica-com-python.git
cd exercicio-logica-com-python
```

Execute o exemplo inicial ou um exercício a partir da raiz do repositório:

```bash
python3 app.py
python3 1-praticando-logica/praticando_print.py
python3 2-exercicios-aritmeticos/desafio-aritmetico1.py
python3 3-exercicios-condicionais/desafio-condicional.py
```

No Windows, se `python3` não estiver disponível, experimente `python` ou `py`. Os arquivos de desafios começam vazios e só mostrarão resultados depois que você escrever o código.

## Contribuições

Para sugerir um exercício ou melhorar uma explicação, abra uma *issue* ou envie um *pull request*. Ao adicionar um desafio, inclua entrada, processamento, saída e pelo menos um exemplo para conferir a resposta.
