from seccion import Seccion
from producto import Producto
from categoria import Categoria
from bodega import Bodega
from bodega_alquilada import BodegaAlquilada

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
    print("\nLista de productos")
    for producto in lista_productos:
        print(producto.get_nombre() + " (" + str(producto.get_cantidad()) + "), " + producto.get_categoria().get_nombre())
    print("\n")

def mostrar_categorias():
    print("\nLista de categorias")
    for categoria in lista_categorias:
        print(categoria.get_nombre())
    print("\n")

def mostrar_bodegas():
    print("\nLista de bodegas")
    for bodega in lista_bodegas:
        print(bodega.get_nombre())
    print("\n")

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

    # La seccion tiene que ser de la misma categoria
    # que el producto que se esta agregando
    if seccion.get_categoria() != categoria:
        print("La categoria de la seccion no concuerda con la del producto.")
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

# Datos iniciales
abarrotes = Categoria("Abarrotes")
electrodomesticos = Categoria("Electrodomesticos")
ropa = Categoria("Ropa")
lista_categorias.append(abarrotes)
lista_categorias.append(electrodomesticos)
lista_categorias.append(ropa)

bodega1 = Bodega("Bodega1")
seccion1 = Seccion(abarrotes, "1")
seccion2 = Seccion(ropa, "2")
bodega1.add_seccion(seccion1)
bodega1.add_seccion(seccion2)

bodega2 = Bodega("Bodega2")
seccion3 = Seccion(electrodomesticos, "3")
seccion4 = Seccion(abarrotes, "4")
bodega2.add_seccion(seccion3)
bodega2.add_seccion(seccion4)

lista_bodegas.append(bodega1)
lista_bodegas.append(bodega2)

agua = Producto("Agua", abarrotes, 10, seccion1)
arroz = Producto("Arroz", abarrotes, 14, seccion1)
camisa = Producto("Camisa", ropa, 18, seccion2)
pantalon = Producto("Pantalon", ropa, 15, seccion2)
cocina = Producto("Cocina", electrodomesticos, 5, seccion3)
refri = Producto("Refri", electrodomesticos, 3, seccion3)
agua2 = Producto("Agua", abarrotes, 18, seccion4)
frijoles = Producto("Frijoles", abarrotes, 19, seccion4)

lista_productos.append(agua)
lista_productos.append(arroz)
lista_productos.append(camisa)
lista_productos.append(pantalon)
lista_productos.append(cocina)
lista_productos.append(refri)
lista_productos.append(agua2)
lista_productos.append(frijoles)


main_menu()