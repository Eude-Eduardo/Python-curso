sal = float(input("What's your wage? R$"))

if sal < 1:
    print("Salário inválido")
elif sal <= 280:
    print(
          f"O seu salário de R${sal:.2f} \n"
          f"Com um almento de 20% \n"
          f"Aumentou R${sal*0.2:.2f} \n"
          f"Ficando com R${sal+(sal*0.2):.2f}"
          )
elif sal <= 700:
    print(
        f"O seu salário de R${sal:.2f} \n"
        f"Com um aumento de 15% \n"
        f"Aumentou R${sal*0.15:.2f} \n"
        f"Ficando com R${sal+(sal*0.15):.2f} de salário"
    )
elif sal <= 1500:
    print(
        f"O seu salário de R${sal:.2f} \n"
        f"Com um aumento de 10% \n"
        f"Aumentou R${sal*0.1:.2f} \n"
        f"Ficando com R${sal+(sal*0.1):.2f} de salário."
    )
else:
    print(
        f"O seu salário de R${sal:.2f} \n"
        f"Com um aumento de 5% \n"
        f"Aumentou R${sal*0.05:.2f} \n"
        f"Ficando com R${sal+(sal*0.05):.2f} de salário."
    )