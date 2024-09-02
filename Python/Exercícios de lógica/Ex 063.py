# Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.
count = media = soma = quantAlunos = nome = 0
quantTurmas = int(input("Qual a quantidade de turmas: "))
while True:
    str(input("Qual o nome da turma: "))
    quantAlunos = int(input("Quantos alunos tem na turma: "))
    while quantAlunos <= 0 or quantAlunos > 40:
        quantAlunos = int(input("Quantidade de alunos inválida. Digite novamente: "))
    soma += quantAlunos
    print("=="*20)
    count += 1
    if count == quantTurmas:
        break
print(
    f"A média de alunos das {quantTurmas} é {soma/quantTurmas}"
    )