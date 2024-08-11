# **D - Dependency Inversion Principle (DIP)** - Principio de Inversión de Dependencias

## Qué es

Este principio establece que las clases de alto nivel no deben depender de las clases de bajo nivel; ambas deben depender de abstracciones. Además, las abstracciones no deben depender de los detalles; los detalles deben depender de las abstracciones.

## Cómo nace

Este principio fue propuesto para evitar el acoplamiento fuerte entre las partes de un sistema, lo que puede dificultar el mantenimiento y la escalabilidad.

## Qué soluciona

Promueve un código más flexible y desacoplado, donde los módulos y componentes del software pueden evolucionar de manera independiente. Facilita la inyección de dependencias y el uso de patrones de diseño como el "Inversion of Control" (IoC).

## EJEMPLO

```py
from abc import ABC, abstractmethod

class VerificadorOrtografico(ABC):
    @abstractmethod
    def verificador_palabra(self, palabra):
        pass

class Diccionario(VerificadorOrtografico):
    def verificador_palabra(self, palabra):
        # Lógica para verificar palabras si está en el diccionario
        pass

class CorrectorOrtografico:
    def __init__(self, verificador):
        self.verificador = verificador

    def corregir_texto(self, texto):
        #Usamos el verificador para corregir el texto
        pass
```

* Dependencia en Abstracciones: La clase CorrectorOrtografico depende de la abstracción VerificadorOrtografico en lugar de una implementación específica como Diccionario. Esto permite que CorrectorOrtografico sea flexible y extensible, ya que puede trabajar con cualquier clase que implemente VerificadorOrtografico.

* Inyección de Dependencias: La dependencia (verificador) se inyecta a través del constructor de CorrectorOrtografico. Esto sigue el DIP al permitir que CorrectorOrtografico reciba cualquier implementación de VerificadorOrtografico sin cambiar su propia implementación.

* Flexibilidad: Puedes cambiar la implementación de VerificadorOrtografico (por ejemplo, de Diccionario a ApiVerificadorOrtografico) sin modificar la clase CorrectorOrtografico.

* Facilidad de Mantenimiento: Si la lógica en Diccionario necesita cambiar, puedes hacerlo sin afectar el módulo de alto nivel CorrectorOrtografico, ya que este solo depende de la interfaz, no de la implementación específica.

* Reusabilidad: El mismo CorrectorOrtografico puede reutilizarse en diferentes contextos con distintas implementaciones de VerificadorOrtografico.
