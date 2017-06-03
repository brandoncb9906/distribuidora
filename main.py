lista_productos = []
lista_categorias = []
lista_bodegas = []

def main_menu():
    print("***Menu***\n",
          "1) Productos\n",
          "2) Categorias\n",
          "3) Bodegas.")
    opcion = input("Digite una opcion: ")
    
    if opcion == "1":
        menu_producto()
    elif opcion == "2":
        menu_categoria()
    elif opcion == "3":
        menu_bodegas()
    else:
        print("Opcion inexistente")
        main_menu()
    
def menu_producto():
    print("***Menu Producto***\n",
          "1) Agregar producto\n",
          "2) Ver producto\n",
          "3) Volver al menu principal.")

    opcion = input("Digite una opcion: ")
    
    if opcion == "1":
        agregar_producto()
        menu_producto()
    elif opcion == "2":
        mostrar_productos()
        menu_producto()
    elif opcion == "3":
        main_menu()
    else:
        print("Opcion inexistente")
        menu_producto()

def menu_categoria():
    print("***Menu Categoria***\n",
          "1) Agregar categoria\n",
          "2) Ver categorias\n",
          "3) Volver al menu principal.")

    opcion = input("Digite una opcion: ")
    
    if opcion == "1":
        agregar_categoria()
        menu_categoria()
    elif opcion == "2":
        mostrar_categorias()
        menu_categoria()
    elif opcion == "3":
        main_menu()
    else:
        print("Opcion inexistente")
        menu_categoria()

def menu_bodegas():
    print("***Menu Bodegas***\n",
          "1) Agregar bodega\n",
          "2) Ver bodega\n",
          "3) Volver al menu principal.")

    opcion = input("Digite una opcion: ")
    
    if opcion == "1":
        tipo = input("Propia (p) o alquilada (a): ")
        if tipo == "p":
            agregar_bodega()
        elif tipo == "a":
            agregar_bodega_alquilada()
        menu_bodegas()

    elif opcion == "2":
        mostrar_bodegas()
        numero_bodega = input("Indique el numero de bodega: ")
        bodega = buscar_bodega(numero_bodega)
        if bodega is None:
            print("No se encontro la bodega indicada")
            menu_bodegas()
        menu_bodega(bodega)
    elif opcion == "3":
        main_menu()
    else:
        print("Opcion inexistente")
        menu_bodegas()
    
def menu_bodega(bodega):
    print("***Menu Bodega***\n",
          "1) Agregar seccion\n",
          "2) Ver secciones\n",
          "3) Volver al menu bodegas.")

    opcion = input("Digite una opcion: ")
    
    if opcion == "1":
        seccion = agregar_seccion()
        bodega.add_seccion(seccion)
        menu_bodega(bodega)
    elif opcion == "2":
        secciones = bodega.get_secciones()
        for seccion in secciones:
            print(seccion.get_numero())
        menu_bodega(bodega)
    elif opcion == "3":
        menu_bodegas()
    else:
        print("Opcion inexistente")
        menu_bodega(bodega)
    

# Metodos de mostrar
def mostrar_productos():
    for producto in lista_productos:
        print(producto.get_nombre())

def mostrar_categorias():
    for categoria in lista_categorias:
        print(categoria.get_nombre())

def mostrar_bodegas():
    for bodega in lista_bodegas:
        print(bodega.get_nombre())

# Busquedas
def buscar_categoria(nombre):
    for categoria in lista_categorias:
        if nombre == categoria.get_nombre():
            return categoria
    return None

def buscar_bodega(nombre):
    for bodega in lista_bodegas:
        if nombre == bodega.get_nombre():
            return bodega
    return None

def buscar_seccion(numero, bodega):
    for seccion in bodega.get_secciones():
        if seccion.get_numero() == numero:
            return seccion
    return None

def agregar_producto():
    nombre = input("Nombre: ")
    nombre_categoria = input("Categoria: ")
    categoria = buscar_categoria(nombre_categoria)
    if categoria is None:
        print("La categoria no existe")
        return
    cantidad = input("Cantidad: ")
    nombre_seccion = input("Seccion: ")
    
    # nombre_seccion tiene formato "bodega1-2"
    # donde bodega1 es el nombre de la bodega
    # y 2 es el numero de seccion
    partes = nombre_seccion.split("-")
    nombre_bodega = partes[0]
    numero_seccion = partes[1]
    
    bodega = buscar_bodega(nombre_bodega)
    if bodega is None:
        print("No se encontro la bodega")
        return
    
    seccion = buscar_seccion(numero_seccion, bodega)
    if seccion is None:
        print("No se encontro la seccion en la bodega")
        return
    
    producto = Producto(nombre, categoria, cantidad, seccion)
    lista_productos.append(producto)
    
def agregar_categoria():
    nombre = input("Nombre: ")
    categoria = Categoria(nombre)
    lista_categorias.append(categoria)

def agregar_bodega():
    nombre = input("Nombre: ")
    bodega = Bodega(nombre)
    lista_bodegas.append(bodega)

def agregar_bodega_alquilada():
    nombre = input("Nombre: ")
    divisa = input("Divisa: ")
    mensualidad = input("Mensualidad: ")
    bodega = BodegaAlquilada(nombre, divisa, mensualidad)
    lista_bodegas.append(bodega)

def agregar_seccion():
    numero = input("Numero: ")
    nombre_categoria = input("Categoria: ")

    categoria = buscar_categoria(nombre_categoria)
    if categoria is None:
        print("No se encontro la categoria")
        return

    seccion = Seccion(categoria, numero)
    return seccion

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


class Categoria:
    def __init__(self, nombre):
        self.__nombre = nombre
        
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, value):
        self.__nombre = value


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

# Datos iniciales
abarrotes = Categoria("Abarrotes")
electrodomesticos = Categoria("Electrodomesticos")
ropa = Categoria("Ropa")
lista_categorias.append(abarrotes)
lista_categorias.append(electrodomesticos)
lista_categorias.append(ropa)
    
main_menu()