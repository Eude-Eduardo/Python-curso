aluno = dict()
aluno["Nome"] = str(input("Nome: "))
aluno["Media"] = float(input(f"Média de {aluno['Nome']}: "))
if aluno["Media"] >= 7:
    aluno["Situação"] = "Aprovado"
elif 5 <= aluno["Media"] < 7:
    aluno["Situação"] = "Recuperação"
else:
    aluno["Situação"] = "Reprovado"
print("-=" * 20)
for k, v in aluno.items():
    print(f"  - {k} é igual a {v}")
print("-=" * 20)