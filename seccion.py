class Seccion:
    def __init__(self, categoria, numero):
        self.__categoria = categoria
        self.__numero = numero

    def get_categoria(self):
        return self.__categoria

    def set_categoria(self, value):
        self.__categoria = value

    def get_numero(self):
        return self.__numero

    def set_numero(self, value):
        self.__numero = value
