dist = float(input("Qual é a distancia da sia viagem:"))
print(f"Você vai começar uma viagem de {dist:.0f}Km")
Preço = dist * 0.5 if dist <= 200 else dist * 0.45
print(f"Sua viagem de {dist:.0f}Km vai custar R${Preço:.2f}")    