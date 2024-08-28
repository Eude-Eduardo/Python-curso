# Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.
num = int(input("digite um número: "))
div = 0
print(f"Os primos de 1 a {num} são: ", end="")
for c in range(2, num+1):
    primo = True
    for i in range (2, c):
        div += 1
        if c % i == 0:
            primo = False
            break 

    if primo:
        print(f"{c}", end=" ")
print(f"\nForam efetuadas {div} divisões")





    