# **S - Single Responsibility Principle (SRP)** - Principio de Responsabilidad Única

## Qué es

Este principio establece que una clase debe tener una única responsabilidad o razón para cambiar. En otras palabras, una clase debe hacer una sola cosa.

## Cómo nace

Surge de la necesidad de evitar clases que hagan demasiadas cosas, lo que las convierte en piezas de código difíciles de mantener y comprender.

## Qué soluciona

Ayuda a reducir la complejidad del código, haciendo que las clases sean más fáciles de entender, mantener y probar. Al tener una única responsabilidad, es más probable que los cambios en un área del código no afecten a otras áreas.

## EJEMPLO

Si creamos la clase `Auto()` sabemos que este puede arrancar, acelerar, frenar, moverse x distancia, utilizar combustible, etc...

Pero para poder mantener el código de forma más limpia, en lugar de solo crear una clase que lo contenga todo, es mejor dividirla en pequeñas funcionalidades, por ejemplo:

```py
class Auto():
    def __init__(self, tanque):
        self.posicion = 0
        self.tanque = tanque
    def mover(self, distancia):
        if self.tanque.obtener_combustible() >= distancia / 2:
            self.posicion += distancia
            self.tanque.usar_combustible(distancia / 2)
            return f'El auto se ha movido {distancia}'
        else:
            print('No hay suficiente combustible')
    def obtener_posicion(self):
        return self.posicion
```

Esta primera clase `Auto()` esta diseñada para poder dedicarse al movimiento del vehículo.

```py
class TanqueDeCombustible:
    def __init__(self):
        self.combustible = 100
    def agregar_combustible(self, cantidad):
        self.combustible += cantidad
    def obtener_combustible(self):
        return self.combustible
    def usar_combustible(self, cantidad):
        self.combustible -= cantidad
```

Esta segunda clase llamada `TanqueDeCombustible()` se encarga de administrar el rendimiento del combustible de la clase `Auto()`.
