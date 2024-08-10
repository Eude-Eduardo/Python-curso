import random
from time import sleep

print("-----Jogo da Adivinhação-----")
print("Tente adivinhar um número entre [1/10]")

num = random.randrange(1,10)
player = 12
tentativa = 0 
while player != num:
    player = int(input("Seu palpite: "))
    if player != num:
        if player > num:
            print("Menos... Tente outra vez")
        else:
            print("Mais... Tente outra vez")
    tentativa += 1 

print("Parabéns o número escolhido foi...")
sleep(0.5)
print(f"==={num}===")
print(f"você usou {tentativa} tentativas")
