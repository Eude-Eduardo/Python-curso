lista = []
for c in range(0, 5):
    num = int(input("Digite um valor: "))
    if c == 0 or num > lista[-1]:
        lista.append(num)
        res = lista.index(num)
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos,num)
                res = lista.index(num)
                break
            pos += 1
    print(f"o número {num} foi inserido na posição {res}...")
print(f"{lista}")