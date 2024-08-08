vel = float(input("Sua velocidade:"))
if vel<= 80:
    print("tenha um bom dia e dirija com segurança")
else:
    print(f"Você ultrapassou o limite de velocidade sua multa é de R${(vel - 80)*7:.2f}")