import csv
from Pedido import Pedido

class ManejadorPedidos:
    __pedidos=[]
    __cantidadDias = 30

    def __init__(self):
        self.__pedidos = []
        self.__cantidadDias = 30

    def cargarPedidos(self):
        archivo = open('VentasMensuales.csv')
        reader = csv.reader(archivo,delimiter=',')
        for fila in reader:
            dni = int(fila[0])
            num = int(fila[1])
            dia = int(fila[2])
            mes = int(fila[3])
            anio = int(fila[4])
            direc = str(fila[5])
            monto = float(fila[6])
            unPedido = Pedido(dni,num,direc,dia,mes,anio,monto)
            self.__pedidos.append(unPedido)
        archivo.close()
        return self.__pedidos

    def __str__(self):
        cadena = 'PEDIDOS\nFecha         Numero de pedido  Costo del envio\n'
        for i, pedido in enumerate(self.__pedidos):
            cadena +=(str(pedido))
        return cadena

    def pedidosPorRepartidor(self,dniRepartidor):
        total = 0
        for indice, pedido in enumerate(self.__pedidos):
            if dniRepartidor == pedido.getDniRepartidor():
                total += pedido.getImporteEnvio()
        return total

    def pedidosPorDia(self, dia):
        pass
