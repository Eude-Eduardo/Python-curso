from time import sleep
num = 0
while True:
    num = int(input("Quer ver a tabuada de qual número: "))
    if num < 0:
        break
    print("__"*14)
    print(" ")
    for c in range(1,11):
        print(f"{num} x {c:2} = {num*c}")
    print("__"*14)
    sleep(0.5)
print("PROGRAMA TABUADA ENCERRADO. Volte sempre!")
