# 20 .Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.
while True:
    num = 0
    while num < 1 or num >= 16 and num != 99:
        num = int(input('Qual número vai querer saber o fatorial [de 1 a 16]? (99 cancelar): '))
    if num == 99:
        print("=="*10, end="")
        print(f"{"FIM DO PROGRAMA":^10}", end="")
        print("=="*10)
        break
    print("="*20)
    n = num
    for c in range (2, num):
        n *= c
    print(f"{num}! (Faotorial) é igual a {n}")
    print("="*20)
    

