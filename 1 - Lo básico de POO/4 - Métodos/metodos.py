class Celular:
    def __init__(self, marca, modelo, camera):
        self.marca = marca
        self.modelo = modelo
        self.camera = camera
    def llamar(self):
        print(f'Estas llamando desde un {self.modelo}...')
    def cortar(self):
        print(f'Terminaste la llamada desde un {self.modelo}...')

cel1 = Celular('Apple', 'iPhone 15', '48MP')
cel2 = Celular('Samsung', 'S23', '48MP')

cel1.llamar()
cel1.cortar()