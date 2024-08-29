"""num = [1,2,4,8,3,7]
num.append(8)
num.insert(0,6)
if 5 in num:
    num.remove(5)
print(num)"""
valores = list()
for cont in range(0, 5):
    valores.append(int(input("Digite um valor: ")))

for c, v in enumerate(valores):
    print(f"na posição {c} encontrei {v}...")
print("final da lista")