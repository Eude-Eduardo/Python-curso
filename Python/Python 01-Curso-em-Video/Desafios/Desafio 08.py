print("=======Conversor de Medidas=======")
med = float(input("Quantos metros?"))
km = med/1000
hm = med/100
dm = med/10
cm = med*100
mm = med*1000

print("{}M são {}Km".format(med, km))
print("{}M são {}Dm".format(med, hm))
print("{}M são {}Dm".format(med, dm))
print("{}M são {}Cm".format(med, cm))
print("{}M são {}Mm".format(med, mm))

