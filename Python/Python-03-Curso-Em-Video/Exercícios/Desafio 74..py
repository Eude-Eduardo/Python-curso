from random import randint
num = (randint(1,9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9))
print("Os números sorteados foram: ", end=" ")
for c in num:
    print(c, end=" ")
print(f"\nO maior número sorteado foi: {max(num)} ")
print(f"O menor número sorteado foi: {min(num)}")
