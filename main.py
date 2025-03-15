from VehiculoBuilder import VehiculoBuilder
# builder crea dos vehiculos
builder = VehiculoBuilder()
carro = builder.set_tipo("Carro").set_ruedas(4).set_motor("Gasolina").set_color("Rojo").build()
moto = builder.set_tipo("Moto").set_ruedas(2).set_motor("Eléctrico").set_color("Negro").build()

#Imprmir datos del objeto (Vehiculo) se construye con los datos que se le pasa al constructor
print(carro.mostrar_info())  # Carro con 4 ruedas, motor Gasolina y color Rojo
print(moto.mostrar_info())   # Moto con 2 ruedas, motor Eléctrico y color Negro

