import os


header_inicio = """
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
"""

header_register = """

█▀▀ ▄▀█ █▀▄ ▄▀█ █▀ ▀█▀ █▀█ █▀█
█▄▄ █▀█ █▄▀ █▀█ ▄█ ░█░ █▀▄ █▄█
"""
header_query = """

█▀▀ █▀█ █▄░█ █▀ █░█ █░░ ▀█▀ ▄▀█
█▄▄ █▄█ █░▀█ ▄█ █▄█ █▄▄ ░█░ █▀█
"""
header_remove = """

█▀█ █▀▀ █▀▄▀█ █▀█ █░█ █▀▀ █▀█
█▀▄ ██▄ █░▀░█ █▄█ ▀▄▀ ██▄ █▀▄
"""
header_exiting = """

█▀ ▄▀█ █ █▄░█ █▀▄ █▀█ ░ ░ ░
▄█ █▀█ █ █░▀█ █▄▀ █▄█ ▄ ▄ ▄
"""

print("<-- Bem vindo ao nosso programa -->");
print("Este é um programa simples em Python.\n");

# Abaixo, solicitamos que o usuário digite o que ele quer fazer no nosso programa, listando as opções dele
# e armazenando ela a resposta logo após a pergunta, 
# para que possamos utilizar ela em nosso programa.

print("Digite uma das opções abaixo:");
options = ["Cadastrar", "Consultar", "Remover", "Sair"];

def show_header():
     print(header_inicio);

def close_app():
     # os.system('cls')
     os.system('clear')
     print("Encerrando o programa.\n")

# Usando um Loop for in range(len(options)) para percorrer a lista de opções
# e imprimir cada uma delas com seu índice correspondente.
for i in range(len(options)):
    print(f"{i}: {options[i]}")

# Atribuímos uma variável para armazenar a resposta do usuário
input_typed = input("O que você deseja fazer hoje?\n");

print(f"Você escolheu: {input_typed}\n");

# Usando lógica condicional,
# para mostrar uma mensagem diferente em determinada opção escolhida pelo usuário.
if (input_typed != "Sair"):
    if (input_typed == "Cadastrar"):
        print(header_register)
    elif (input_typed == "Consultar") :
        print(header_query)
    elif (input_typed == "Remover") :
        print(header_remove)
else :
    print(header_exiting)

# Também podemos fazer de uma forma mais simplificada, 
# mas isso seria para somente a gente entender que há mais de uma forma de escrever um algoritmo.
if input_typed == "Cadastrar":
      print(header_register)
elif input_typed == "Consultar":
      print(header_query)
elif input_typed == "Remover":
      print(header_remove)
elif input_typed == "Sair":
      print(header_exiting)
      close_app()


def main():
     show_header;

if __name__ == "__main__":
    main()
