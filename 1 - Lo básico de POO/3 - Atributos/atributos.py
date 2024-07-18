class Celular:
    def __init__(self, marca, modelo, camera):
        self.marca = marca
        self.modelo = modelo
        self.camera = camera

cel1 = Celular('Apple', 'iPhone 15', '48MP')
cel2 = Celular('Samsung', 'S23', '48MP')

print(cel1.marca)
print(cel2.modelo)