estoque = [
    {"nome": "Caixa de Leite 3L", "Data-Vencimento": "01/06/2023"},
    {"nome": "Caixa de Leite 3L", "Data-Vencimento": "01/06/2023"},
    {"nome": "Caixa de Leite 3L", "Data-Vencimento": "15/05/2023"},
    {"nome": "Caixa de Leite 3L", "Data-Vencimento": "25/07/2023"},
    {"nome": "Caixa de Leite 3L", "Data-Vencimento": "29/05/2023"},
    {"nome": "Caixa de Leite 3L", "Data-Vencimento": "25/07/2022"},
]

diaA, mesA, anoA = 28, 5, 2023

def verifica_vencimento(produto):
    vencido = False

    dia, mes, ano = produto["Data-Vencimento"].split("/")
    dia, mes, ano = int(dia), int(mes), int(ano)

    if ano < anoA:
        vencido = True
    elif ano == anoA and mes <= mesA and dia <= diaA:
        vencido = True
    
    return vencido


for produto in estoque:
    print(produto["nome"], verifica_vencimento(produto))