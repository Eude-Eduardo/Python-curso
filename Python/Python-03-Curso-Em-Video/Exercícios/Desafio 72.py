extenso = ("zero", 'um', "dois", "três", "quatro",
            "cinco", "seis", "sete", "oito", "nove", 
            "dez", "onze", "doze", "treze","quatorze", 
            "quinze", "dezesseis", "dezessete", "dezoito", 
            "dezenove", "vinte")
while True:
    num = int(input("Digite um número entre 0 e 20: "))
    while num < 0 or num > 20:
        num = int(input("Tente novamente.Digite um número entre 0 e 20: "))
    print(f"Você digitou o número {extenso[num]}.")
    print("=="*20)
    opc = ""
    while opc != "S" and opc != "N":
        opc = str(input("Quer continuar? [S/N]")).strip().upper()[0]
    if opc == "N":
        break
print("{:=^40}".format("Fim do Programa"))