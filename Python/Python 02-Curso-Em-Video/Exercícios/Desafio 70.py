nome = ""
preço = 0
res = "S"
soma = 0
pr = []
maisMil = 0
nomeMenor = ""
while res == "S":
    nome = str(input("Nome do produto: "))
    preço = float(input("Preço: R$"))
    soma += preço
    pr.append(preço)
    if preço > 1000:
        maisMil += 1
    if min(pr):
        nomeMenor = nome
    res = str(input("Quer continuar? [S/N] ")).upper()[0]
    while res != "S" and res != "N":
        res = str(input("Quer continuar? [S/N] ")).upper()[0]
print(
    f"O total da compra foi: R${soma:.2f}\n"
    f"Temos no total {maisMil} produtos custando mais de R$1000.00\n"
    f"O produto mais barato foi {nomeMenor.capitalize()} custando R${min(pr):.2f}"

    )