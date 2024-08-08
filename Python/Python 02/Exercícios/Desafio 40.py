nota1 = float(input("Nota 1:"))
nota2 = float(input("Nota 2:"))
media = (nota1+nota2)/2
print(media)

if media < 5:
    print(f"Suas notas foram {nota1:.1f} e {nota2:.1f} por isso você foi reprovado e sua média foi de {media:.1f} pontos")
elif media >= 5 and media <= 6.9:
    print(f"Suas notas foram {nota1:.1f} e {nota2:.1f} por isso você está em recuperação, a sua média foi de {media:.1f} pontos")
else:
    print(f"Suas notas foram {nota1:.1f} e {nota2:.1f} por isso parabéns você foi aprovado com {media:.1f} pontos de média")