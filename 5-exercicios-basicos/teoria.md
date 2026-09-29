# Teoria: revisão de variáveis, funções e coleções

[Voltar ao início](../README.md) · [Ir para os desafios](desafios.md) · [Executar os exemplos](exemplos_listas.py)

Esta etapa reúne os fundamentos necessários para guardar um valor, organizar vários valores e criar funções que manipulam esses dados.

## 1. Declarar variáveis

Em Python, uma variável nasce quando recebe um valor. Não é necessário informar o tipo antes do nome:

```python
nome = "Ana"             # str: texto
idade = 20               # int: número inteiro
altura = 1.68            # float: número decimal
usuario_ativo = True     # bool: verdadeiro ou falso
```

Use nomes descritivos em `snake_case`. Python possui tipagem dinâmica, mas cada valor continua tendo um tipo, que pode ser consultado com `type(nome)`.

## 2. Receber e converter dados

`input()` sempre retorna uma string. Converta o valor quando precisar fazer operações numéricas:

```python
nome = input("Nome: ").strip()
idade = int(input("Idade: "))
print(f"{nome} terá {idade + 1} anos no próximo aniversário.")
```

`strip()` remove espaços extras do início e do fim. `int()` converte um texto numérico para inteiro e `float()` converte para decimal.

## 3. Criar funções

Uma função dá nome a uma tarefa e evita repetição:

```python
def criar_saudacao(nome):
    return f"Olá, {nome}!"


mensagem = criar_saudacao("Ana")
print(mensagem)
```

Os dados entre parênteses na definição são parâmetros. `return` entrega o resultado para quem chamou a função. Prefira retornar o dado quando ele ainda poderá ser utilizado; use `print()` para apresentá-lo.

## 4. `list`: uma coleção ordenada e alterável

No aprendizado inicial, a coleção chamada informalmente de “array” normalmente é a `list` do Python. Ela mantém a ordem, aceita valores repetidos e pode crescer ou diminuir:

```python
numeros = [10, 20, 30]
emails = ["ana@email.com", "bia@email.com"]

print(numeros[0])   # 10
print(emails[-1])   # bia@email.com
```

Os índices começam em `0`. O índice `-1` acessa o último item.

### Adicionar valores

```python
emails.append("caio@email.com")                 # adiciona um item no fim
emails.insert(0, "admin@email.com")             # adiciona em uma posição
emails.extend(["dani@email.com", "eli@email.com"])  # adiciona vários
```

### Remover valores

```python
emails.remove("admin@email.com")  # remove a primeira ocorrência desse valor
email_removido = emails.pop()      # remove e retorna o último
primeiro = emails.pop(0)           # remove e retorna o item do índice 0
emails.clear()                      # remove todos os itens
```

`remove()` gera `ValueError` se o valor não existir. Quando houver dúvida, verifique antes:

```python
if "ana@email.com" in emails:
    emails.remove("ana@email.com")
```

## 5. Percorrer uma lista

Use `for` quando quiser executar uma ação para cada item:

```python
def listar_numeros(numeros):
    for numero in numeros:
        print(numero)


listar_numeros([4, 8, 15, 16, 23, 42])
```

Uma versão realista para os e-mails capturados pelo programa:

```python
def listar_emails(emails):
    for email in emails:
        print(email)


emails_cadastrados = ["ana@email.com", "bia@email.com"]
listar_emails(emails_cadastrados)
```

As funções não precisam conhecer uma variável global: elas recebem a lista que devem percorrer.

## 6. Guardar nome e e-mail juntos

Duas listas separadas podem perder a correspondência entre seus índices. Para um cadastro, prefira uma lista de dicionários:

```python
usuarios = []


def capturar_usuario():
    nome = input("Nome: ").strip()
    email = input("E-mail: ").strip().lower()
    return {"nome": nome, "email": email}


def adicionar_usuario(usuarios, nome, email):
    usuario = {"nome": nome, "email": email}
    usuarios.append(usuario)


def listar_usuarios(usuarios):
    for usuario in usuarios:
        print(f"{usuario['nome']} | {usuario['email']}")


adicionar_usuario(usuarios, "Ana", "ana@email.com")
adicionar_usuario(usuarios, "Bruno", "bruno@email.com")
listar_usuarios(usuarios)

# Para capturar outro cadastro pelo terminal:
# novo_usuario = capturar_usuario()
# usuarios.append(novo_usuario)
```

Cada dicionário mantém os dados de uma pessoa juntos. A lista organiza todos os cadastros.

Para remover pelo e-mail, procure o cadastro e remova o dicionário correspondente:

```python
def remover_usuario_por_email(usuarios, email):
    for usuario in usuarios:
        if usuario["email"] == email:
            usuarios.remove(usuario)
            return True
    return False
```

O retorno informa se alguém foi removido.

## 7. `list`, `tuple`, `set` e `dict`

| Coleção | Característica | Exemplo | Uso comum |
| --- | --- | --- | --- |
| `list` | ordenada e alterável; aceita repetição | `["a", "b"]` | sequência de cadastros |
| `tuple` | ordenada e imutável | `(10, 20)` | coordenada que não deve mudar |
| `set` | valores únicos, sem acesso por índice | `{"Python", "Dart"}` | remover duplicados, testar associação |
| `dict` | pares de chave e valor | `{"nome": "Ana"}` | representar dados nomeados |

Exemplos:

```python
linguagens = {"Python", "Dart"}
linguagens.add("C#")
linguagens.discard("Dart")  # não gera erro se o valor não existir

usuario = {"nome": "Ana", "email": "ana@email.com"}
usuario["idade"] = 20
usuario.pop("idade")
```

## 8. Equivalências entre Dart e Python

| Dart | Python | Observação |
| --- | --- | --- |
| `List` | `list` | sequência ordenada e alterável |
| `lista.add(valor)` | `lista.append(valor)` | adiciona no fim |
| `lista.addAll(valores)` | `lista.extend(valores)` | adiciona vários valores |
| `lista.remove(valor)` | `lista.remove(valor)` | remove a primeira ocorrência |
| `lista.removeAt(indice)` | `lista.pop(indice)` | remove pelo índice e retorna o item |
| `Set` | `set` | armazena valores únicos |
| `conjunto.add(valor)` | `conjunto.add(valor)` | adiciona um valor único |
| `conjunto.remove(valor)` | `conjunto.remove(valor)` | gera erro se não existir |
| `Map` | `dict` | armazena chave e valor |
| `mapa[chave] = valor` | `dicionario[chave] = valor` | inclui ou atualiza uma chave |
| `mapa.remove(chave)` | `dicionario.pop(chave)` | remove pela chave |

Python também possui o módulo `array` para sequências de um único tipo e bibliotecas como NumPy para computação numérica. Para cadastros e lógica básica, `list` é a escolha usual.

## Cuidados frequentes

- Não use `list`, `set` ou `dict` como nome de variável, pois são nomes dos tipos nativos.
- Não altere uma lista enquanto a percorre, salvo quando você compreende as consequências. Para remoções mais complexas, crie outra lista ou percorra uma cópia.
- Verifique se um valor existe antes de usar `remove()` quando sua ausência for possível.
- Use uma lista de dicionários para dados pequenos de cadastro; ao estudar POO, cada usuário também poderá virar uma instância de `Usuario`.

Execute [os exemplos](exemplos_listas.py) e depois resolva a [lista de exercícios](desafios.md).
