class Persona:
    def __init__(self, nombre, edad, nacionalidad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        self.sexo = sexo
    def presentarse(self):
        mensaje = f'Hola, mi nombre es {self.nombre}, tengo {self.edad} años, soy {self.nacionalidad} y soy {self.sexo}'
        return print(mensaje)

class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad
    def mostrar_habilidad(self):
        hab = f'Mi habilidad es: {self.habilidad}'
        return print(hab)

class EmpleadoArtista(Persona,Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        Persona.__init__(self, nombre, edad, nacionalidad, None)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa
    def presentarse(self):
        return super().mostrar_habilidad()

james = EmpleadoArtista('James',29,'chileno','Guitarrista',2500,'Google')

james.presentarse()
james.mostrar_habilidad()

herencia = issubclass(EmpleadoArtista, Artista)
instancia = isinstance(james, EmpleadoArtista)
print(herencia)
print(instancia)