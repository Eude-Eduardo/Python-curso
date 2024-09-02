#Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de voto de cada candidato.
candidato1 = candidato2 = candidato3 = voto = quantVotos = nulos =0

quantEleitor = int(input("Qual a quantidade de eleitores: "))
while True:
    print(
        "Em quem você irá votar?\n"
        "[10] - Candidato 1\n"
        "[11] - Candidato 2\n"
        "[12] - Candidato 3\n"
        "[99] - anular\n"
        )
    quantVotos += 1
    voto = int(input("Qual o seu voto: ")) 
    while voto != 10 and voto != 11 and voto != 12 and voto != 99:
        voto = int(input("Digite um voto válido: "))
        
    if voto == 10:
        candidato1 += 1
    elif voto == 11:
        candidato2 += 1
    elif voto == 12:
        candidato3 += 1
    elif voto == 99:
        nulos += 1 
    if quantVotos == quantEleitor:
        break
print(
    f"O candidato 1 ficou com {candidato1}\n"
    f"O candidato 2 ficou com {candidato2}\n"
    f"O candidato 3 ficou com {candidato3}\n"
    f"E nulos foram {nulos}"
    )