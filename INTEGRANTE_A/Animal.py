class Animal:
    def __init__(self, nombre, peso, altura, tipo):
        self.nombre = nombre
        self.peso = peso
        self.altura = altura
        self.tipo = tipo

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "peso": self.peso,
            "altura": self.altura,
            "tipo": self.tipo
        }

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getPeso(self):
        return self.peso

    def setPeso(self, peso):
        self.peso = peso

    def getAltura(self):
        return self.altura

    def setAltura(self, altura):
        self.altura = altura

    def getTipo(self):
        return self.tipo

    def setTipo(self, tipo):
        self.tipo = tipo

    def Salutacio2(self):
        print(f"Nombre {self.nombre}")
        print(f"Peso {self.peso}")
        print(f"Altura {self.altura}")
        print(f"Tipo {self.tipo}")
