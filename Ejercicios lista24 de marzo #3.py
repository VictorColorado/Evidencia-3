alumnos = {}
cantidad = int(input("Introduce la cantidad de alumnos que vamos a guardar:"))
for num in range(cantidad):
    alumno = input("Nombre del alumno:")
    while alumno in alumnos:
        print("Alumno ya existe.")
        alumno = input("Nombre del alumno:")
    notas=[]
    nota = int(input("Dame una nota del alumno(Negativo para terminar):"))
    while nota > 0:
        notas.append(nota)
        nota = int (input("Dame una nota del alumono (Negativo para terminar):"))
    alumnos[alumno] = notas.copy()
    
for alumno, notas in alumnos.items():
    print("%s ha sacado de nota media %f" % (alumno,sum(notas)/len(notas)))