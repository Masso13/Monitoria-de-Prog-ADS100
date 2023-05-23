idades = [18, 18, 19, 18, 19, 19, 20, 20, 20, 21, 25, 27, 22]

soma = 0
for idade in idades:
    soma += idade

media = soma // len(idades)
print(media)