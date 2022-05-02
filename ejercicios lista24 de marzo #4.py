numero = int(input("Dime un numero:"))
cuadrados = {}

for num in range(1,numero+1):
    cuadrados[num] = num ** 2
for num, valor in cuadrados.items():
    print("%d -> %d" % (num,valor))