nota1 = float(input("Nota 1:"))
nota2 = float(input("Nota 2:"))
media = (nota1 + nota2)/2

if media < 7:
    print(f"foi reprovado com média {media:.1f}")
elif media >= 7 and media <= 8.5:
    print(f"A sua média foi de {media:.1f} e está de recuperação")
elif media > 8.5 and media <=9.5:
    print(f"foi aprovado com média {media:.1f}")
else:
    print(f"Aprovado com louvor, parabéns a sua média foi {media:.1f}")
