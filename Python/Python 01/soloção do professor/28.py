from random import randint 
from time import sleep
computador = randint(0, 5) 
print("_==_"*15)
print("Vou pensar em um número entre 0 e 5")
print("_==_"*15)
user = int(input("Em que número eu pensei?"))
print("processando...")
sleep(3)
if user == computador:
    print("Você conseguiu me vencer")
else:
    print(f"Eu ganhei!! Eu pensei no número {computador} e não no número {user}")