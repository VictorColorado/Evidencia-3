import csv


class Incidente:
    def __init__(self,FECHA,CASOS,MUERTES,PAIS):
        self.FECHA = FECHA
        self.CASOS = CASOS
        self.MUERTES = MUERTES
        self.PAIS = PAIS

with open('AnalisisCOVID.csv') as archivo_csv:
    lector_csv = csv.reader(archivo_csv,delimiter='|')
    contador_lineas = 0
    lista_incidentes = []
    for linea_datos in lector_csv:
        if contador_lineas == 0:
            print(f'Los nombres de columnas son{",".join(linea_datos)}')
        else:
            objeto_temporal = Incidente({linea_datos[0]},{linea_datos[1]},{linea_datos[2]},{linea_datos[3]})
            lista_incidentes.append(objeto_temporal)
            
        contador_lineas +=1
    
    print(f'Procesadas{len(lista_incidentes)}lineas.')