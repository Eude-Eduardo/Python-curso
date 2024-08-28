# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';
nome = str(input("Seu nome: ")).strip()
idade = int(input("sua idade: ")) 
salario = float(input("seu salário: R$"))
sexo = str(input("Seu sexo [F/M]: ")).upper()[0].strip()
estadoCivil =str(input("Seu Estado civil: ")).strip().upper()[0]

while not any(carac in "SCVD" for carac in estadoCivil) or len(nome) <= 2 or (idade < 0 and idade > 150) or salario <= 0 or (sexo != "F" and sexo != "M"):
    if len(nome) <= 2:
        nome = str(input("Nome muito curto! Digite novamente: ")).strip
    elif idade < 0 or idade > 150:
        idade = int(input("Idade inválida! Digite novamente: "))
    elif salario <=0:
        salario = float(input("Salário inválido! Digite novamente: R$"))
    elif sexo != "F" and sexo != "M":
        sexo = str(input("Sexo inválido! Digite [F/M]: ")).strip().upper()[0]
    elif not any(carac in "SCVD" for carac in estadoCivil):
        estadoCivil = str(input("Estado civil inválido! Seu estado civil: ")).strip().upper()[0]
    else:
        print(f"Olá {nome.capitalize()}")

print(f"Olá {nome.capitalize()} você foi registrado com sucesso!")