class Auto:
    def __init__(self, marca:str, modelo:str):
        self.marca = marca
        self.modelo = modelo
        self.__estado = 'off'

    def encender(self):
        self.__estado = 'on'
        print('Vehículo encendido')

    def conducir(self):
        if self.__estado == 'off':
            self.encender()
        print(f'Conduciendo tu {self.marca} {self.modelo}')


auto = Auto('Suzuki', 'Swift')
auto.conducir()
