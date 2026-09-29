# Desafios: classes e métodos especiais

[Voltar à teoria](teoria.md) · [Voltar ao início](../README.md)

Resolva os exercícios na ordem. Crie um arquivo `.py` para cada desafio ou continue os arquivos existentes em `classes/`. Use quatro espaços para cada nível de indentação.

## 1. Inicialização de um restaurante

Crie a classe `Restaurante` com `__init__`. Receba `nome` e `categoria` e faça o atributo `ativo` começar como `False`.

Crie os objetos abaixo e imprima separadamente seus atributos:

```python
restaurante_praca = Restaurante("Praça", "Gourmet")
restaurante_pizza = Restaurante("Pizza Express", "Italiana")
```

## 2. Entendendo `self`

Adicione o método comum `ativar(self)`, que altera para `True` somente o atributo `ativo` da instância que chamou o método.

Ative `restaurante_pizza` e confirme que `restaurante_praca.ativo` continua sendo `False`. Explique em um comentário o que `self` representa nessa chamada.

## 3. Representação com `__str__`

Implemente `__str__` para retornar o nome e a categoria separados por ` | `.

Saída esperada:

```text
Praça | Gourmet
Pizza Express | Italiana
```

Teste com `print(objeto)`, `str(objeto)` e uma f-string.

## 4. Estado na representação textual

Altere `__str__` para também mostrar `ativo` ou `inativo`, em vez de exibir diretamente `True` ou `False`.

```text
Praça | Gourmet | inativo
Pizza Express | Italiana | ativo
```

## 5. Inspeção

Use `vars()` em uma instância e identifique as chaves e os valores retornados. Depois use `dir()` e encontre na saída:

- `__init__`;
- `__str__`;
- `ativar`;
- os atributos da instância.

Registre em comentários a diferença entre os resultados de `vars()` e `dir()`.

## 6. Uma classe `Cliente`

Crie uma classe `Cliente` que receba `nome`, `email`, `telefone` e `ativo` no `__init__`. O parâmetro `ativo` deve ter `True` como valor padrão. Implemente `__str__` para retornar `nome <email>`.

Crie três clientes e mostre todos com `print()`.

## 7. Tamanho de um cardápio

Crie uma classe `Cardapio` que receba uma lista de pratos. Implemente `__len__` para permitir esta operação:

```python
cardapio = Cardapio(["Feijoada", "Moqueca", "Cuscuz"])
print(len(cardapio))  # 3
```

Adicione um método comum `adicionar_prato(self, prato)` e confirme que o tamanho muda para `4`.

## Desafio final

Crie uma classe `Pedido` com:

- número do pedido;
- nome do cliente;
- lista de itens;
- `__init__` para inicializar esses dados;
- `__str__` para gerar um resumo legível;
- `__len__` para retornar a quantidade de itens;
- `adicionar_item()` para incluir um item.

Teste um pedido vazio e outro com pelo menos três itens. Antes de executar, preveja a saída de `print(pedido)` e `len(pedido)`.
