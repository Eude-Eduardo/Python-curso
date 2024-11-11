jogadores = list()
temp = {}
while True:
    temp["Nome"] = str(input("Nome: "))
    temp["Gols"] = list()
    partidas = int(input(f"Quantas partidas {temp['Nome'].capitalize()} jogou? "))
    for c in range(1, partidas+1):
        temp["Gols"].append(int(input(f"""   Quantos gols {temp['Nome'].capitalize()} fez na partida {c}? """)))
        temp["Total"] = sum(temp['Gols'])   
    jogadores.append(temp.copy())
    temp.clear()
    res = str(input("Quer continuar [S/N]: ")).strip().upper()
    while res != "N" and res != "S":
        res = str(input("Erro! Digite apenas S ou N: ")).strip().upper()
    print("--"*20)
    if res in "Nn":
        break
print("Cod", end=" ")
for k in jogadores[0].keys():
        print(f"{k:<15}", end="")
print()
print("--" * 20)
for p, i in enumerate(jogadores):
    print(f"{p:<4}", end="")
    for l in i.values():
        print(f"{str(l):<15}", end="")
    print()
cont = 1
while True: 
    resp = int(input("Que dados de jogador gostaria de ver? (999 para parar): "))
    if resp == 999:
        break
    if resp <= len(jogadores)- 1:
        print(f"-- Levantamento do jogador {jogadores[resp]["Nome"]}")
        for i in jogadores[resp]["Gols"]:
            print(f"""   No jogo {cont} fez {i}""", "Gol." if i == 1 else "Gols.")
            cont += 1
        cont = 1
    elif resp > len(jogadores) -1:
        print(f"Erro! não existe Jogador com o código {resp}.")
print("<<< VOLTE SEMPRE >>>")