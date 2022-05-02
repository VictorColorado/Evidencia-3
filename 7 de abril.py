import csv

class Contacto:
    def __init__(self,Usuario,Nombre,Correo):
        self.Usuario = Usuario
        self.Nombre = Nombre
        self.Correo = Correo
Contactos = []

with open('contactos.csv',newline='')as archivo_csv:
    lector_csv = csv.reader(archivo_csv, delimiter='|')
    for e in lector_csv:
        Contactos.append(Contacto(e[0],e[1],e[2]))
        
for o in Contactos:
    print(o.Usuario)
    print(o.Nombre)
    print(o.Correo)