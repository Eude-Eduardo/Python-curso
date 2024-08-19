print("--==--"*4)
print("Sequencia de Fibonacci")
print("--==--"*4)
num = int(input("Quantos termos vai querer? "))
print("~~"*15)
i = 1
ant = 0
atual = 1
prox = 1
print(0, end=" ⭢ ")
while i < num:
    print(f"{atual}", end=" ⭢ ")
    prox = ant + atual
    ant = atual
    atual = prox
    i += 1
print("Fim")