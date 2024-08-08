n = int(input("Digite um número:"))
print("Para qual base vai ser convertido?")
print("""1 - binário
2 - Octal
3 - Hexadecimal""")
esc = int(input("Sua Opção: "))

if esc == 1:
    bi = bin(n)
    print(f"O número {n} em base binária é {bi[2:]}")
elif esc == 2:
    oc = oct(n)
    print(f"O número {n} em base Octal é {oc[2:]}")
elif esc == 3:
    he = hex(n)
    print(f"O número {n} em base hexadecimal é {he[2:]}")
else:
    print("Por favor escolha um valor válido")



