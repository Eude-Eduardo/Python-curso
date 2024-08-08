hr = float(input("Quanto você ganha por hora? R$" ))
hrM = float(input("Quantas horas você trabalha por mês?"))
sal = hr*hrM

IR = (sal*0.11)
INSS = (sal*0.08)
sind = (sal*0.05)


print(f"+ Salário bruto: R${sal:.2f}")
print(f"- IR(11%): R${IR:.2f}")
print(f"- INSS (8%): R${INSS:.2f}")
print(f"- Sindicato (5%): R${sind:.2f}")
print(f"Salário Liquido: R${sal-IR-INSS-sind:.2f}")

print("__"*20)

preco_hora = float(input("Digite quanto você ganha por hora: "))
horas_trabalhadas = float(
    input("Digite quantas horas você trabalhou esse mês: ")
)
salario_bruto = preco_hora * horas_trabalhadas
IR = salario_bruto * (11 / 100)
INSS = salario_bruto * (8 / 100)
sindicato = salario_bruto * (5 / 100)
salario_liquido = salario_bruto - IR - INSS - sindicato
print(
    f"+ Salário Bruto : R${salario_bruto:.2f}\n"
    f"- IR (11%) : R${IR:.2f}\n"
    f"- INSS (8%) : R${INSS:.2f}\n"
    f"- Sindicato (5%) : R${sindicato:.2f}\n"
    f"= Salário Liquido : R${salario_liquido:.2f}"
)