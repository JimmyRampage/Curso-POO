# **O - Open/Closed Principle (OCP)** - Principio Abierto/Cerrado

## Qué es

Este principio establece que las clases deben estar abiertas para su extensión, pero cerradas para su modificación.

## Cómo nace

Se origina de la necesidad de crear software que pueda evolucionar con nuevos requisitos sin tener que modificar el código existente, lo que podría introducir errores.

## Qué soluciona

Permite agregar nuevas funcionalidades mediante la extensión del código existente (por ejemplo, a través de herencia o composición) en lugar de modificar el código original, lo que reduce el riesgo de introducir bugs.

## EJEMPLO

```py
class Notificador:
    def __init__(self, usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje

    def notificar(self):
        raise NotImplementedError("Este método debe ser implementado por una subclase")


class NotificadorEmail(Notificador):
    def notificar(self):
        print(f'Enviando mensaje a {self.usuario.email}')

class NotificadorSms(Notificador):
    def notificar(self):
        print(f'Enviando SMS a {self.usuario.sms}')
```

* La clase notificador hace referencia a un objeto que se encarga de notificar.

* tiene una funcion `notificar()` que obliga a crear una funcion notificar cuando esta es heredada

    >[!NOTE]
    >**NotImplementedError**
    >
    >NotImplementedError es un tipo específico de excepción en Python. Se utiliza principalmente en clases base o abstractas para indicar que un método o función no ha sido implementado y debe ser sobrescrito en una subclase.
    >
    >Cuando defines un método en una clase base que no tiene una implementación concreta y quieres forzar a las subclases a que lo implementen, puedes utilizar raise NotImplementedError. Esto es útil para diseñar interfaces o clases abstractas donde ciertos métodos deben ser implementados por cualquier subclase.
    >
    >En este ejemplo, Notificador es una clase base que define el método notificar, pero no proporciona una implementación. En cambio, lanza un NotImplementedError. Esto significa que cualquier subclase de Notificador debe implementar el método notificar; de lo contrario, si se intenta usar el método sin sobrescribirlo, se lanzará la excepción.

* **No Modificación de la Clase Base**: La clase base Notificador sigue siendo la misma y no requiere cambios a medida que se agregan nuevos tipos de notificaciones. Esto cumple con la parte de “cerrado para modificación” del OCP.

* **Extensión a través de Subclases**: Se pueden agregar nuevas subclases (como NotificadorEmail o NotificadorSms) que implementen el método notificar sin modificar las clases existentes, cumpliendo con la parte de “abierto para extensión” del OCP.

## Beneficios

* Escalabilidad: Puedes agregar tantas nuevas formas de notificación como necesites (como NotificadorFax, NotificadorWhatsApp, etc.) sin tocar el código existente. Esto minimiza el riesgo de introducir errores en el código previamente probado.
* Mantenimiento: El código es más fácil de mantener y actualizar, ya que las nuevas funcionalidades se agregan de manera modular y aislada.
