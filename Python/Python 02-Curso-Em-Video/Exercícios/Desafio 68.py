from random import randrange
print("-="*12)
print("VAMOS JOGAR PAR OU IMPAR")
print("-="*12)
pc = 0
cont = 0
while True:
    pc = randrange(0, 11)
    player = int(input("Digite um valor: "))
    parImp = str(input("PAR ou IMPAR? [P/I]")).upper()[0]
    soma = player + pc
    print("__"*12)
    print(f"você jogou {player} e o computador jogou {pc}. total = {soma}\n")
    print("__"*12)
    if soma % 2 == 0:
        # par
        if parImp == "P":
            print("VOCÊ VENCEU!\n")
        else:
            print("VOCÊ PERDEU!\n")
            break
    else:
        if parImp == "I":
            print("VOCÊ VENCEU!\n")
        else:
            print("VOCÊ PERDEU!\n")
            break
    cont += 1
    print("Vamos jogar novamente...")
    print("-="*12)

print(f"GAME OVER! Você venceu {cont} vezes.")
