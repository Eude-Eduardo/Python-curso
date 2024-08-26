# Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.
"""num = 16
primo = 0
p = 0
i = 0
c = 1
while i != num+1:
    i+=1
    base = i+1
    for c in range(1, base):
        if i % c == 0:
            primo += 1
            if primo > 2:
                print(f"{i} não é")
                continue
            elif primo == 2:
                print(f"{i} é primo")
                primo= 0"""

# Solicita ao usuário um número inteiro N
N = int(input("Digite um número inteiro: "))

# Inicializa a contagem de divisões
divisoes = 0
pr = 0
# Itera sobre todos os números de 2 até N
for num in range(2, N + 1):
    # Assume que o número é primo
    primo = True
    
    # Verifica se o número é divisível por algum número entre 2 e num-1
    for i in range(1, num):
        divisoes += 1
        if num % i == 0:
            primo = False
        
            break
    
    # Se o número for primo, imprime-o
    if primo:
        print(num)

# Exibe o número total de divisões realizadas
print("Número total de divisões realizadas:", divisoes)






    