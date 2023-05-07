class PlanAhorro:
    cantcuotas = 60
    cuotaslicitar = 10
    def __init__ (self, codigo, modelo, version , valor):
        self.__codigo = codigo
        self.__modelo = modelo
        self.__version = version
        self.__valor = valor


    def retornacodigo(self):
        return self.__codigo
    
    def retornamodelo(self):
        return self.__modelo
    
    def retornaversion(self):
        return self.__version
   
    def retornavalor(self):
        return self.__valor
    @classmethod
    def retornacuotaslicitar (cls):
        return cls.cuotaslicitar
 
    def modificarvalor (self, nuevovalor):
        self.__valor = nuevovalor




