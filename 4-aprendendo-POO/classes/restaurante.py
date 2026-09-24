class Restaurante:
  nome = '';
  categoria = '';
  aberto = False;

restaurante_praca = Restaurante();
restaurante_praca.nome = "Leão da Praça"
restaurante_praca.categoria = "Comida Típica Brasileira"
restaurante_praca.aberto = True

restaurante_praia = Restaurante();

restaurantes = [restaurante_praca, restaurante_praia]
print(restaurante_praca)