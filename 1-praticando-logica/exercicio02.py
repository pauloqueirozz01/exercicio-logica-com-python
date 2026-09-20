print("Hello, guys!")
print("<-- Fazendo o primeiro exercício de lógica com Python -->\n")

print("""
### 2. Apresentação pessoal

Imprima a frase 
=> `Meu nome é {nome} e tenho {idade} anos`, substituindo `{nome}` e `{idade}` pelos valores guardados em variáveis. 
Escolha seu nome e sua idade antes de executar o programa.

Por exemplo, se `nome` guardar `Ana` e `idade` guardar `20`, a saída deve ser:

Meu nome é Ana e tenho 20 anos\n""")

print("Vamos lá?\n")

# Primeiro, vou criar uma variavel chamada nome para armazenar o nome do usuário, e outra chamada idade para armazenar a idade do usuário.
# Lembrando que temos como perguntar qual o nome e a idade do usuario, usando o comando input().

# Vamos usar neste exemplo, o input() para capturar e usar o print() para exibir a mensagem final.
name = input("Digite seu nome: ");
age = input("Digite sua idade: ");

print(f"Seu nome é {name} e você tem {age} anos de idade.")


# Também há como já declararmos um valor para as variaveis, no meu caso, por exemplo
nome = "Paulo"
idade = 22
print(f"Seu nome é {nome} e você tem {idade} anos de idade.")

# Para fortalecer e fixar bem o aprendizado, a gente pode sempre estar variando.
# Gosto de usar o input() para deixar a apresentação de nomes e idades dinâmicas.