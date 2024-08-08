from datetime import date

dia = int(input("Qual seu de dia de nascimento?"))
mes = int(input("Qual seu de mês de nascimento?"))
ano = int(input("Qual seu de ano de nascimento?"))

atualA = date.today().year
atualM = date.today().month
atualD = date.today().day

if mes < atualM:
    idade = atualA - ano
elif dia <= atualD: 
    idade = (atualA - ano)-1
else:
    idade = (atualA - ano)-1



if idade == 18:
    print(f"Está na hora de se alistar nas forças armardas IMEDIATAMENTE")
elif idade > 18:
    print(f"Você tem {idade} e já passou do tempo de alistamento por {abs(idade - 18)} anos")
    print(f"Seu alistamento foi no ano de {abs((idade - 18) - atualA)}")
else:
    print(f"Você tem {idade} e faltam {abs(idade-18)} anos para o alistamento militar obrigatório")
    print(f"Deverá se alistar no ano de {abs((idade-18)- atualA)} ")