import random
print("_==_"*10)
print("Pensei em um número de 0 a 5. Tente adivinhhar")
print("_++_"*10)
User = int(input("Em que número eu pensei?"))
correct = random.randrange(0,5)

if(User == correct):
    print("---PARABÉNS VOCÊ ACERTOU---")
else:
    print(f"Errou!!!! o número correto é {correct}")