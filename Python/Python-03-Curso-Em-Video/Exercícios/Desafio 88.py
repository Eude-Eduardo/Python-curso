from random import randint
from time import sleep
print("=="*20)
print("{:^40}".format("MEGA SENA"))
print("=="*20)
numJogos = int(input("Quantos jogos você quer que eu sorteie? "))
print(f" -=-=-= SORTEANDO {numJogos} JOGOS =-=-=-")
jogos = list()
count = 1
while True:
    num = randint(1, 60)
    if jogos.count(num) == 0:
        jogos.append(num)
    if len(jogos) == 6:
        jogos.sort()
        print(f"Jogo {count}:{jogos}")
        sleep(1)
        jogos.clear()
        count += 1
    if count == numJogos+1:
        print("-=-=-=-= < BOA SORTE > =-=-=-=-")
        break
