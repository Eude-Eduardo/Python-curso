from time import sleep
n1 = 0
count = 0
for c in range(1, 501, 2):
    if c % 2 != 0: 
        if c % 3 == 0:
            count += 1
            n1 += c
            
            
print(f"O valor de todos os {count} números somados é {n1}")
