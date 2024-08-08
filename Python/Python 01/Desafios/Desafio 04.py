algo = input("Digite algo:")

print("o tipo primitivo desse valor é {}".format(type(algo)))

print('{} é um número? {}'.format(algo, algo.isalnum()))

print("{} só tem espaços? {}".format(algo, algo.isspace()))

print("{} é alfabético? {}".format(algo, algo.isalpha()))

print("{} é alfanumérico? {}".format(algo, algo.isalnum()))

print("{} está em maiúsculas? {}".format(algo, algo.isupper()))

print("{} está em minúsculas? {}".format(algo, algo.isnumeric()))

print("{} Está capitalizada {}".format(algo, algo.istitle()))