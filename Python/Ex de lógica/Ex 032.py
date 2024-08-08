nota1 = float(input("Primeira nota: ")) 
nota2 = float(input("Segunda nota: "))
media = (nota1 + nota2)/2

if media <= 4:
    nota = "E"
elif media <= 6:
    nota = "D"
elif media <= 7.5:
    nota = "C"
elif media <= 9.0:
    nota = "B"
else:
    nota = "A"

if nota == "A" or nota == "B" or nota == "C":
    print(f"Sua média foi {media:.1f} e você foi == Aprovado ==")
else:
    print(f"Sua média foi {media:.1f} e você foi -- Reprovado --")
