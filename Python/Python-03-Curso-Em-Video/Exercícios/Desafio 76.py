from time import sleep

lista = ('Shampoo', 22.19, 
         'Creme', 27.90, 
         'Sabonete', 8.50, 
         'Bucha', 7.00, 
         'Toalha', 10.80, 
         'chuveiro', 75.00)

print("=="*20)
print(f"{"Listagem De Produtos":^40}")
print("=="*20)

for c in range(0, len(lista)):
    if c % 2 == 0:
        print(f"{lista[c]:.<20}", end= f"R$")
    else:
        print(f"{lista[c]:>7.2f}")