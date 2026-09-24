class Music:
  nome = ''
  artista = ''
  duracao = int


Music1 = Music()
Music1.nome = "Bohemian Rhapsody"
Music1.artista = "Queen"
Music1.duracao = 350
print(Music1)

Music2 = Music()
Music2.nome = "Original"
Music2.artista = "Malcom Todd"
Music2.duracao = 160
print(Music2)

Music3 = Music()
Music3.nome = "The Feeling"
Music3.artista = "Steve Lacy"
Music3.duracao = 137


## Acessando e impriminod as informações da instancia Music1
print(f"""
Acessando {Music1}, informações sobre a faixa {Music1.nome}
Nome da Musica: {Music1.nome}
Artista ou Banda: {Music1.artista}
Duração: {Music1.duracao}
""")