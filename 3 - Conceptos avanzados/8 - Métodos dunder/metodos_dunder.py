class Persona:
    def __init__(self, nombre:str, edad:int):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona(nombre={self.nombre}, edad={self.edad})'

    def  __repr__(self):
        return f'Persona("{self.nombre}", {self.edad})'

    def __add__(self, other, combinar_nombres=True):
        nueva_edad:int = self.edad + other.edad
        if combinar_nombres:
            nuevo_nombre:str = self.nombre + '-#-' + other.nombre
        else:
            nuevo_nombre:str = self.nombre
        return Persona(nuevo_nombre, nueva_edad)

    def __len__(self):
        car = len(self.nombre)
        return car

    def __mul__(self, other):
        multi_edad = self.edad * other.edad
        multi_nombre = self.nombre * (len(other.nombre))
        return Persona(multi_nombre, multi_edad)

# Instanciando personas
person = Persona('Jimmy', 29)
person1 = Persona('Maria', 32)
person2 = Persona('Ikigai', 3)
person3 = Persona('Frederick', 2)

# Usando el método __add__
nueva_persona = person + person1 + person2 + person3
print(nueva_persona.nombre)
print(nueva_persona.edad)

nueva_persona1 = person2 + person3
print(nueva_persona1.nombre)
print(nueva_persona1.edad)

# Usando el método __len__
print(len(nueva_persona))
print(nueva_persona1.__len__())

# Usando el método __mul__
nueva_persona2 = person1 * person2
print(nueva_persona2.edad)
print(nueva_persona2.nombre)
