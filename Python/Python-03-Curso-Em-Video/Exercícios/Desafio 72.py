num = int(input("Digite um número entre 0 e 20: "))
extenso = ("zero", 'um', "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")
while num < 0 or num > 20:
    num = int(input("Tente Novamente. Digite um número entre 0 e 20: "))

print(f"Você digitou o número {extenso[num]}.")