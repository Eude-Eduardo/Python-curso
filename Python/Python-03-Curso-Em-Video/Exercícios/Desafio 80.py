lista = []
for c in range(0, 5):
    num = int(input("Digite um valor: "))
    if c == 0 or num > lista[-1]:
        lista.append(num)
        print("O número foi adicionado no final da lista")
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos,num)
                break
            pos += 1
        print(f"o número {num} foi inserido na posição {lista.index(num)}...")
print(f"Os números ordenados são {lista}")