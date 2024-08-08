# Se o usuário informar o valor de A igual a zero, a equação não é do segundo graue o programa não deve fazer pedir os demais valores,sendo encerrado; 
   
# Se o delta calculado for negativo, a equação não possui raízes reais. Informe ao usuário e encerre o programa;
#Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário; 
# Se o delta for positivo, a equação possui duas raiz reais;informe-as ao usuário;
import math
from operator import neg
a = float(input("Digite o valor de 'a': "))
if a <= 0:
    print('Valor inválido')
else:
    b = float(input("Digite o valor de 'b': "))
    c = float(input("Digite o valor de 'c': "))
    delta = (b**2) - 4 * a * c
    raizD = delta**1/2
    bb = neg(b)
    bh1 = (bb + raizD)/(2 * a)
    bh2 = (bb - raizD)/(2 * a)

    if delta < 0:
        print("Delta tem valor negativo e a equação não tem raizes reais")
    elif delta == 0:
        print(f"X1/X2 = {bh1:.2f}")
    else:
        print(f"X1 = {bh1:.2f}")
        print(f"X2 = {bh2:.2f}")
    

    
        
    
    

