from time import sleep

while True:
    num = int(input("Quer ver a tabuada de qual número? "))
    if num < 0:
        break
    print("=="*10)
    for c in range(1,11):
        print(f"{num} x {c:2} = {num*c}")
    print("=="*10)
    sleep(0.5)
print("PROGRAMA TABUADA ENCERRADO. Volte sempre!")
