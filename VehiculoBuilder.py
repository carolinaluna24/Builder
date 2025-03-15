from vehiculo import Vehiculo
#Define la clase VehiculoBuilder, que sigue el patrón Builder para construir objetos Vehiculo paso a paso.

class VehiculoBuilder:
    def __init__(self):
        self.tipo = None
        self.ruedas = 0
        self.motor = None
        self.color = None
        self.modelo = 0
 #Proporciona métodos para establecer cada atributo (set_tipo, set_ruedas, set_motor, set_color) 
 
    def set_tipo(self, tipo):
        self.tipo = tipo
        return self

    def set_ruedas(self, ruedas):
        self.ruedas = ruedas
        return self

    def set_motor(self, motor):
        self.motor = motor
        return self

    def set_color(self, color):
        self.color = color
        return self
    
    def set_modelo(self, modelo):
        self.modelo = modelo
        return self
 ## y el método build() para crear una instancia de Vehiculo.       
 
    def build(self):
        return Vehiculo(self.tipo, self.ruedas, self.motor, self.color, self.modelo)