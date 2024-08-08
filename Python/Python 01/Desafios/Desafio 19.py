from random import choice

#meu jeito

alunos = [input("Qual o primeiro aluno: "),input("Segundo aluno: "),input("Terceiro aluno: "), input("Quarto aluno: ")]

print("O vencedor do sorteio foi {}".format(choice(alunos)))

#jeito da aula

n1 = str(input("Aluno 1:"))
n2 = str(input("Aluno 2:"))
n3 = str(input("Aluno 3:"))
n4 = str(input("Aluno 4"))
list = [n1, n2, n3, n4]

print
