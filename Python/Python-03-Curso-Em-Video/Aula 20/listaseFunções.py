def dobra(lst):
    dobro = []
    for i in lst:
        dobro.append(i*2)     
    print(dobro)
"""def dobra(lst): # Tudo que acontecer com o "lst" interfere diretemanete na lista valores
    pos = 0
    dobro = []
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
"""

valores = [7, 2 ,5, 0, 4]
dobra(valores)
print(valores)