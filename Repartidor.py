class Repartidor:
    __dniRepartidor=0
    __nombre=''
    __apellido=''
    __dia=0
    __mes=4
    __anio=2020

    def __init__(self, dniRepartidor,nombre,apellido,dia=1,mes=4,año=2020):
        self.__dniRepartidor = dniRepartidor
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dia = dia
        self.__mes = mes
        self.__anio = año

    def getDniRepartidor(self):
        return self.__dniRepartidor
    def getNombre(self):
        return self.__nombre
    def getApellido(self):
        return self.__apellido
    def getDia(self):
        return self.__dia
    def getMes(self):
        return self.__mes
    def getAnio(self):
        return self.__anio

    def mostrarDatos(self):
        return'%8s %10s %10d  %02d/%02d/%4d\n'%(self.__apellido,self.__nombre,self.__dniRepartidor,self.__dia,self.__mes,self.__anio)

    def calcularAntiguedad(self):
        dia = 5
        mes =5
        anio=2020
        if dia < self.__dia:
            mes-=1
        if mes < self.__mes:
            mes += 12
            anio -=1
        m = mes-self.__mes
        a = anio - self.__anio
        meses = 12*a + m
        return meses

    def __gt__(self):
        pass

    def __str__(self):
        return "Repartidor: %s\nDNI: %s" % (self.__nombre+" "+self.__apellido,self.__dniRepartidor)

