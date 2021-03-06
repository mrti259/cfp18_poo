from .validador import *

class Producto:

    def __init__(self, producto_id=0, nombre="", descripcion="", precio=0, stock=0, categoria_id=0, marca_id=0, fecha_de_publicacion="dd/mm/aaaa", fecha_de_ultima_modificacion="dd/mm/aaaa"):
        '''Inicializa un producto con sus datos provenientes de la base de datos o se crea uno nuevo con los valores por default.'''

        self.producto_id = producto_id
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.categoria_id = categoria_id
        self.marca_id = marca_id
        self.fecha_de_publicacion = fecha_de_publicacion
        self.fecha_de_ultima_modificacion = fecha_de_ultima_modificacion
        self.categoria = None
        self.marca = None



    def __str__(self):
        '''Da formato al objeto para ser pasado como cadena'''

        return (f"{self.get_nombre()} ($ {self.get_precio()} /u.)")



    def ficha_producto(self):
        '''Da formato al objeto para pasarlo como una ficha más informativa'''

        return (f"""\
Producto:
=========
Nombre: {self.get_nombre()}
Descripcion: {self.get_descripcion()}
Precio: {self.get_precio()}
Stock: {self.get_stock()}
Categoria: {self.get_categoria_id()}
Marca: {self.get_marca_id()}
Fecha de publicacion: {self.get_fecha_de_publicacion()}
Fecha de ultima modificacion: {self.get_fecha_de_ultima_modificacion()}
""")



    def set_producto_id(self, producto_id):
        self.producto_id = producto_id
        return 1

    def get_producto_id(self):
        return self.producto_id


    def set_nombre(self, nombre):
        if valida_nombre(nombre):
            self.nombre = nombre.title()
            return 1
        print("El nombre no es válido")

    def get_nombre(self):
        return self.nombre


    def set_descripcion(self, descripcion):
        self.descripcion = descripcion.capitalize()
        return 1

    def get_descripcion(self):
        return self.descripcion


    def set_stock(self, stock):
        if valida_stock(stock):
            self.stock = int(stock)
            return 1
        print("El stock no es válido")

    def incr_stock(self, incr):
        self.stock += int(incr)
        return 1

    def decr_stock(self, decr):
        self.stock -= int(decr)
        return 1

    def get_stock(self):
        return self.stock


    def set_precio(self, precio):
        if valida_precio(precio):
            self.precio = float(precio)
            return 1
        print("El precio no es válido")

    def get_precio(self):
        return self.precio


    def set_categoria_id(self, categoria_id):
        self.categoria_id = categoria_id
        return 1

    def get_categoria_id(self):
        return self.categoria_id


    def set_marca_id(self, marca_id):
        self.marca_id = marca_id
        return 1

    def get_marca_id(self):
        return self.marca_id


    def set_categoria(self, categoria):
        self.categoria = categoria
        self.categoria_id = categoria.get_categoria_id()
        return 1

    def get_categoria(self):
        return self.categoria


    def set_marca(self, marca):
        self.marca = marca
        self.marca_id = marca.get_marca_id()
        return 1

    def get_marca(self):
        return self.marca


    def set_fecha_de_publicacion(self, fecha_de_publicacion):
        self.fecha_de_publicacion = fecha_de_publicacion
        return 1

    def get_fecha_de_publicacion(self):
        return self.fecha_de_publicacion


    def set_fecha_de_ultima_modificacion(self, fecha_de_ultima_modificacion):
        self.fecha_de_ultima_modificacion = fecha_de_ultima_modificacion
        return 1

    def get_fecha_de_ultima_modificacion(self):
        return self.fecha_de_ultima_modificacion
