vel  = float(input("Qual é a sua velocidade?"))

if vel > 80:
    print(f"você encedeu o limite de velocidade que é de 80km/h e foi multado em RS{(vel - 80)*7:.2f}")
print("Tenha uma boa viagem")