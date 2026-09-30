class Restaurant:
  def __init__(this, nome, categoria, ativo=False):
    this.nome = nome
    this.categoria = categoria
    this.ativo = ativo

## Usamos o método __str__ para definir como podemos mostrar o objeto com texto puro
## A saída no terminal agora, não vai ser mais só uma class << objeto >>
## Agora, podemos ver os textos das informações da nossa instância

  def __str__(this):
    status = "Sim" if this.ativo else "Não"
    return f"""
    Restaurante: {this.nome}, 
    Categoria: {this.categoria}, 
    Está aberto? {status}
    """

restaurant_italian = Restaurant("La Pasta Food", "Culinária Italiana", True)

print(restaurant_italian)