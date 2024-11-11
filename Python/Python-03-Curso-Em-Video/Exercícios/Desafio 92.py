from datetime import date

dados = {}
ano = date.today().year
while True:
    dados["Nome"] = str(input("Nome: "))
    anoNascomento = int(input("Ano de Nascimento: "))
    dados["Idade"] = ano - anoNascomento
    ctps = int(input("Carteira de trabalho (0 - Não tem): "))
    if ctps <= 0:
        dados["CTPS"] = "Não tem"
        break
    dados["CTPS"] = ctps
    dados["Contratação"] = int(input("Ano de contratação: "))
    dados["Salário"] = float(input("Salário: R$"))
    dados["Aposentadoria"] = (dados["Contratação"] + 35) - anoNascomento
    break
print("-=" * 20)
for k, v in dados.items():
    if k == "Idade" or k == "Aposentadoria":
        print(f" - {k}: {v} anos")
    elif k == "Salário":
        print(f" - {k}: R${v:.2f}")
    else:
        print(f" - {k}: {v}")