# **I - Interface Segregation Principle (ISP)** - Principio de Segregación de Interfaces

## Qué es

Este principio establece que una clase no debe estar obligada a implementar interfaces que no utiliza. En otras palabras, es mejor tener varias interfaces pequeñas y específicas que una interfaz grande y general.

## Cómo nace

Surge de la necesidad de evitar que las clases sean forzadas a depender de métodos que no necesitan, lo que puede llevar a código innecesario y dependencias no deseadas.

## Qué soluciona

Reduce la cantidad de código innecesario en las clases, haciendo que el código sea más claro y más fácil de mantener, y facilita su reutilización.

## EJEMPLO

```py
from abc import ABC, abstractmethod

# Interface para comer
class Comedor(ABC):
    @abstractmethod
    def comer(self):
        pass

# Interface para trabajar
class Trabajador(ABC):
    @abstractmethod
    def trabajar(self):
        pass

# Interface para dormir
class Durmiente(ABC):
    @abstractmethod
    def dormir(self):
        pass

# Clase que implementa todas las interfaces
class Humano(Trabajador, Durmiente, Comedor):
    def comer(self):
        return 'Comiendo'

    def trabajar(self):
        return 'Trabajando'

    def dormir(self):
        return 'Durmiendo'

# Clase que implementa solo la interfaz de trabajador
class Robot(Trabajador):
    def trabajar(self):
        return 'Trabajando'
```

### Interfaces Específicas

* Comedor: Define la capacidad de “comer”.

* Trabajador: Define la capacidad de “trabajar”.

* Durmiente: Define la capacidad de “dormir”.

### Clases que Implementan Interfaces

* Humano: Implementa todas las interfaces (Comedor, Trabajador, Durmiente), porque un humano puede comer, trabajar y dormir.

* Robot: Solo implementa la interfaz Trabajador, porque un robot en este contexto solo tiene la capacidad de trabajar.

### ISP

* Segregación de Responsabilidades: Cada interfaz define una única responsabilidad o capacidad. Esto evita que las clases que no necesitan ciertas funcionalidades estén obligadas a implementarlas. Por ejemplo, Robot no tiene que implementar comer o dormir porque no son capacidades relevantes para un robot.

* Flexibilidad: Si necesitas agregar otra entidad en el futuro (por ejemplo, un Animal que solo coma y duerma), puedes hacerlo sin modificar las interfaces existentes ni las clases Humano o Robot. Este enfoque facilita la expansión del sistema sin romper el código existente.

* Evita Métodos Innecesarios: Clases como Robot no están obligadas a implementar métodos que no necesitan (comer y dormir), lo cual es un claro cumplimiento del ISP.

* Facilidad para Extender el Sistema: Nuevas entidades pueden implementarse fácilmente añadiendo las interfaces que necesiten sin afectar a las clases existentes.

* Claridad y Mantenimiento: El código es más claro, ya que cada clase implementa solo lo que le es relevante, y es más fácil de mantener y entender.
