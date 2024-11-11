pessoa = dict()
galera = list()
soma = media = 0
while True:
    pessoa["Nome"] = str(input("Nome: "))
    while True:
        pessoa['Sexo'] = str(input("Sexo: [M/F] ")).upper().strip()
        if pessoa["Sexo"] in "MF":
            break
        print("Erro! Por favor, digite apenas M ou F.")
    pessoa["Idade"] = int(input("Idade: "))
    soma += pessoa["Idade"]
    galera.append(pessoa.copy())
    pessoa.clear()
    while True:
        res = str(input("Quer Continuar? [S/N] ")).strip().upper()
        if res in "SN":
            break
        print("Digite apenas S ou N.")
    if res == "N":
        break
print("-=" *20)
print(f"A) Ao todo temos {len(galera)} pessoas cadastradas.")
media = soma / len(galera)
print(f"B) A média de idade é de {media:5.2f} anos")
print(f"C) As mulheres cadastradas foram: ", end="")
for p in galera:
    if p["Sexo"] in "Ff":
        print(f"{p["Nome"]} ", end="")
print()
print(f"D) Listas das pessoas que estão acima da média: ", end="")
for p in galera:
    if p["Idade"] >= media:
        print()
        for k, v in p.items():
            print(f"{k} = {v}", end="")
print()
print("<< Encerrado >>")