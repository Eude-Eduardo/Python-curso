import random

#Meu método

"""alunos = [input("Primeiro aluno:"),input("Segundo aluno:"),input("Terceiro aluno:"),input("Quarto aluno:")]

random.shuffle(alunos)

print("A ordem de apresentação é {}".format(alunos))"""

#Aula

n1 = input("Primeiro aluno:")
n2 = input("Segundo aluno:")
n3 = input("Terceiro aluno:")
n4 = input("Quarto aluno:")
list = [n1, n2, n3, n4]

random.shuffle(list)

print("A ordem de apresentação será:")
print(list)

