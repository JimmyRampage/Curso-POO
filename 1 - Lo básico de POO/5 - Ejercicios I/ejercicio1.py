class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    def estudiar(self):
        print(f'El estudiante {self.nombre} esta estudiando...')

nombre = input('Nombre del estudiante: ')
edad = int(input('Edad del estudiante: '))
grado = input('Grado del estudiante: ')

estudiante1 = Estudiante(nombre, edad, grado)

print(f'''
    DATOS DEL ESTUDIANTE
    Nombre: {estudiante1.nombre}
    Edad: {estudiante1.edad}
    Grado: {estudiante1.grado}
    ''')

while True:
    estudiar = input('estudiar S/N: ').lower()
    if estudiar == 's':
        estudiante1.estudiar()
        break
    elif estudiar == 'n':
        print(f'{estudiante1.nombre} no estudiara')
        break
