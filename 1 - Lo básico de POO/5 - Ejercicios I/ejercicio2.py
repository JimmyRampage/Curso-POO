class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def presentarse(self):
        mensaje = f'Hola, soy {self.nombre} y tengo {self.edad} años de edad'
        return mensaje

persona1 = Persona('Maria', 32)

print(persona1.presentarse())