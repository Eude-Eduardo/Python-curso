num = int(input('Digite um número e vou analisar se ele é primo ou composto: '))
result = ''
lista = 0
for verific in range(2, num + 1):
    if num % verific == 0:
        lista += verific
        print(lista)
        if lista > num:
            result = 'NÃO É PRIMO! E sim COMPOSTO!'
        elif lista == num:
            result = 'É PRIMO!'
if num == 1:
    print('O número "1" é engraçado! Ele não é primo nem composto!')
else:
    print(f'O número "{num}" {result}')