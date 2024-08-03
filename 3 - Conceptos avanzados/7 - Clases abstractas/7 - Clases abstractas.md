# ¿Qué son las clases abstractas?

Una clase abstracta es una clase que no puede ser instanciada directamente. Es decir, no puedes crear objetos a partir de ella. En cambio, se utiliza como una plantilla para otras clases. Las clases abstractas pueden contener métodos abstractos (sin implementación) y métodos concretos (con implementación).

## ¿Para qué se usan?

Las clases abstractas se utilizan para definir una estructura común que puede ser reutilizada mediante herencia. Aquí hay algunos usos comunes:

1. **Proporcionar una superclase común**: Permiten definir una base común para un conjunto de clases relacionadas.
2. **Definir métodos abstractos**: Los métodos abstractos deben ser implementados por las subclases, asegurando que todas las subclases compartan ciertos comportamientos.
3. **Reducir código duplicado**: Al definir métodos y atributos comunes en la clase abstracta, se evita la duplicación de código en las subclases.

### Ejemplo en Python

Aquí tienes un ejemplo sencillo en Python usando el módulo `abc` para definir una clase abstracta:

```py
from abc import ABC, abstractclassmethod

class Persona(ABC):
    @abstractclassmethod
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad

    @abstractclassmethod
    def hacer_actividad(self):
        pass

    def presentarse(self):
        print(f'Hola, soy {self.nombre}')

class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)

    def hacer_actividad(self):
        print(f'Mi actividad es {self.actividad}')

class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)

    def hacer_actividad(self):
        print(f'Mi actividad es {self.actividad}')

jimmy = Estudiante('Jimmy', 29, 'Masculino', 'Estudiante')
jimmy.hacer_actividad()

james = Trabajador('James', 29, 'Masculino', 'Programador')
james.hacer_actividad()
```

En este ejemplo, `Persona` es una clase abstracta con un método abstracto `hacer_actividad`. Las clases `Estudiante` y `Trabajador` heredan de `Persona` y proporcionan una implementación para el método `hacer_actividad`.
