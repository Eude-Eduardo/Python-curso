# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada.
num = 5
i = 0
while i < 10:
    i += 1
    print(f"{num} x {i:2} = {num*i}")