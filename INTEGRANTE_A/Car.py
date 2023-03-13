class Car:
    def __init__(self, motor, peso, color, marca):
        self.motor = motor
        self.peso = peso
        self.color = color
        self.marca = marca

    def to_dict(self):
        return {
            "motor": self.motor,
            "peso": self.peso,
            "color": self.color,
            "marca": self.marca
        }

    def getMotor(self):
        return self.motor

    def setMotor(self, motor):
        self.motor = motor

    def getPeso(self):
        return self.peso

    def setPeso(self, peso):
        self.peso = peso

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def getMarca(self):
        return self.marca

    def setMarca(self, marca):
        self.marca = marca

    def Salutacio(self):
        print(f"Motor {self.motor}")
        print(f"Peso {self.peso}")
        print(f"Color {self.color}")
        print(f"Marca {self.marca}")
