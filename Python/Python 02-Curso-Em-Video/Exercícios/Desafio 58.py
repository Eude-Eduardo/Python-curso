import random

print("-----Jogo da Adivinhação-----")
print("Tente adivinhar um número de [1/10]")

num = random.randrange(1,10)
player = 0
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
print(f"==={num}===")
print(f"você usou {tentativa} tentativas")
