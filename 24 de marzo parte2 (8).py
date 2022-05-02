palabra = input("palabra:" )
lista = []
while palabra != "OK":
    lista.append(palabra)
    palabra = input("palabra:" )
    
buscar = input("palabra a buscar:" )
print ("la encontre %d veces"% lista.count(buscar))
