precios =(50, 75, 46, 22, 80, 65, 8)
minimo = maximo = precios[0]
for precios in precios:
    if precios < minimo:
        minimo = precios
    elif precios > maximo:
        maximo = precios
        
print ("El precio minimo es " + str(minimo))
print ("El precio maximo es " + str(maximo))

    
    
    
    
    
    
    