# Implemente uma classe chamada Carro com os atributos básicos, como:
# modelo, cor e ano.

print("""
RESOLVENDO PRIMEIRA QUESTÃO
""")

class Car:
  def __init__(self, model, color, year):
    self.model = model
    self.color = color
    self.year = year

  def list_details(self):
    print(f"""
    Informações sobre o carro:
    Nome do Modelo: {self.model}
    Cor do Carro: {self.color}
    Ano de Fabricação: {self.year}
\n
""")


# Crie uma instância dessa classe e atribua valores aos seus atributos.
print(f"Criando uma instância da classe {Car}, como pede a segunda questão\n")
sedan_car = Car("Yaris", "Cinza", 2026)
sedan_car.list_details()

# Crie uma classe chamada Restaurante com os atributos
# nome, categoria, ativo e crie mais 2 atributos.

class Restaurant:
  # Quando modificar a classe, ele vai pedir para modificar tudo que precisa ter um valor setado.
  def __init__(self, name, category, opened=False , review=0.0, parking=False):
    self.name = name
    self.category = category
    self.opened = opened
    self.review = review
    self.parking = parking

  def list_details(self):
    print(f"""
    Informações sobre o restaurante: {self.name},
    Nome do Restaurante: {self.name},
    Categoria do Restaurante: {self.category},
    Aberto: {self.opened}
    Avaliação do Restaurante: {self.review},
    Estacionamento gratuito: {self.parking}
    """)

# Instancie um restaurante e atribua valores aos seus atributos.
print("Instanciando um restaurante e atribuindo seus respectivos valores.")
restaurant_nomeOfSpain = Restaurant("Nome da Espanha", "Comida Típica Espanhola",True, 4.5, False)
restaurant_nomeOfSpain.list_details();
# Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e inicia ativo como False por padrão.

# Crie uma instância utilizando o construtor.
# Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante.
# Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.
