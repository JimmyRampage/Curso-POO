from abc import ABC, abstractmethod

class Comedor(ABC):
    @abstractmethod
    def comer (self):
        pass

class Trabajador(ABC):
    @abstractmethod
    def trabajar(self):
        pass

class Durmiente(ABC):
    @abstractmethod
    def dormir(self):
        pass

class Humano(Trabajador, Durmiente, Comedor):
    def comer (self):
        return 'Comiendo'

    def trabajar(self):
        return 'Trabajando'

    def dormir(self):
        return 'Durmiendo'

class Robot(Trabajador): # el robot solo trabaja
    def trabajar(self):
        return 'Trabajando'

class Animal(Comedor, Durmiente):
    def comer(self):
        return 'Comiendo'

    def dormir(self):
        return 'Durmiendo'

def hacer_comer(comedor: Comedor):
    print(comedor.comer())

def hacer_trabajar(trabajador: Trabajador):
    print(trabajador.trabajar())

def hacer_dormir(durmiente: Durmiente):
    print(durmiente.dormir())


humano = Humano()
robot = Robot()
animal = Animal()

hacer_comer(humano)   # Salida: "Comiendo"
hacer_trabajar(humano) # Salida: "Trabajando"
hacer_dormir(humano)  # Salida: "Durmiendo"

hacer_trabajar(robot) # Salida: "Trabajando"
# hacer_comer(robot)  # Error: Robot no implementa la interfaz Comedor
# hacer_dormir(robot) # Error: Robot no implementa la interfaz Durmiente

hacer_comer(animal)   # Salida: "Comiendo"
hacer_dormir(animal)  # Salida: "Durmiendo"