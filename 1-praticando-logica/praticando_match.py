"""Menu de estudos para praticar funções e match (Python 3.10+)."""


def estudar_variaveis():
    print("Estude como guardar valores em variáveis.")


def estudar_aritmetica():
    print("Pratique contas com números.")


def estudar_condicionais():
    print("Pratique decisões com if e else.")


def mostrar_menu():
    print("Escolha um assunto: Variáveis, Aritmética ou Condicionais.")
    print("Digite Sair para encerrar.")


def escolher_acao(opcao):
    match opcao:
        case "variáveis":
            estudar_variaveis()
        case "aritmética":
            estudar_aritmetica()
        case "condicionais":
            estudar_condicionais()
        case "sair":
            print("Até a próxima prática!")
        case _:
            print("Opção inválida. Execute novamente e escolha um item do menu.")


def main():
    mostrar_menu()
    opcao = input("Sua escolha: ").strip().lower()
    escolher_acao(opcao)


if __name__ == "__main__":
    main()
