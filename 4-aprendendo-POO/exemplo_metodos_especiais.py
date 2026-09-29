class Restaurante:
    """Representa um restaurante e demonstra __init__ e __str__."""

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

    def __str__(self):
        estado = "ativo" if self.ativo else "inativo"
        return f"{self.nome} | {self.categoria} | {estado}"

    def ativar(self):
        self.ativo = True


restaurante_praca = Restaurante("Praça", "Gourmet")
restaurante_pizza = Restaurante("Pizza Express", "Italiana")

print(restaurante_praca)
print(restaurante_pizza)

restaurante_pizza.ativar()
print(restaurante_pizza)

print("Atributos da instância:", vars(restaurante_pizza))
