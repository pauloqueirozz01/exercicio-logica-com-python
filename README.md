# Exercícios de Lógica com Python

Este repositório reúne explicações e desafios progressivos para aprender lógica de programação com Python. Cada assunto tem uma leitura teórica e uma lista de atividades para praticar.

## Como estudar

1. Leia a **teoria** do assunto e execute os exemplos, alterando os valores para observar o resultado.
2. Resolva os **desafios** na ordem, dos mais simples aos mais elaborados.
3. Em cada atividade, identifique **entrada** (dados necessários), **processamento** (cálculo ou decisão) e **saída** (resultado apresentado).
4. Confira a saída com os exemplos do enunciado e teste outros valores.

As listas trazem os problemas e resultados esperados; a implementação fica como prática para quem está estudando.

## Conteúdo

| Tema | Explicação | Atividades |
| --- | --- | --- |
| Operadores aritméticos | [Teoria de aritmética](exercicios-aritmeticos/teoria.md) | [Desafios de aritmética](exercicios-aritmeticos/desafios.md) |
| Condições e operadores lógicos | [Teoria de condicionais](exercicios-condicionais/teoria.md) | [Desafios de condicionais](exercicios-condicionais/desafios.md) |

```text
.
├── README.md
├── app.py                         # Exemplo inicial de variáveis e saída
├── exercicios-aritmeticos/
│   ├── teoria.md                  # Conceitos e exemplos
│   ├── desafios.md                # Lista progressiva de exercícios
│   ├── desafio-aritmetico1.py     # Arquivos para praticar
│   └── desafio-aritmetico2.py
└── exercicios-condicionais/
    ├── teoria.md
    ├── desafios.md
    ├── desafio-condicional.py
    └── desafio-condicional2.py
```

Os arquivos de desafios em Python são espaços para escrever soluções. Crie novos arquivos conforme avançar na lista.

## Como executar

Instale o [Python 3](https://www.python.org/downloads/) e clone o projeto:

```bash
git clone https://github.com/pauloqueirozz01/exercicio-logica-com-python.git
cd exercicio-logica-com-python
```

Execute o exemplo inicial ou um exercício a partir da raiz do repositório:

```bash
python3 app.py
python3 exercicios-aritmeticos/desafio-aritmetico1.py
python3 exercicios-condicionais/desafio-condicional.py
```

No Windows, se `python3` não estiver disponível, experimente `python` ou `py`. Os arquivos de desafios começam vazios e só mostrarão resultados depois que você escrever o código.

## Contribuições

Para sugerir um exercício ou melhorar uma explicação, abra uma *issue* ou envie um *pull request*. Ao adicionar um desafio, inclua entrada, processamento, saída e pelo menos um exemplo para conferir a resposta.
