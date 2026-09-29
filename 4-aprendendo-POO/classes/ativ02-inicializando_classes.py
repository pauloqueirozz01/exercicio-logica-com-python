# Exercícios — __init__ e self

# Comece com:
# class Restaurante:
#     pass

# Crie o método __init__ dentro da classe Restaurante. Ele deve receber self, nome e categoria.
# Dentro do __init__, utilize self para armazenar nome e categoria como atributos da instância.
# Ainda utilizando self, crie o atributo ativo e faça todo restaurante começar com o valor False.
# Crie restaurante_praca utilizando:
# restaurante_praca = Restaurante("Leão da Praça", "Brasileira")
# Acesse restaurante_praca.nome. Compare esse acesso com a atribuição self.nome = nome existente dentro do construtor. Tente explicar com suas palavras qual é a relação entre os dois.
# Crie uma segunda instância:
# restaurante_pizza = Restaurante("Pizza Place", "Italiana")
# Imprima o nome das duas instâncias.

# Altere:
# restaurante_pizza.ativo = True

# Depois imprima ativo dos dois restaurantes. Explique por que alterar um restaurante não alterou o outro.
# Adicione à classe o seguinte método:
# def exibir_informacoes(self):
#     print(self.nome)
#     print(self.categoria)
#     print(self.ativo)

# Utilize esse método com os dois restaurantes.
# Dentro de exibir_informacoes, substitua temporariamente self.nome por apenas nome. Execute novamente e investigue o erro apresentado pelo Python.

# Desafio: crie o método ativar(self), responsável por alterar o atributo ativo do próprio restaurante para True.
# Desafio: crie desativar(self), responsável por fazer o contrário.

# Explique com suas próprias palavras o que self representa nesta chamada:
# restaurante_praca.exibir_informacoes()

# E depois nesta:
# restaurante_pizza.exibir_informacoes()

# A pergunta 12 é particularmente importante para verificar se aprenderam de verdade.
# O aluno deveria eventualmente chegar à conclusão de que:
# restaurante_praca.exibir_informacoes()
# #                          ↑
# # self representa restaurante_praca
# enquanto:
# restaurante_pizza.exibir_informacoes()
# #                          ↑
# # self representa restaurante_pizza
# Ou, simplificando para a aula:
# self = "este objeto aqui".