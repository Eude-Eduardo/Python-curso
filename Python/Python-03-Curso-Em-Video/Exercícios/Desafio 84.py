dados = list()
idadePeso = list()
res = 0
maiorMenor = list()
nomeMaior = list()
nomeMenor = list()
while True:
    idadePeso.append(str(input("Nome: ")))
    idadePeso.append(float(input("Peso: ")))
    dados.append(idadePeso[:])
    idadePeso.clear()
    res = ""
    while res != "S" and res != "N":
        res = str(input("Quer continuar? [S/N]" )).strip().upper()[0]
    if res == "N":
        break
print("-="*30)
print(f"Você digitou {len(dados)} nomes")
for pessoa in dados:
    for pos,c in enumerate(pessoa):
        if pos % 2 == 1:
            maiorMenor.append(c)
for pessoas in dados:
    for l in pessoas:
        menor = min(maiorMenor)
        maior = max(maiorMenor)            
        if l == maior:
            nomeMaior.append(pessoas[0])
        elif l == menor:
            nomeMenor.append(pessoas[0])
print(f"O maior peso foi de {max(maiorMenor)}Kg. peso de ",end="")
for p,v in enumerate(nomeMaior):
    tam = len(nomeMaior)-1
    print(v, end=" "if p != tam else ".")

print(f"\nO menor peso foi de {min(maiorMenor)}Kg. Peso de ", end="")
for posicao, n in enumerate(nomeMenor):
    t = len(nomeMenor)-1
    print(n, end=" "if posicao != t else ".")


