def media(valores):
    soma = sum(valores)
    media = soma / len(valores)
    return media

notas = []

while True:
    nota = float(input("\nDigite a nota do aluno: "))
    notas.append(nota)

    escolha = input("Deseja parar ? (S/N) ").upper()
    if escolha == "S":
        break

media_notas = media(notas)
print(f"A média de notas foi de {media_notas} pontos")