from ManejadorPedidos import ManejadorPedidos
from ManejadorRepartidores import ManejadorRepartidores

if __name__=='__main__':

    ListaPedidos = ManejadorPedidos()
    ListaRepartidores = ManejadorRepartidores()

    lista1 =[]
    lista1=ListaRepartidores.cargarRepartidores()
    lista2=[]
    lista2=ListaPedidos.cargarPedidos()

    #Inciso 1
    dni =  int(input('Ingrese DNI de repartidor: '))
    i=0
    while i < 5:
        if dni == lista1[i].getDniRepartidor():
            print(lista1[i])
            i+=5
        i+=1
    print('Fecha         Numero de pedido  Costo del envio')
    for i, pedido in enumerate(lista2):
        if dni == pedido.getDniRepartidor():
            print(pedido)
    print('Total: {:33}\n'.format(ListaPedidos.pedidosPorRepartidor(dni)))

    #Inciso2
    print('Monto a pagar a cada repartidor')
    for i, rep in enumerate(lista1):
        print(rep)
        envios=ListaPedidos.pedidosPorRepartidor(rep.getDniRepartidor())
        anti=rep.calcularAntiguedad()*100
        tot = anti +envios
        print('Envios: $ {:.2f}   Antiguedad: $ {:.2f}   Total: $ {:.2f}\n'.format(envios,anti,tot))

    #Inciso3
    lista1 = lista1>0

    #Inciso4
    dia=int(input('Ingrese dia para conocer los pedidos: '))
    for i, pedido in enumerate(lista2):
        if pedido.getDia() == dia:
            for j, rep in enumerate(lista1):
                if pedido.getDniRepartidor()==rep.getDniRepartidor():
                    print('Repartidor: '+rep.getNombre()+' '+rep.getApellido())
            print('Numero de Pedido: {}'.format(pedido.getNumeroPedido()))

