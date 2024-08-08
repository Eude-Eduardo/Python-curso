print("---"*6)
print("Qual o seu gênero?")
print("---"*6)
print("""[F] Feminino
[M] Masculino""")
sexo = str(input(""))

if sexo.lower() == "f":
    print("Seu sexo é feminino")
elif sexo.lower() == "m":
    print("Seu sexo é masculino")
else:
    print("Sexo inválido")