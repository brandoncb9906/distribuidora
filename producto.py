class Producto:
    def __init__(self, nombre, categoria, cantidad, seccion):
        self.__nombre = nombre
        self.__categoria = categoria
        self.__cantidad = cantidad
        self.__seccion = seccion

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, value):
        self.__nombre = value

    def get_categoria(self):
        return self.__categoria

    def set_categoria(self, value):
        self.__categoria = value

    def get_cantidad(self):
        return self.__cantidad

    def set_cantidad(self, value):
        self.__cantidad = value

    def get_seccion(self):
        return self.__seccion

    def set_seccion(self, value):
        self.__seccion = value
