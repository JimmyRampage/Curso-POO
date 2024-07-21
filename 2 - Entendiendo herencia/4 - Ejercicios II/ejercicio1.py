class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def presentarse(self):
        mensaje = f'Hola, soy {self.nombre} y tengo {self.edad} años.'
        return mensaje

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado
    def curso(self):
        mensaje = f'Estoy en {self.grado} grado.'
        return mensaje

estudiante1 = Estudiante('María', 32, 'FP')

print(estudiante1.presentarse())
print(estudiante1.curso())