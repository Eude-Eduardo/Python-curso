print("=="*20)
print(f"{"SUPERMARCADO":^40}")
print("=="*20)
soma = maisMil = cont = menor = 0
nomeMenor = ""
while True:
    nome = str(input("Nome do produto: ")).strip()
    preço = float(input("Preço: R$"))
    soma += preço
    cont += 1
    if cont == 1 or preço < menor:
        menor = preço
        nomeMenor = nome
    if preço > 1000:
        maisMil += 1
    print("=="*20)
    res = " "
    while res not in "SN":
        res = str(input("Quer continuar? [S/N] ")).upper()[0].strip()
    if res == "N":
        break
print("{:=^40}".format("FIM DO PROGRAMA"))
print(
    f"O total da compra foi: R${soma:.2f}\n"
    f"Temos no total {maisMil} produtos custando mais de R$1000.00\n"
    f"O produto mais barato foi '{nomeMenor.capitalize()}' custando R${menor:.2f}"

    )