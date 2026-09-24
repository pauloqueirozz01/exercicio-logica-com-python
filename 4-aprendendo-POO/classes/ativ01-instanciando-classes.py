# Em uma carreira de desenvolvimento de software, a prática consistente desempenha um papel fundamental na construção de bases sólidas. Pensando nisso, criamos uma lista de atividades (não obrigatórias) focada em prática para melhorar ainda mais sua experiência de aprendizagem. Bora praticar então?

# Exercícios
# Atribua o valor 'Italiana' ao atributo categoria da instância restaurante_praca da classe Restaurante.
# Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.
# Verifique o valor inicial do atributo ativo para a instância restaurante_praca e exiba uma mensagem informando se o restaurante está ativo ou inativo.
# Acesse o valor do atributo de classe categoria diretamente da classe Restaurante e armazene em uma variável chamada categoria.
# Altere o valor do atributo nome para 'Bistrô'.
# Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 'Pizza Place' e categoria 'Fast Food'.
# Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.
# Mude o estado da instância restaurante_pizza para ativo.
# Imprima no console o nome e a categoria da instância restaurante_praca.

class Restaurant :
  nome = ''
  categoria = ''
  disponivel = False

  def checa_disponibilidade(self):
    if (Restaurant.disponivel != False):
      print(f"O restaurante {self.nome} ainda está em ativa. Você pode ir visitá-lo")
    else :
      print(f"O restaurante {self.nome} não está mais em ativa. Não é possível ir até o estabelecimento.")

# A primeira atividade pede para atribuirmos uma Categoria Italiana para a nossa instância.
restaurante_italiano = Restaurant()
restaurante_italiano.nome = "La Masa"
restaurante_italiano.categoria = "Italiana"
restaurante_italiano.disponivel = True

restaurante_praca = Restaurant();
restaurante_praca.nome = "Leão da Praça"
restaurante_praca.categoria = "Comida Típica Brasileira"
restaurante_praca.aberto = True

# Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.
print(f"Acessando o atributo nome da instância: {restaurante_praca.nome}")

# Verifique o valor inicial do atributo ativo para a instância restaurante_praca 
# e exiba uma mensagem informando se o restaurante está ativo ou inativo.
if (restaurante_praca.disponivel != False):
  print(f"O restaurante {restaurante_praca.nome} ainda está em ativa. Você pode ir visitá-lo")
else :
  print(f"O restaurante {restaurante_praca.nome} não está mais em ativa. Não é possível ir até o estabelecimento.")