# Desafios: variáveis, funções e coleções

[Voltar à teoria](teoria.md) · [Voltar ao início](../README.md)

Crie um arquivo `.py` para cada exercício. Antes de executar, anote a saída esperada. Nos desafios com funções, teste pelo menos dois conjuntos diferentes de dados.

## 1. Dados de uma pessoa

Crie as variáveis `nome`, `idade`, `email` e `usuario_ativo` com tipos adequados. Mostre uma frase com todos os dados usando uma f-string.

## 2. Entrada e conversão

Leia o nome e a idade pelo terminal. Mostre quantos anos a pessoa terá no próximo aniversário. Lembre-se de que `input()` retorna texto.

## 3. Função de apresentação

Crie `apresentar_usuario(nome, email)`. A função deve **retornar** uma string no formato `Nome: Ana | E-mail: ana@email.com`. Mostre o resultado fora da função.

## 4. Primeira lista

Crie uma lista com cinco números. Mostre:

- a lista inteira;
- o primeiro item;
- o último item;
- a quantidade de itens com `len()`.

## 5. Listar todos os números

Implemente `listar_numeros(numeros)`, que usa `for` para imprimir cada número em uma linha. Teste com números positivos, negativos e zero.

## 6. Adicionar e remover

Comece com `linguagens = ["Python", "Dart"]`. Depois:

1. adicione `Java` ao fim;
2. adicione `C#` na posição `1`;
3. remova `Dart` pelo valor;
4. remova e guarde o último item;
5. mostre a lista e o item removido.

## 7. Lista de e-mails

Crie `listar_emails(emails)` e mostre cada e-mail com o prefixo `Contato:`. Teste com uma lista de pelo menos três endereços.

## 8. E-mails sem repetição

Receba uma lista que contém e-mails duplicados e crie um `set` para manter somente valores únicos. Mostre quantos e-mails existiam antes e quantos permaneceram.

## 9. Cadastro com dicionário

Crie um dicionário com as chaves `nome` e `email`. Adicione a chave `ativo`, atualize o nome e mostre cada chave e valor usando:

```python
for chave, valor in usuario.items():
    print(chave, valor)
```

## 10. Lista de usuários

Crie uma lista com três dicionários, cada um representando uma pessoa com nome e e-mail. Implemente `listar_usuarios(usuarios)` para produzir esta saída:

```text
Ana | ana@email.com
Bruno | bruno@email.com
Carla | carla@email.com
```

## 11. Capturar um novo usuário

Implemente uma função `capturar_usuario()` que pede nome e e-mail com `input()` e retorna um dicionário. Adicione o resultado à lista com `append()`.

Não é necessário validar o formato do e-mail neste exercício.

## 12. Remover por e-mail

Implemente `remover_usuario_por_email(usuarios, email)`. Retorne `True` ao remover e `False` quando não encontrar. Teste os dois resultados e confirme a lista final.

## 13. Buscar sem alterar

Crie `buscar_usuario_por_email(usuarios, email)`. A função deve retornar o dicionário encontrado ou `None`. Ela não deve remover nem modificar dados.

## Desafio final: pequeno cadastro

Monte um programa com um menu repetido por `while`:

```text
1 - Cadastrar usuário
2 - Listar usuários
3 - Remover usuário pelo e-mail
4 - Sair
```

Use uma lista de dicionários e divida cada operação em uma função. Ao cadastrar, não permita um e-mail já existente. Ao remover, informe se o cadastro foi encontrado. O programa termina somente quando a opção `4` for escolhida.
