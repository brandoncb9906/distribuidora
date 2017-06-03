from bodega import Bodega

class BodegaAlquilada(Bodega):
    def __init__(self, numero, nombre, divisa, mensualidad):
        Bodega.__init__(numero, nombre)
        self.__divisa = divisa
        self.__mensualidad = mensualidad

    def get_divisa(self):
        return self.__divisa()

    def set_divisa(self, value):
        self.__divisa = value

    def get_mensualidad(self):
        return self.__mensualidad

    def set_mensualidad(self, value):
        self.__mensualidad = value
