import time 
import os

def agenda(): #Este programa sirve para agregar,modificar,eliminar y consultar contactos de 
una agenda
       contactos = {}
       salir=True
       while(salir):
               print('Bienvenido A Mi Agenda\n')
               print('1.) Ver Contactos\n 2.) Agregar Contacto\n 3.) Buscar Contacto\n 4.) Modificar Contacto\n 5.) Eliminar Contacto\n 6.) Salir\n')
              
              opcion=input('Digite el numero de la opcion que desea ver: ')
              #os.system('clear')
              if opcion == '1':
                      for contacto in contactos:
                              for numero in contactos:
                                      print('Contacto / Numero')
                                      print( numero,contactos[contacto])
