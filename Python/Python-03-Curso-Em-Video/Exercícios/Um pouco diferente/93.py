jogador = {}
partidas = []
jogador["Nome"] = str(input("Nome do jogador: "))
tot = int(input(f"Quantas partidas {jogador['Nome']} jogou? "))
for c in range(1, tot+1):
    partidas.append(int(input(f"   Quantos gols na partida {c}? ")))
jogador["Gols"] = partidas[:]
jogador["Total"] = sum(partidas)
print("-=" * 30)
print(jogador)
print("-=" * 30)
for k, v in jogador.items():
    print(f"O campo {k} tem valor {v}")
print("-=" * 30)
print(f"O jogador {jogador['Nome']} jogou {len(jogador['Gols'])}")
for i, v in enumerate(jogador["Gols"]):
    print(f"   => Na partida {i}, fez {v} gols")
print(f"Foi um total de {jogador['Total']} gols")