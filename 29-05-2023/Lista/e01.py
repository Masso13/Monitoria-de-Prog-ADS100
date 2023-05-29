def media(valores):
    soma = sum(valores)
    media = soma // len(valores)
    return media

idades = [18, 18, 19, 18, 19, 19, 20, 20, 20, 21, 25, 27, 22]

media_idades = media(idades)
print(f"A média das idades foi de {media_idades} anos")