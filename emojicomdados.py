emoji_data = {

  "nome": "Smile",

  "grade": [

    [(255,255,0), (255,255,0), (255,255,0), (255,255,0), (255,255,0)], # Linha 0

    [(255,255,0), (0,0,0),  (255,255,0), (0,0,0),  (255,255,0)], # Linha 1 (Olhos)

    [(255,255,0), (255,255,0), (255,255,0), (255,255,0), (255,255,0)], # Linha 2

    [(255,255,0), (0,0,0),  (0,0,0),  (0,0,0),  (255,255,0)], # Linha 3 (Boca)

    [(255,255,0), (255,255,0), (255,255,0), (255,255,0), (255,255,0)] # Linha 4

  ]

}

nova_grade = []

for chave, valor in emoji_data.items():

  if chave == "grade":

    for linha in valor:

      nova_linha = []

      for pixel in linha:

        if pixel == (255,255,0):

          novo_pixel = (pixel[0]//2, pixel[1]//2, pixel[2]//2)

        else:

          novo_pixel = pixel

        nova_linha.append(novo_pixel)

      nova_grade.append(nova_linha)

emoji_data["grade"] = nova_grade

print(emoji_data)


##parte 2


biblioteca_musical = {

  "Toques": [

    {"Alegre": ([440, 480], [520, 560])},

    {"Triste": ([200, 150], [100, 50])}

  ]

}

for item in biblioteca_musical["Toques"]:

  for nome, matriz in item.items():

    linha1 = matriz[0]

    linha2 = matriz[1]

    # Transposição
    nova_matriz = (

      [linha1[0], linha2[0]],

      [linha1[1], linha2[1]]

    )

    # Atualiza o dicionário
    item.update({nome: nova_matriz})

print(biblioteca_musical)


##parte 3


playlist_imagens = {

  "Playlist": [

    {

      "Sol": (

        [(255,255,0), (255,255,0)],

        [(255,255,0), (255,255,0)]

      )

    },

    {

      "Noite": (

        [(0,0,0), (0,0,0)],

        [(0,0,0), (0,0,0)]

      )

    }

  ]

}

nova_playlist = []

for item in playlist_imagens["Playlist"]:      # 1º nível

  for nome in item.keys():             # usando .keys()

    imagem = item[nome]

    nova_imagem = []

    for linha in imagem:             # 2º nível

      nova_linha = []

      for pixel in linha:           # 3º nível

        # exemplo de transformação:
        # inverter cores simples
        novo_pixel = (
          255 - pixel[0],
          255 - pixel[1],
          255 - pixel[2]
        )

        nova_linha.append(novo_pixel)

      # usando .insert()
      nova_imagem.insert(0, nova_linha)

    # usando .pop()
    if len(nova_imagem) > 1:

      nova_imagem.pop()

    nova_playlist.append({nome: tuple(nova_imagem)})

playlist_imagens["Playlist"] = nova_playlist

print(playlist_imagens)