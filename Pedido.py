class Pedido:
    __dniRepartidor=0
    __numeroPedido=0
    __direccion=''
    __dia=0
    __mes=4
    __anio=2020
    __importeEnvio=0.0

    def __init__(self, dniRepartidor, numeroPedido, direccion,dia, mes, anio, importeEnvio):
        self.__dniRepartidor = dniRepartidor
        self.__numeroPedido = numeroPedido
        self.__direccion = direccion
        self.__dia = dia
        self.__mes = mes
        self.__anio = anio
        self.__importeEnvio = importeEnvio

    def getImporteEnvio(self):
        return self.__importeEnvio
    def getDniRepartidor(self):
        return self.__dniRepartidor
    def getNumeroPedido(self):
        return self.__numeroPedido
    def getDia(self):
        return self.__dia
    def getMes(self):
        return self.__mes
    def getAnio(self):
        return self.__anio
    def getDireccion(self):
        return self.__direccion

    def __str__(self):
        cadena ='%02d/%02d/%4d %12d %16.2f' % (self.__dia,self.__mes,self.__anio,self.__numeroPedido,self.__importeEnvio)
        return cadena
