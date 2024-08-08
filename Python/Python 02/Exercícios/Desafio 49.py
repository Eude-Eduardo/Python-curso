print("{:=^20}".format("Tabuada"))
n = int(input("Digite um número:"))

for div in range(1, 11):
    print(f"{n} x {div:2} = {n*div}")