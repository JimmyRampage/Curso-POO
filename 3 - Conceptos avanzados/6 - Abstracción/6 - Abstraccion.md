# Abstracción

La abstracción es uno de los cuatro pilares fundamentales de la programación orientada a objetos, junto con la encapsulación, la herencia y el polimorfismo.

En Python, la abstracción se refiere al proceso de ocultar los detalles de implementación y mostrar solo la funcionalidad esencial de un objeto. Esto ayuda a reducir la complejidad y aumentar la eficiencia del código.

## ¿Cómo se logra la abstracción en Python?

En Python, la abstracción se puede lograr utilizando clases abstractas y métodos abstractos. Las clases abstractas no pueden ser instanciadas directamente y están diseñadas para ser heredadas por otras clases. Mientras que los métodos abstractos son métodos declarados en una clase abstracta que deben ser implementados por las clases derivadas.

## Ejemplo

```py
class Auto:
    def __init__(self, marca:str, modelo:str):
        self.marca = marca
        self.modelo = modelo
        self.__estado = 'off'

    def encender(self):
        self.__estado = 'on'
        print('Vehículo encendido')

    def conducir(self):
        if self.__estado == 'off':
            self.encender()
        print(f'Conduciendo tu {self.marca} {self.modelo}')

auto = Auto('Suzuki', 'Swift')
auto.conducir()
```

### Explicación

La abstracción aquí permite que el usuario de la clase Auto no tenga que preocuparse por los detalles de cómo se enciende el automóvil o cómo se maneja su estado interno. Solo necesita interactuar con los métodos encender y conducir para utilizar la funcionalidad del automóvil.
