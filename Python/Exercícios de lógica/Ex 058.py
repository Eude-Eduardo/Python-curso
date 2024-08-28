# Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível

num = int(input("Digite um número para saber se ele é primo: "))
primo = 0
if num == 1:
    print("o número 1 não é composto e nem considerado um número primo")
else:
    for c in range(1 , num+1):
        if num % c == 0:
            primo += 1
        if primo == 2:
            res = f"é primo."
        else:
            res = f"não é primo e é divisível por"

    print(f"O número {num} {res}", end= " ")  
    
    for c in range(1 , num+1):
        if num % c == 0:
            if res == f"é primo.":
                continue
            else:
                n = num/c
                print(f"{n:.0f}" , end=", "if n != 1 else ".") 

        

        
        
    
