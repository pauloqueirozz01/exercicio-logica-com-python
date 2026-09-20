# NO nosso primeiro arquivo da categoria praticando-logica/
# No exemplo anterior que está no arquivo: praticando_print.py,
# fizemos uso do comando print() para exibir informações na tela do terminal.
# Agora, vamos praticar o uso de variáveis, que são utilizadas para armazenar informações.

# E, de quebra a gente pode adicionar valores para informações 
# ou capturar esses valores para as nossas informações.
# Como fazer isso?
# Vamos fazer isso agora :)

#Capturando informações do usuário com o comando input()
name = input("Digite seu nome: ");
sobrenome = input("Digite seu sobrenome: ");

# Criando a variavel nome_completo, que vai armazenar o valor do nome e do sobrenome do usuário.
nome_completo =  name + " " + sobrenome;
print(f"Seu nome completo é: {nome_completo}");

# Caputarando a idade e o ano de nascimento com o comando input() 
# para armazenar o que o usuário vai digitar.
age = input("Digite sua idade: ");
print(f"Sua idade é: {age}");

# Capturando o ano de nascimento do usuário com o comando input()
# e armazenando o valor digitado na variável year_of_birth.
year_of_birth = input("Digite o ano de nascimento: ");
print(f"Ano de nascimento: {year_of_birth}");

# ou seja, com tantas informações, podemos fazer o seguinte:
print(f"Olá, {nome_completo}, você tem {age} anos e nasceu em {year_of_birth}. Que legal! \n");
