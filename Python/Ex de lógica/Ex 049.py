# Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.
print("=="*20)
print(f"{"Calculo de potência":^40}")
print("=="*20)
base = int(input("Digite a Base: "))
expoente = int(input("Digite o Expoente: "))
i = 1
resultado = base
while i < expoente:
    resultado *= base
    i+= 1
print("=="*20)
print (f"{base} elevado a {expoente} é {resultado} ")    
