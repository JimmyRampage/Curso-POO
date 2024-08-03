class Personaje:
    def __init__(self, nombre, fuerza, velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad
    def __repr__(self):
        rpr = f'{self.nombre} (Fuerza = {self.fuerza:_.0f}, velocidad = {self.velocidad:_.0f})'
        return rpr
    def __add__(self,other):
        nuevo_nombre = self.nombre[:2] + other.nombre[2:]
        x = self.fuerza + other.fuerza
        nueva_fuerza = (x/2)**1.1
        y = self.velocidad + other.velocidad
        nueva_velocidad = (y/2)**1.05
        return Personaje(nuevo_nombre,nueva_fuerza,nueva_velocidad)

goku = Personaje('Goku', 12341, 123)
gohan = Personaje('Gohan', 5433, 58)
vegeta = Personaje('Vegeta', 12213, 100)

print(goku)
print(gohan)
print(vegeta)
print()
print(goku+vegeta)
print()
fusion1 = vegeta+gohan
print(fusion1)
print()
print(fusion1+goku)
