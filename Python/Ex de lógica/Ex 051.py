# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo
print("=="*20)
print(f"{"Sequencia de Finonacci":^40}")
print("=="*20)
termo = int(input("Qual termo vai querer: "))
anterior = 0
atual = 1
proximo = 1
i = 1
while i < termo:
    proximo = atual + anterior
    anterior = atual
    atual = proximo
    i += 1
print(f"O {termo}º da sequencia de fibonacci é {atual}")
