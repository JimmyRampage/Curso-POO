class Animal:
    def __init__(self):
        pass
    def comer(self):
        print('comiendo')

class Mamifero(Animal):
    def __init__(self):
        super().__init__()
    def amamantar(self):
        print('amamantando')

class Ave(Animal):
    def __init__(self):
        super().__init__()
    def volar(self):
        print('volando')

class Murcielago(Mamifero, Ave):
    def __init__(self):
        super().__init__()

bat = Murcielago()

bat.amamantar()
bat.comer()
bat.volar()

print(Murcielago.mro())