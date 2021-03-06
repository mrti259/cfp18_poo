class Provincia:
    def __init__(self, provincia_id=0, nombre="", pais_id=0):
        self.provincia_id = provincia_id
        self.nombre = nombre
        self.pais_id = pais_id
        self.pais = None



    def __str__(self):
        return (self.get_nombre())



    def set_provincia_id(self, provincia_id):
        self.provincia_id = provincia_id
        return 1

    def get_provincia_id(self):
        return self.provincia_id



    def set_nombre(self, nombre):
        self.nombre = nombre
        return 1

    def get_nombre(self):
        return self.nombre



    def set_pais_id(self, pais_id):
        self.pais_id = pais_id
        return 1

    def get_pais_id(self):
        return self.pais_id



    def set_pais(self, pais):
        self.pais = pais
        self.set_pais_id(pais.get_pais_id())
        return 1

    def get_pais(self):
        return self.pais
