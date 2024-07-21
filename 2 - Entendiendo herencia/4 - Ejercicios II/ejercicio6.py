class Trabajador:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
    def info(self):
        mensaje = f'Nombre: {self.nombre}\nSalario: {self.salario}'
        return print(mensaje)

class Gerente(Trabajador):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento
    def info(self):
        mensaje = f'Departamento: {self.departamento}'
        return super().info(), print(mensaje)

gerente = Gerente('James', 3000, 'Python')

gerente.info()