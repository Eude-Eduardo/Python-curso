alunos = list()
nomes = list()
notas = list()
res = count = 0

while True:
    nomes.append(str(input("Nome: ")))
    notas.append(float(input("Nota 1: ")))
    notas.append(float(input("Nota 2: ")))
    nomes.append(notas[:])
    alunos.append(nomes[:])
    nomes.clear()
    notas.clear()
    res = ""
    count += 1
    while res != "N" and res != "S":
        res = str(input("Quer continuar? [S/N]")).strip().upper()[0]
    if res == 'N':
        break
print(f"{"Nº"}{"Nome":>5}{"Média":>15}")
print("--"*15)
for pos,c in enumerate(alunos):
    print(f"{pos}", end=f"{"":>2}")
    print(f"{c[0]:15}", end=f"")
    print(sum(c[1])/2)
print("--"*15)
resp = 0
while True:
    resp = int(input("Mostrar notas de qual aluno? (999 para interromper): "))
    if resp == 999:
        break
    while resp < 0 or resp > len(alunos)-1:
        resp = int(input("Valor inválido. digite novamente (999 para interromper): "))
        if resp == 999:
            break
    if resp == 999:
        break
    print("--"*20)
    print(f"As notas do aluno {alunos[resp][0].capitalize()} foram {alunos[resp][1]}.")
    print("--"*20)