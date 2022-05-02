from typing import List
import json

class Persona:
    nombre=""
    apellidos=""
    
    def __init__(self, nombre, apellidos):
        self.nombre=nombre
        self.apellidos=apellidos
    
    def muestraInfo(self):
        print("Clase Base")
        print(self.nombre)
        print(self.apellidos)
        
class Estudiante(Persona):
    aniograduacion=0
    def __init__ (self, nombre, apellidos, aniograduacion=2015):
        super().__init__(nombre, apellidos)
        self.aniograduacion=aniograduacion
    
    def muestraInfo(self):
        print("Clase Derivada")
        print(self.nombre)
        print(self.apellidos)
        print(self.aniograduacion)
    
    def derivadoInfo(self):
        print(self.aniograduacion)
        
print("-------------------------------")
unaPersona=Persona("Felipe","Ramirez")
unaPersona.muestraInfo()
print("-------------------------------")
unEstudiante=Estudiante("Alejandro", "Jodorowski")
unEstudiante.aniograduacion=2019
unEstudiante.muestraInfo()
print("-------------------------------")
unEstudiante.derivadoInfo()

Estudiantes=[]
Estudiantes.append(Estudiante("Juan","Hernandez",2022))
Estudiantes.append(Estudiante("Maria","Gomez",2013))
Estudiantes.append(Estudiante("Nidia","Marquez",2021))

print(Estudiantes)
json_data = json.dumps(Estudiantes, default = lambda o: o.__dict__, indent=4)
print(json_data)