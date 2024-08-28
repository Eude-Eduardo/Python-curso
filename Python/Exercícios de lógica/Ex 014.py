peso = float(input("Quantos quilos?"))


if peso <=50:
    print(f"Seu peixe tem {peso}Kg, não é nescessário multa")
else:
    exe = (peso-50)*4
    print(f"Seu peixe tem {peso:.2f}Kg, a sua multa é de {exe:.2f}")   