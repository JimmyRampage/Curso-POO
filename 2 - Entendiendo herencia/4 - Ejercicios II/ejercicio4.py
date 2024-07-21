class Dispositivo:
    def __init__(self, marca, precio:float, descuento:float):
        self.marca = marca
        self.precio = precio
        self.descuento = descuento
    def info(self):
        mensaje = f'''
        Marca: {self.marca}
        Precio: €{self.precio:.2f}
        Descuento {self.descuento}%
        Valor Final €{(self.precio)*(1-(self.descuento/100)):.2f}'''
        return print(mensaje)

test = Dispositivo('Apple', 599.90, 10)
test.info()

class Movil(Dispositivo):
    def __init__(self, marca, precio: float, descuento: float, os):
        super().__init__(marca, precio, descuento)
        self.os = os
    def show_os(self):
        mensaje = f'''
        SO: {self.os}'''
        return print(mensaje)

test1 = Movil('Apple', 149, 6, 'iOS')

test1.info()
test1.show_os()