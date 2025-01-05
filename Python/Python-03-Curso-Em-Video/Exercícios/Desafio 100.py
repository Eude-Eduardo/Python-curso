from random import randint
from time import sleep

lista = []

def sorteio():
    print("Sorteando 5 valores da lista: ", end="")
    for c in range(0, 5):
        n = randint(1, 10)
        print(n, end=" ", flush=True)
        sleep(0.5)
        lista.append(n)
    print("PRONTO!")

def somaPar():
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(f"Somando os valores pares de {lista}, temos {soma}")

sorteio()
somaPar()
    