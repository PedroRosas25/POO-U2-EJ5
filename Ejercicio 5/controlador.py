import csv
from planahorro import PlanAhorro
class ControladorPlanes:
    __listacompleta = []
    def __init__(self):
        __listacompleta = []
    def cargardatos (self):
        archivo = open('planes.csv')
        reader = csv.reader (archivo, delimiter= ';')
        for fila in reader:
                codigo = int(fila[0])
                modelo = str(fila[1])
                version = str(fila[2])
                valor = int (fila[3])
                lista = PlanAhorro(codigo,modelo,version,valor)
                self.__listacompleta.append(lista)
    def modificarvalores (self):
        for i in range (len(self.__listacompleta)):
            print ('Codigo: {} Modelo: {} Version: {}'.format(self.__listacompleta[i].retornacodigo(),self.__listacompleta[i].retornamodelo(),self.__listacompleta[i].retornaversion()))  
            nuevovalor = input ('Ingrese nuevo valor del vehiculo ')  
            self.__listacompleta[i].modificarvalor(nuevovalor)
            print ('Valor modificado = {}'.format(self.__listacompleta[i].retornavalor()))

    def valores(self,valoringresado):
         print ('Lista de los vehiculos que cumplieron la condicion: ')
         for i in range (len(self.__listacompleta)):
              if (((float(self.__listacompleta[i].retornavalor()) / 60) + float(self.__listacompleta[i].retornavalor()*0.10)) < float(valoringresado)):
                    print ('Codigo: {} Modelo: {} Version: {}'.format(self.__listacompleta[i].retornacodigo(),self.__listacompleta[i].retornamodelo(),self.__listacompleta[i].retornaversion()))  

    def mostrarmontolicitar (self):
         for i in range (len(self.__listacompleta)):
            monto = (((float(self.__listacompleta[i].retornavalor() / 60)) + float(self.__listacompleta[i].retornavalor()*0.10)) * float(10))              
            print ('Monto para licitar vehiculo con codigo {}: {}'.format(self.__listacompleta[i].retornacodigo(),round(monto,2)))
    def modificarlicitacion(self, cuotax):
        PlanAhorro.cuotaslicitar = cuotax  
        for i in range (len(self.__listacompleta)):
            print ('Codigo: {} Cuotas para licitar: {}'.format(self.__listacompleta[i].retornacodigo(),self.__listacompleta[i].retornacuotaslicitar()))
            
    