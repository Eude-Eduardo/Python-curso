from random import randint
from time import sleep

dados = {
    "Jogador 1": randint(1, 6),
    "Jogador 2": randint(1, 6),
    "Jogador 3": randint(1, 6),
    "Jogador 4": randint(1, 6)}

cont = 1
print("Os Valores Sorteados:")
for j, d in dados.items():
    print(f"""   O {j} tirou {d}""")
print("-=-"*10)
print("Ranking dos Jogadores:")
for d in sorted(dados.values(), reverse=True):
    for j, c in dados.items(): 
        if d == c:
            print(f"""   {cont}º lugar: {j} com {c}""")
            del(dados[j])
            break
    cont += 1