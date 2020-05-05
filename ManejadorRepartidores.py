import csv
from Repartidor import Repartidor

class ManejadorRepartidores:
    __repartidores=[]

    def __init__(self):
        self.__repartidores = []

    def cargarRepartidores(self):
        archivo = open('Repartidores.csv')
        reader = csv.reader(archivo,delimiter=',')
        for fila in reader:
            dni = int(fila[0])
            nom = str(fila[1])
            apellido = str(fila[2])
            dia = int(fila[3])
            mes = int(fila[4])
            anio = int(fila[5])
            unRepartidor = Repartidor(dni,nom,apellido,dia,mes,anio)
            self.__repartidores.append(unRepartidor)
        archivo.close()
        return self.__repartidores

    def __str__(self):
        cadena = 'Repartidores:\n'
        cadena += '------------\n'
        for i in range(len(self.__repartidores)):
            cadena += str(self.__repartidores[i].mostrarDatos())
        return cadena

