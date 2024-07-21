class Persona:
    def __init__(self, nombre, edad, nacionalidad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        self.sexo = sexo
    def presentarse(self):
        mensaje = f'Hola, mi nombre es {self.nombre}, tengo {self.edad} años, soy {self.nacionalidad} y soy {self.sexo}'
        return print(mensaje)

class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, cargo, salario):
        super().__init__(nombre, edad, nacionalidad, None)
        self.cargo = cargo
        self.salario = salario
    def presentarse(self):
        mensaje = f'Hola, mi nombre es {self.nombre}, tengo {self.edad} años, soy {self.cargo} y mi salario es de: €{self.salario}/month'
        return print(mensaje)

persona1 = Persona('James',29,'chileno','Masculino')
empleado1 = Empleado('James',29,'chileno', 'Programador', 2500)

persona1.presentarse()

empleado1.presentarse()