# Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
idade = soma = cont = quant = res = 0
while True:
    idade = int(input("Digite sua idade: [0 para anular]"))
    while idade < 0:
        idade = int(input("Idade inválida. Digite sua idade: "))
    soma += idade
    quant += 1
    cont += 1
    if cont == 4:
        res =  ""
        while res != "S" and res != "N":
            res = str(input("Quer adicionar mais idades? [S/N] ")).strip().upper()[0]
        cont = 0
    if res == "N":
        break
media = soma/quant
if media <= 25:
    etaria = "jovem"
elif media < 60:
    etaria = "adulta"
else:
    etaria = "Idosa"
print(f"A turma é {etaria}")