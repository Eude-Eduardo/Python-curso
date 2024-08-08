
#Minha solução

'''nome = str(input("Qual o seu nome completo:")) 
n = nome.replace(" ", '')
ns = nome.split()

print("Todas as letras maiúsculas:{}".format(nome.upper()))
print("Todas minúsculas:{}".format(nome.lower()))
print("Quantas letras(sem considerar espaços):{}".format(len(n)))
print("seu primeiro nome é {} e tem {} letras".format(ns[0], len(ns[0])))'''


#Professor

nome = str(input("Digite seu nome completo:")).strip()

print('analisando seu nome')

print('Seu nome em maúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('seu nome tem ao todo {} letras'.format(len(nome) - nome.count(" ")))
sep=nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(sep[0], len(sep[0])))

