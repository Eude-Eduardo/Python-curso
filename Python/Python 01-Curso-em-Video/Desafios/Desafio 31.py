dist = int(input("Qual a distância da sua viagem:"))
if dist > 200:
    print(f"Sua viagem de {dist}Km vai custar R${dist*0.45:.2f}")
else:
    print(f'Sua viagem de {dist}Km vai custar R${dist*0.5:.2f}')