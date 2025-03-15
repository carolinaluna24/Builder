# Se define el onjeto Vehiculo
class Vehiculo:
    def __init__(self, tipo, ruedas, motor, color, modelo):
        self.tipo = tipo
        self.ruedas = ruedas
        self.motor = motor
        self.color = color
        self.modelo = modelo

    def mostrar_info(self):
        return f"{self.tipo} con {self.ruedas} ruedas, motor {self.motor} , color {self.color} y modelo {self.modelo}"