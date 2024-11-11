from datetime import date
dados = {}
dados["Nome"] = str(input("Nome: "))
nasc = int(input("Ano de Nascimento: "))
dados["idade"] = date.today().year - nasc
dados["CTPS"] = int(input("Carteira de Trabalho (0 não tem)"))
if dados != 0:
    dados["Contratação"] = int(input("Ano de Contratação: "))
    dados["Salario"] = float(input("Salário: R$"))
    dados["Aposentadioria"] = (dados["idade"] + dados["Contratação"] + 35) - date.today().year
print("-=" * 20)
for k, v in dados.items():
    print(f" - {k} tem o valor {v}")