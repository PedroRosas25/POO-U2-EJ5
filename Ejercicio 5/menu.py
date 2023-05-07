from planahorro import PlanAhorro
from controlador import ControladorPlanes
class Menu:
    def __init__(self):
        self.__opcion = 0
    def opciones (self,lista):
        while self.__opcion != 5:
            print ('''\t    Opcion 1: Actualizar valor de vehiculo de cada plan
            Opcion 2: Mostar datos por vehiculo con valor de cuota inferior
            Opcion 3: Mostar monto para licitar vehiculo
            Opcion 4: Modificar cantidad de cuotas por plan para licitar
            Opcion 5: SALIR ''')
            self.__opcion = int(input('Ingrese una opcion '))
            if self.__opcion == 1:
                print(lista.modificarvalores ())    
            elif self.__opcion == 2:
                valoringresado = input('Ingrese valor de cuota ')
                print(lista.valores(valoringresado))
            elif self.__opcion == 3:
                print(lista.mostrarmontolicitar())
            elif self.__opcion == 4:
                cuotax = input('Ingrese neva cantidad de cuotas para licitar ')
                print(lista.modificarlicitacion(cuotax))
            elif self.__opcion == 5:
                print ('USTED HA SALIDO DEL PROGRAMA')
       
    