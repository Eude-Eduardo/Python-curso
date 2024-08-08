import random
from time import sleep

print("_="*15)
print("Vamos jogar Pedra, papel e tesoura?")
print("_="*15)
pc = random.randint(1,3)
print("""1- Pedra
2- Papel
3- Tesoura""")
p1 = int(input("Faça a sua escolha:"))

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!")



if p1 <= 0 or p1 > 3:
    print("Valor inválido")
elif pc == p1:
    print("---Deu Empate---")
elif pc == 1 and p1 == 2:
    print("-=-"*10)
    print(" Você colocou Pedra ")
    print(" O computador jogou Papel ")
    print("-=-"*10)
    print("JOGADOR VENCEU")
elif pc == 2 and p1 == 3:
    print("-=-"*10)
    print(" Você colocou Papel ")
    print(" O computador jogou Tesoura ")
    print("-=-"*10)
    print("JOGADOR VENCEU")
elif pc == 3 and p1 == 1:
    print("-=-"*10)
    print(" Você colocou Tesoura ")
    print(" Computador jogou Pedra")
    print("-=-"*10)
    print("JOGADOR VENCEU")
elif pc == 1 and p1 == 3:
    print("-=-"*10)
    print(" O Computador colocou pedra ")
    print(" Você jogou Tesoura ")
    print("-=-"*10)
    print("COMPUTADOR VENCEU")
elif pc == 3 and p1 == 2:
    print("-=-"*10)
    print(" O Computador colocou tesoura ")
    print(" Você jogou Papel ")
    print("-=-"*10)
    print("COMPUTADOR VENCEU")
elif pc == 2 and p1 == 3:
    print("-=-"*10)
    print(" O Computador colocou papel ")
    print(" Você jogou Pedra ")
    print("-=-"*10)
    print("COMPUTADOR VENCEU")
