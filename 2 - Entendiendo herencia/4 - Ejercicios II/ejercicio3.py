class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    def info(self):
        mensaje = f'Marca: {self.marca}\nModelo: {self.modelo}'
        return print(mensaje)

class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas
    def door(self):
        mensaje = f'Este vehículo cuenta con {self.puertas} puertas.'
        return print(mensaje)

coche1 = Coche('Suzuki', 'Swift', 5)

coche1.info()
coche1.door()