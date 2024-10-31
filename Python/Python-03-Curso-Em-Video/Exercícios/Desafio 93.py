jogador = {"Nome": (input("Nome: "))}
jogador["Gols"] = list()
partidas = int(input(f"Quantas partidas {jogador['Nome']} jogou? "))
for c in range(1, partidas+1):
    jogador["Gols"].append(int(input(f"Quantos gols na partida {c}? ")))
jogador["Total"] = sum(jogador["Gols"])
print("-=" *20)
print(jogador)
print("-=" *20)
for k, v in jogador.items():
    print(f"O campo {k} tem o valor {v}")
print("-=" *20)
cont = 1
print(f"O jogador {jogador['Nome']} 5 partidas:")
for i in jogador["Gols"]:
    print(f"""   => Na partida {cont}, fez {i} Gols""")
    cont += 1
print(f"Fez um total de {jogador['Total']} Gols")
print("-=" *20)

