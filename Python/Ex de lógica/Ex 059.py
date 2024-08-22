# Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.
num = 12
primos = 0
primo = 0
for i in range(1, num+1):
    for c in range(1, i+1):
        primo = 0
        if i % c == 0:
            primo += 1
        if primo == 2:
            primos = i
            print(f"{primos}===")
        else:
            composto = i
            # print(f"{composto}---")


    