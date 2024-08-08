letra = str(input("Digite uma letra: "))

if letra.lower() in "a e i o u":
    print(f"A letra '{letra}' É vogal")
else:
    print(f"A letra '{letra}' não é vogal")