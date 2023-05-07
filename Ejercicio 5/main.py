from menu import Menu
from planahorro import PlanAhorro
from controlador import ControladorPlanes as CP
def test():
    controlador = CP()
    controlador.cargardatos()
    print('LISTA CARGADA')
    menu = Menu()
    menu.opciones(controlador)
if __name__ == '__main__':
    test()