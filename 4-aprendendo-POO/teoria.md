# Teoria: métodos especiais em Python POO

[Voltar ao início](../README.md) · [Ir para os desafios](desafios.md) · [Executar o exemplo](exemplo_metodos_especiais.py)

## O que são métodos especiais?

Métodos especiais são métodos que o próprio Python reconhece e chama em determinadas operações. Seus nomes começam e terminam com dois sublinhados, como `__init__` e `__str__`. Por isso, eles também são conhecidos como métodos *dunder* (*double underscore*).

Não chamamos esses métodos em todas as situações de forma direta. Ao criar `Restaurante(...)`, por exemplo, Python executa `__init__`. Ao usar `print(restaurante)`, Python procura `__str__` para saber qual texto deve mostrar.

```python
class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

    def __str__(self):
        return f"{self.nome} | {self.categoria}"


restaurante_praca = Restaurante("Praça", "Gourmet")
print(restaurante_praca)  # Praça | Gourmet
```

Os métodos estão indentados com quatro espaços porque pertencem à classe. As linhas dentro de cada método recebem mais quatro espaços.

## `__init__`: inicializar um objeto

`__init__` é executado logo depois que uma instância é criada. No estudo introdutório, é comum chamá-lo de **construtor**, embora tecnicamente `__new__` crie o objeto e `__init__` inicialize o objeto já criado.

Use `__init__` quando cada novo objeto precisar começar com atributos definidos ou com um estado inicial válido.

```python
class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False


restaurante_praca = Restaurante("Praça", "Gourmet")
restaurante_pizza = Restaurante("Pizza Express", "Italiana")
```

Nessa classe:

- `nome` e `categoria` são valores recebidos na criação;
- `self.nome` e `self.categoria` tornam esses valores atributos da instância;
- `ativo` começa como `False` para todos os restaurantes, mas cada instância possui seu próprio valor.

Assim, esquecer o nome ou a categoria gera um erro imediatamente, em vez de produzir um restaurante incompleto.

## O que `self` representa?

`self` é a referência à instância que está usando o método naquele momento:

```python
restaurante_praca.ativar()  # self é restaurante_praca
restaurante_pizza.ativar()  # self é restaurante_pizza
```

O primeiro parâmetro poderia ter outro nome e o programa ainda funcionaria, mas `self` é a convenção do Python. Respeitar essa convenção deixa o código compreensível para outras pessoas.

Um método comum também usa `self` para ler ou alterar o próprio objeto:

```python
def ativar(self):
    self.ativo = True
```

`ativar` não é um método especial: foi criado para representar uma ação do domínio do programa. Já `__init__` e `__str__` têm significados definidos pelo Python.

## `__str__`: representação textual amigável

Sem `__str__`, imprimir uma instância normalmente mostra o tipo do objeto e uma identificação interna semelhante a esta:

```text
<__main__.Restaurante object at 0x102A4F310>
```

Essa informação é pouco útil para quem utiliza o programa. `__str__` define uma representação legível:

```python
def __str__(self):
    return f"{self.nome} | {self.categoria}"
```

Use `__str__` quando o objeto puder aparecer em `print()`, em uma f-string ou convertido por `str()`:

```python
print(restaurante_praca)
mensagem = f"Selecionado: {restaurante_praca}"
texto = str(restaurante_praca)
```

O método precisa **retornar uma string**. Fazer apenas `print()` dentro de `__str__` está errado, pois o método retornaria `None`.

## Inspecionar o objeto com `vars()` e `dir()`

Essas funções ajudam a investigar objetos, mas resolvem problemas diferentes:

```python
print(vars(restaurante_praca))
print(dir(restaurante_praca))
```

- `vars(objeto)` mostra, em um dicionário, os atributos armazenados naquela instância. Exemplo: `{'nome': 'Praça', 'categoria': 'Gourmet', 'ativo': False}`.
- `dir(objeto)` mostra os nomes disponíveis no objeto: atributos, métodos criados na classe e métodos herdados, inclusive muitos métodos especiais.

O nome correto da função é `dir()`, no singular. Use essas ferramentas para estudo e depuração; para a saída normal do programa, prefira propriedades, métodos próprios ou `__str__`.

## Outros métodos especiais comuns

Você não precisa implementar todos. Adicione um método especial somente quando a operação fizer sentido para a classe.

| Método | Python o utiliza em | Exemplo de uso |
| --- | --- | --- |
| `__repr__` | `repr(objeto)` e representações voltadas à depuração | mostrar uma descrição precisa do objeto |
| `__len__` | `len(objeto)` | quantidade de itens de um carrinho |
| `__eq__` | `objeto_a == objeto_b` | comparar objetos por seus dados |
| `__contains__` | `item in objeto` | verificar se um item pertence a uma coleção própria |
| `__iter__` | `for item in objeto` | permitir a iteração sobre um objeto |

Exemplo com `__len__`:

```python
class Cardapio:
    def __init__(self, pratos):
        self.pratos = pratos

    def __len__(self):
        return len(self.pratos)


cardapio = Cardapio(["Feijoada", "Moqueca", "Cuscuz"])
print(len(cardapio))  # 3
```

## Exemplo completo

```python
class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

    def __str__(self):
        estado = "ativo" if self.ativo else "inativo"
        return f"{self.nome} | {self.categoria} | {estado}"

    def ativar(self):
        self.ativo = True


restaurante = Restaurante("Praça", "Gourmet")
print(restaurante)  # Praça | Gourmet | inativo

restaurante.ativar()
print(restaurante)  # Praça | Gourmet | ativo
```

Observe a divisão de responsabilidades: `__init__` estabelece o estado inicial, `ativar` muda esse estado e `__str__` informa como o objeto será exibido como texto.

## Quando usar cada recurso

- Use `__init__` para garantir que uma nova instância comece válida e completa.
- Use `__str__` para oferecer uma descrição curta e amigável do objeto.
- Use um método comum, como `ativar()`, para representar uma ação do objeto.
- Use `vars()` para ver os atributos atuais durante o estudo ou a depuração.
- Use `dir()` para descobrir os nomes e métodos disponíveis.
- Não crie métodos com nomes `__qualquer_coisa__`: os nomes especiais pertencem ao protocolo da linguagem.

Agora execute [o exemplo completo](exemplo_metodos_especiais.py), altere sua saída e avance para os [desafios](desafios.md).
