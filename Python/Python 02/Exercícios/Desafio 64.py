num = 0
n = 0
cont = 0
while num != 999:
    num = int(input("Digite um número [999 para parar]: "))
    if num != 999:
        n += num
        cont += 1
if n == 999:
    print("Você parou o programa")
else:        
    print(f"Você digitou {cont} números e a soma é desses números é igual a {n}")