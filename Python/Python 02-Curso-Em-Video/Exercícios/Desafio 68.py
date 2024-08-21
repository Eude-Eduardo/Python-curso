from random import randrange
print("-="*12)
print("VAMOS JOGAR PAR OU IMPAR")
print("-="*12)
contV = 0
while True:
    pc = randrange(0, 11)
    player = int(input("Digite um valor: "))
    parImp = str(input("PAR ou IMPAR? [P/I]")).upper()[0].strip()
    while parImp != "I" and parImp != "P":
        parImp = str(input("PAR ou IMPAR? [P/I]")).upper()[0].strip()
    soma = player + pc
    print("__"*12)
    print(f"você jogou {player} e o computador jogou {pc}. total de {soma}", end=" ")
    print("DEU PAR" if soma % 2 == 0 else "DEU IMPAR")
    print("__"*12)
    if soma % 2 == 0:
        # par
        if parImp == "P":
            print("VOCÊ VENCEU!\n")
        else:
            print("VOCÊ PERDEU!\n")
            break
    else:
        #impar
        if parImp == "I":
            print("VOCÊ VENCEU!\n")
        else:
            print("VOCÊ PERDEU!\n")
            break
    contV += 1
    print("Vamos jogar novamente...")
    print("-="*12)

print(f"GAME OVER! Você venceu {contV} vezes.")
