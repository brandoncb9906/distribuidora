class Bodega:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__secciones = []

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, value):
        self.__nombre = value

    def get_secciones(self):
        return self.__secciones

    def add_seccion(self, seccion):
        self.__secciones.append(seccion)