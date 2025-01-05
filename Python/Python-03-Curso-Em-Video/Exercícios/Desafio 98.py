from time import sleep


def firula():
    print("-=" * 25)


def contador(inicio=None, fim=None, passo=None):
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

    
    inicio = int(input(f"{"Inicio: ":7}"))
    fim = int(input(f"{"Fim: ":7}"))
    passo = int(input(f"{"Passo: ":7}"))
    firula()
    if passo == 0:
        passo = 1
    if passo < 0:
        passo = -passo
    if fim < 0:
        passo = -passo
    print(f"Contando de {inicio} até {fim} de {-passo} em {-passo}:")
    for c in range(inicio, fim+1, passo):
        print(c, end=" ", flush=True)
        sleep(0.4)
    print("Fim")
    firula()

contador()