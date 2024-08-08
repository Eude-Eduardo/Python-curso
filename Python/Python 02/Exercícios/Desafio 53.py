frase = str(input("Digite uma frase: ")).upper()
sem_espaco = frase.replace(" ", "")
invert = sem_espaco[::-1]



if sem_espaco == invert:
    print(f"A frase '{frase}' de trás para frente fica '{invert}'(sem espaços), por isso é um palíndromo")
else:
    print(f'A frase "{frase}" de trás para frente fica "{invert}"')
    print(f'A frase  não é um palindromo')