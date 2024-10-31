aluno = {}
aluno["Nome"] = str(input("Nome: "))
aluno["Média"] = float(input(f"Média de {aluno["Nome"]}: "))

if 5.5 <= aluno["Média"] < 7:
    result = "recuperação"
elif aluno["Média"] < 5.5:
    result = "reprovado"
elif aluno["Média"] >= 7:
    result = "aprovado"
for a, m in aluno.items():
    print(f"{a} é igual a {m}.")
print(f"A situação é igual a {result}.")