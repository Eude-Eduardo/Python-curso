jogador = {}
partidas = []
time = []

while True:
    jogador.clear()
    jogador["Nome"] = str(input("Nome do jogador: "))
    tot = int(input(f"Quantas partidas {jogador['Nome'].capitalize()} jogou? "))
    partidas.clear()
    for c in range(1, tot+1):
        partidas.append(int(input(f"   Quantos gols na partida {c}? ")))
    jogador["Gols"] = partidas[:]
    jogador["Total"] = sum(partidas)
    time.append(jogador.copy())
    while True:
        res = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]
        if res in "SN":
            break
        print("Erro! Responda apenas S ou N")
    if res == "N":
        break
print("-=" * 25)
print("Cod ", end="")
for i in jogador.keys():
    print(f"{i:<15}", end="")
print()
print("-=" * 25)
for k, v in enumerate(time):
    print(f"{k:>4} ", end="")
    for d in v.values():
        print(f"{str(d):<15}", end=" ")
    print()
print("-=" * 25)
while True:
    busca = int(input("Mostrar dados de qual jogador? (999 para parar) "))
    if busca == 999:
        break
    if busca >= len(time):
        print(f"ERRO! não existe jogador com {busca}")
    else:
        print(f" -- LEVANTAMENTO DO JOGADOR {time[busca]["Nome"].capitalize()}")
        for i, g in enumerate(time[busca]["Gols"]):
            print(f"    No jogo {i+1} fez {g} gols")
    print("-=" * 25)
print("<< Volte sempre >>")
    