# A série de Fibonacci é formada pela sequência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500.
anterior = 0
atual = 1
proximo = 1
print(f"{atual}", end="⭢ ")
while anterior <= 500:
    print(f"{atual}", end="⭢ ")
    proximo = anterior + atual
    anterior = atual
    atual = proximo
    if proximo >= 500:
        break
print("Acho que é isso")