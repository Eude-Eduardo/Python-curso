horas = int(input("Quantas horas você trabalha no mês? "))
horas_mes = int(input("Quanto você ganha por hora? "))
salario_bruto = horas * horas_mes
fgts = salario_bruto * 0.11
inss = salario_bruto * 0.10

print("{:=^30}".format("Calculo de descontos"))

if salario_bruto < 1:
    print("inválido")
elif salario_bruto <= 900:
    print(
        f"Salário Bruto:      R${salario_bruto:.2f} \n"
        f"(-) IR (0%):        Isento \n"
        f"(-) INSS (10%):     R${inss:.2f} \n"
        f"FGTS (11%):         R${fgts:.2f} \n"
        f"Total de descontos: R${inss:.2f} \n"
        f"Salário Liquido:    R${salario_bruto - (inss)}"
    )
elif salario_bruto <= 1500:
    print(
        f"Salário Bruto:      R${salario_bruto:.2f} \n"
        f"(-) IR (5%):        R${salario_bruto*0.05:.2f} \n"
        f"(-) INSS (10%):     R${inss:.2f} \n"
        f"FGTS (11%):         R${fgts:.2f} \n"
        f"Total de descontos: R${inss + salario_bruto*0.05:.2f}"
        f"Salário liquido:    R${salario_bruto - (inss + salario_bruto*0.05)}"
    )
elif salario_bruto <= 2500:
    print(
        f"Salário Bruto:      R${salario_bruto:.2f} \n"
        f"(-) IR (10%):       R${salario_bruto*0.10:.2f} \n"
        f"(-) INSS (10%):     R${inss:.2f} \n"
        f"FGTS (11%):         R${fgts:.2f} \n"
        f"Total de descontos: R${inss + (salario_bruto*0.10):.2f} \n"
        f"Salário liquido:    R${salario_bruto - (inss + salario_bruto*0.10)}"
    )
else:
    print(
        f"Salário Bruto:      R${salario_bruto:.2f} \n"
        f"(-) IR (10%):       R${salario_bruto*0.20:.2f} \n"
        f"(-) INSS (10%):     R${inss:.2f} \n"
        f"FGTS (11%):         R${fgts:.2f} \n"
        f"Total de descontos: R${inss + (salario_bruto*0.20):.2f} \n"
        f"Salário liquido:    R${salario_bruto - (inss + salario_bruto*0.20)}"
    )
    