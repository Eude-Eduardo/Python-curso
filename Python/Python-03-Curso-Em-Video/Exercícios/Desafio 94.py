dados = []
temp = {}
soma = []
while True:
    temp["Nome"] = str(input("Nome: ")).strip().capitalize()
    temp["Sexo"] = str(input("Sexo [F/M]: ")).strip().upper()
    temp["Idade"] = int(input("Idade: "))
    soma.append(temp["Idade"]) 
    dados.append(temp.copy())
    temp.clear()
    res = str(input("Quer continuar [S/N]: "))
    if res in "Nn":
        break
print("-=" * 20)
media = sum(soma)/len(dados)
print(f"- O grupo tem {len(dados)} pessoas")
print(f"- A média de idade é {media} anos")
print(f"- As mulheres cadastradas foram:", end=" ")
for pos, c in enumerate(dados):
    for k,v in c.items():
        if k == "Sexo" and v == "F":
            print(dados[pos]["Nome"], end=" ")
print()
print(f"- Lista das pessoas que estão acima da média: ")
for p, c in enumerate(dados):
    for k,v in c.items():
        if k == "Idade" and v > media:
            print(f"Nome = {dados[p]["Nome"]}; Sexo = {dados[p]["Sexo"]}; Idade = {dados[p]["Idade"]}")
            print()
print("<ENCERRADO>")