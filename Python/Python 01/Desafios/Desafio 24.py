city = str(input('Qual sua cidade?'))
c= city.split()
c2= c[0].lower()

print('A sua cidade é {}'.format(city.strip()))

if(c2.find("santo") == 0  or c2.find('são') == 0):
    print('A sua cidade tem santo na primeira palavra')
else:
    print('Sua cidade não tem santo na primeira palavra')


