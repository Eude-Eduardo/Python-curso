matrix = [[],[],[]]
for c in range(0, 3):
    for i in range(0 ,3):
        num = int(input(f"Digite um valor para [{c}, {i}]: "))
        if c == 0: 
            matrix[0].append(num)
        elif c == 1:
            matrix[1].append(num)
        else:
            matrix[2].append(num)
for n in matrix[0]:
    print(f"[ {n:^3} ]", end=" ")
print()
for number in matrix[1]:
    print(f"[ {number:^3} ]", end=" ")
print()
for numero in matrix[2]:
    print(f"[ {numero:^3} ]", end=" ")