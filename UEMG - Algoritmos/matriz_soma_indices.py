
matriz = []


for coluna in range(7):
    linha = []

    for linhaIndex in range(8):
        linha.append(coluna + linhaIndex)

    matriz.append(linha)
    print(f"matriz ${matriz[coluna]}")

