from random import randint

lista = list()
jogos = list()
print("-="*20)
print(f"{"MEGA SENA":^40}")
print("-="*20)
quant = int(input("Quantos jogos você quer que eu sorteie? "))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break 
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print("-=" * 5, f"SORTEANDO {quant} JOGOS", "=-" * 5)
for i, l in enumerate(jogos):
    print(f"jogo {i+1}: {l}")
print("-=" * 6, "< BOA SORTE >", "=-" * 6)