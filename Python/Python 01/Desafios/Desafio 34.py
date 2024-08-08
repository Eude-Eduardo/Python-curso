sal = float(input("Qual o seu salário? R$"))
if sal > 1250.00:
    print(f"Seu novo salário é R${sal+(sal*0.1):.2f}")
else:
    print(f"Seu novo salário é R${sal+(sal*0.15):.2f}")
