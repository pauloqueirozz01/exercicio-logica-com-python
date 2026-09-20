# O que é uma tupla?
# Uma tupla é uma coleção de elementos que são imutáveis, ou seja, não podem ser alterados após a sua criação.
# As tuplas são definidas utilizando parênteses () e os elementos são separados por vírgulas.
# Elas podem conter elementos de diferentes tipos, como números, strings, listas e até outras tuplas.
# As tuplas são úteis quando você deseja armazenar um conjunto de valores que não devem ser modificados,
# como coordenadas, configurações ou registros de dados.
print("""
  P
  A
  U
  L
  O
""")

# Exemplo de uso de tupla em Python
# Usando uma tupla para imprimir o cabeçalho OU a primeira mensagem do programa.
print("""
░█████╗░░█████╗░██████╗░██╗███╗░░██╗░██████╗░
██╔══██╗██╔══██╗██╔══██╗██║████╗░██║██╔════╝░
██║░░╚═╝██║░░██║██║░░██║██║██╔██╗██║██║░░██╗░
██║░░██╗██║░░██║██║░░██║██║██║╚████║██║░░╚██╗
╚█████╔╝╚█████╔╝██████╔╝██║██║░╚███║╚██████╔╝
░╚════╝░░╚════╝░╚═════╝░╚═╝╚═╝░░╚══╝░╚═════╝░
""")

# Exemplo de uso de tupla em Python
# Criando uma tupla com diferentes tipos de elementos
minha_tupla = (1, "Olá", 3.14, [1, 2, 3], (4, 5, 6))
print(minha_tupla)

# Usando tuplas para fazer a impressão de descrições de produtos
# Imagine que você está desenvolvendo em Python para a Meteora, uma loja de roupas e-commerce.
# Você está no processo de adicionar descrições de produtos ao site
# e precisa usar a função print em python para exibir as descrições na página.
# As descrições dos produtos incluem várias linhas e parágrafos.

# Como implementar isso em Python?
# Uma maneira de fazer isso é utilizando tuplas para armazenar as descrições dos produtos.
print("""
  Produto: Camiseta Básica
  Tamanho: P, M, G
  Material: Algodão, Poliéster
  Cores disponíveis: Azul, Vermelho, Verde
  Instruções de lavagem: Lavar à mão, Não usar alvejante, Secar à sombra
  Garantia: 6 meses contra defeitos de fabricação
""")