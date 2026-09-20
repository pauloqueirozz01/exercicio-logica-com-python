
print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

print("<-- Bem vindo ao nosso programa -->");
print("Este é um programa simples em Python.\n");

# Abaixo, solicitamos que o usuário digite o que ele quer fazer no nosso programa, listando as opções dele
# e armazenando ela a resposta logo após a pergunta, 
# para que possamos utilizar ela em nosso programa.

print("Digite uma das opções abaixo:");
options = ["Cadastrar", "Consultar", "Remover", "Sair"];

# Usando um Loop for in range(len(options)) para percorrer a lista de opções
# e imprimir cada uma delas com seu índice correspondente.
for i in range(len(options)):
    print(f"{i}: {options[i]}")

# Atribuímos uma variável para armazenar a resposta do usuário
input_typed = input("O que você deseja fazer hoje?\n");

print(f"Você escolheu: {input_typed}\n");

print("<-- Fim do programa -->\n");