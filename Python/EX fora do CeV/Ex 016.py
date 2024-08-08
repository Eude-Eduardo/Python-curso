h = float(input("Altura da parede: "))
b = float(input("Largura da parede: "))
m2 = b*h
litros_tinta = m2/3

print(f"A sua parede de {m2:.2f}m² vai precisar de {int(litros_tinta)} litros de tinta, com o valor de R${int(litros_tinta)*80:.2f}")






