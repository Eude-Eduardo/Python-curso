print("Gerador de PA")
print("--"*10)
inicio = int(input("Digite o inicio: "))
razão = int(input("Digite a razão: "))
i = 0
num = inicio
cont = 0
while i != 10:
    print(f"{num}", end="-> ")
    num += razão
    i += 1
    cont += 1
    if i == 10:
        print("PARADA")
        res = 1
        c = 1
        while res !=0:
            res = int(input("Quer mais termos? quantos: "))
            c = res
            while c != 0:
                print(f"{num}", end="-> ")
                num += razão
                c -= 1
                cont +=1
                if c == 0:
                    print("PARADA")
    
      
print(f"Finalizada com {cont} termos mostrados")
