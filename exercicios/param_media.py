
def param_media(*numeros: float):
    soma_geral = 0

    for item in numeros:
        soma_geral += item

    media = soma_geral / len(numeros)
    print(f'media = {media}')

param_media(10, 5, 10.5)