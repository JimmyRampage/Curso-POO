class Auto():
    def __init__(self, tanque):
        self.posicion = 0
        self.tanque = tanque
    def mover(self, distancia):
        if self.tanque.obtener_combustible() >= distancia / 2:
            self.posicion += distancia
            self.tanque.usar_combustible(distancia / 2)
            return f'El auto se ha movido {distancia}'
        else:
            print('No hay suficiente combustible')
    def obtener_posicion(self):
        return self.posicion

class TanqueDeCombustible:
    def __init__(self):
        self.combustible = 100
    def agregar_combustible(self, cantidad):
        self.combustible += cantidad
    def obtener_combustible(self):
        return self.combustible
    def usar_combustible(self, cantidad):
        self.combustible -= cantidad

tanque = TanqueDeCombustible()
auto = Auto(tanque)

print(auto.obtener_posicion())
print(auto.tanque.obtener_combustible())
print(auto.mover(10))
print(auto.obtener_posicion())
print(auto.tanque.obtener_combustible())
print(auto.mover(30))
print(auto.obtener_posicion())
print(auto.tanque.obtener_combustible())
print(auto.mover(24))
print(auto.obtener_posicion())
print(auto.tanque.obtener_combustible())
print(auto.mover(45))
print(auto.obtener_posicion())
print(auto.tanque.obtener_combustible())
print(auto.mover(45))
print(auto.obtener_posicion())
print(auto.tanque.obtener_combustible())
print(auto.mover(75))
print(auto.obtener_posicion())
print(auto.tanque.obtener_combustible())