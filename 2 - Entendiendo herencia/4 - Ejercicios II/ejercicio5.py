class Figura:
    def __init__(self, color, grosor_linea):
        self.color = color
        self.grosor_linea = grosor_linea
    def info(self):
        mensaje = f'''
        Color: {self.color}
        Grosor de linea: {self.grosor_linea}
        '''
        return print(mensaje)

class Rectangulo(Figura):
    def __init__(self, color, grosor_linea, alto, ancho):
        super().__init__(color, grosor_linea)
        self.alto = alto
        self.ancho = ancho
    def area(self):
        area = self.ancho * self.alto
        return print(f'        Área es: {area}')

rect1 = Rectangulo('Rojo', '2px', 4.5, 3)

rect1.info()
rect1.area()