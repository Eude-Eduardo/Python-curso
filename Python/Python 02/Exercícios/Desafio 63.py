num = int(input("Quantos termos vai querer? "))
i = 0
ant = 0
atual = 1
prox = 1
while i < num:
    print(f"{atual}")
    prox = ant + atual
    ant = atual
    atual = prox
    i += 1
    