from time import sleep


def firula():
    print("-=" * 25)
def contador(inicio, fim, passo):
    firula()
    print("Contando de 1 até 10 de 1 em 1:")
    for a in range(1, 11):
        print(f"{a}", end=" ", flush=True)
        sleep(0.4)
    print("Fim")
    firula()
    print("Contando de 10 até 0 de 2 em 2:")
    for b in range(10, -1, -2):
        print(b, end=" ", flush=True)
        sleep(0.4)
    print("Fim")
    firula()
    print("Agora é a sua vez de personalizar a contagem")

    i = int(input("Inicio: "))
    f = int(input("Fim: "))
    r = int(input("Passo:"))
    inicio = i
    fim = f
    passo = r

    for c in range(inicio, fim, passo):
        print(c, end=" ", flush=True)
        sleep(0.4)
    print("Fim")
    firula()
contador(1, 2, 2)