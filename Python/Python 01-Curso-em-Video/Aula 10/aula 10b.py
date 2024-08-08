n1 = float(input("Digite a primeira nota:"))
n2 = float(input("Digite a segunda nota:"))
m = (n1 + n2)/2
print(f"Sua média foi {m:.1f}")
print("parabéns" if m >= 7 else "ESTUDE MAIS")