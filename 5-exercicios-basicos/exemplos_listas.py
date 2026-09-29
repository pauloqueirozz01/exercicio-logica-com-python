def listar_numeros(numeros):
    """Mostra todos os números recebidos, um por linha."""
    for numero in numeros:
        print(numero)


def listar_emails(emails):
    """Mostra todos os e-mails recebidos, um por linha."""
    for email in emails:
        print(email)


def capturar_usuario():
    """Captura nome e e-mail no terminal e retorna um novo cadastro."""
    nome = input("Nome: ").strip()
    email = input("E-mail: ").strip().lower()
    return {"nome": nome, "email": email}


def adicionar_usuario(usuarios, nome, email):
    """Adiciona à lista um dicionário com os dados de um usuário."""
    usuario = {"nome": nome, "email": email}
    usuarios.append(usuario)


def listar_usuarios(usuarios):
    """Mostra nome e e-mail de cada usuário."""
    for usuario in usuarios:
        print(f"{usuario['nome']} | {usuario['email']}")


def remover_usuario_por_email(usuarios, email):
    """Remove o primeiro usuário com o e-mail informado."""
    for usuario in usuarios:
        if usuario["email"] == email:
            usuarios.remove(usuario)
            return True
    return False


numeros = [4, 8, 15, 16, 23, 42]
emails = ["ana@email.com", "bia@email.com"]
usuarios = []

print("Números:")
listar_numeros(numeros)

emails.append("caio@email.com")
emails.remove("bia@email.com")
print("\nE-mails após adicionar e remover:")
listar_emails(emails)

adicionar_usuario(usuarios, "Ana", "ana@email.com")
adicionar_usuario(usuarios, "Bruno", "bruno@email.com")
adicionar_usuario(usuarios, "Carla", "carla@email.com")

# Para cadastrar uma pessoa pelo terminal, retire os comentários:
# novo_usuario = capturar_usuario()
# usuarios.append(novo_usuario)

print("\nUsuários cadastrados:")
listar_usuarios(usuarios)

foi_removido = remover_usuario_por_email(usuarios, "bruno@email.com")
print(f"\nUsuário removido: {foi_removido}")
listar_usuarios(usuarios)

linguagens = {"Python", "Dart", "Python"}
linguagens.add("C#")
print("\nLinguagens sem repetição:", linguagens)
