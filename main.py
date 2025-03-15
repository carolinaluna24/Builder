from VehiculoBuilder import VehiculoBuilder
# builder crea dos vehiculos
builder = VehiculoBuilder()
carro = builder.set_tipo("Carro").set_ruedas(4).set_motor("Gasolina").set_color("Rojo").set_modelo(2008).build()
moto = builder.set_tipo("Moto").set_ruedas(2).set_motor("Eléctrico").set_color("Negro").set_modelo(2020).build()
camion = builder.set_tipo("Camión").set_ruedas(8).set_motor("Diesel").set_color("Blanco").set_modelo(2024).build()

#Imprmir datos del objeto (Vehiculo) se construye con los datos que se le pasa al constructor
print(carro.mostrar_info())  # Carro con 4 ruedas, motor Gasolina y color Rojo
print(moto.mostrar_info())   # Moto con 2 ruedas, motor Eléctrico y color Negro
print(camion.mostrar_info()) # Un camion de 8 ruedas motor diesel 

