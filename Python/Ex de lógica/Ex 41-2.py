"""Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação."""

print("Tempo para passar a população")
habA = int(input("Qual a população da cidade A: "))
habB = int(input("Qual a polulação da cidade B: "))
taxaA = float(input("Taxa de crescimento da cidade A (por ano): "))
taxaB = float(input("taxa de crescimento da cidade B (por ano): "))
cont = 0
while habA <= 0 and habB <= 0:
    habA = int(input("Poucos habitantes digite novamento a população da cidade A: "))
    habB = int(input("Poucos habitantes digite novamento a população da cidade B: "))

if habA > habB:
    while taxaA >= taxaB:
        taxaA = float(input("Cidade 'A' com mais população também tem uma taxa de crescimento maior ou igual, digite de novo: "))
        taxaB = float(input("Cidade 'B' com menos polupação tem uma taxa mais baixa ou igual impossivel fazer a conta, digite de novo: "))
    taxaA = taxaA/100
    taxaB = taxaB/100
    while habB < habA:
        habA += habA * taxaA
        habB += habB * taxaB
        cont += 1

    print(f"Serão necessários {cont} para a cidade B ultrapassar a cidade A em população")
elif habA == habB:
    print("As populações são iguais")
else:
    while taxaB >= taxaA:
        taxaA = float(input("Cidade 'B' com mais população também tem uma taxa de crescimento maior ou igual, digite de novo: "))
        taxaB = float(input("Cidade 'A' com menos polupação tem uma taxa mais baixa ou igual impossivel fazer a conta, digite de novo: "))
    taxaA = taxaA/100
    taxaB = taxaB/100
    while habA < habB:
        habA += habA * taxaA
        habB += habB * taxaB
        cont += 1
    print(f"Serão necessarios {cont} para cidade A ultrapassar a cidade B em população")
