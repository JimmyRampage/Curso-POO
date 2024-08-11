# **L - Liskov Substitution Principle (LSP)** - Principio de Sustitución de Liskov

## Qué es

Según este principio, los objetos de una clase derivada deben poder reemplazar a los objetos de su clase base sin alterar el comportamiento correcto del programa.

## Cómo nace

Fue propuesto por Barbara Liskov y se basa en la idea de que las subclases deben ser capaces de funcionar en lugar de sus clases base sin que el usuario deba conocer las diferencias.

## Qué soluciona

Asegura que las subclases mantengan la integridad y el comportamiento esperado del programa, evitando problemas cuando se utilizan jerarquías de herencia.

## EJEMPLO

```py
# Clase para compartir todo lo que las aves tienen en común
class Ave:
    def comer(self):
        return "Esta ave está comiendo"

# Se aplica el principio, para agregar funcionalidades a una clase diferente (subclase)
class AveVoladora(Ave):
    def volar(self):
        return 'Volando'

# Nuevamente se aplica el principio gracias a otro tipo de aves
class AveNoVoladora(Ave):
    pass

def hacer_comer(ave):
    print(ave.comer())

def hacer_volar(ave):
    if isinstance(ave, AveVoladora):
        print(ave.volar())
    else:
        print("Esta ave no puede volar")

paloma = AveVoladora()
pinguino = AveNoVoladora()

hacer_comer(paloma)  # Salida: "Esta ave está comiendo"
hacer_comer(pinguino)  # Salida: "Esta ave está comiendo"

hacer_volar(paloma)   # Salida: "Volando"
hacer_volar(pinguino) # Salida: "Esta ave no puede volar"
```

* Clase base Ave: La clase Ave define un comportamiento común que todas las aves pueden realizar, como comer. No se incluye el método volar aquí porque no todas las aves pueden volar.

* Subclase AveVoladora: Esta clase extiende Ave e introduce el método volar. Esto refleja que algunas aves pueden volar, pero no todas.

* Subclase AveNoVoladora: Esta clase también extiende Ave, pero no tiene el método volar, lo que es correcto porque representa aves que no pueden volar.

* Cumplimiento del LSP: Ahora, cualquier subclase de Ave puede ser utilizada sin romper las expectativas de comportamiento. AveNoVoladora no tiene un método volar, lo cual es esperado y no causa errores.

* Claridad en la Jerarquía de Clases: La jerarquía de clases refleja mejor las capacidades y características de las aves. Las clases se estructuran de manera que las capacidades específicas, como volar, están solo en las subclases apropiadas.

* Extensibilidad: Si necesitas agregar más tipos de aves, como aves acuáticas que nadan pero no vuelan, puedes hacerlo sin modificar las clases existentes.
