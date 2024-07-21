class Rectangle:
    def __init__(self, high, width):
        self.high = high
        self.width = width
    def area(self):
        area = self.high * self.width
        return print('Área =', area)
    def perimeter(self):
        perimeter = (self.high * 2) + (self.width * 2)
        return print('Perimetro =', perimeter)

rectangulo1 = Rectangle(8,15)
rectangulo1.area()
rectangulo1.perimeter()