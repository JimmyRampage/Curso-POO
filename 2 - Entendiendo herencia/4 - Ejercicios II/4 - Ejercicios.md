# Ejercicios

## Ejercicio 1

Ejercicio de herencia y uso de super:

Crear un sistema para una escuela. En este sistema, vamos a tener dos clases principales: **Persona y Estudiante**.

La clase **Persona** tendrá los atributos de nombre y edad y un método que imprima el nombre y la edad de la persona.

La clase **Estudiante** heredará de la clase `Persona` y también tendrá un atributo adicional: grado y un método que imprima el grado del estudiante.

Deberás utilizar `super` en el método de inicialización `__init__` para reutilizar el código de la clase padre (`Persona`).

Luego crea una instancia de la clase `Estudiante` e imprime sus atributos y utiliza sus métodos para asegurarte de que todo funciona correctamente.

[Resultado](/2%20-%20Entendiendo%20herencia/4%20-%20Ejercicios%20II/ejercicio1.py)

## Ejercicio 2

Imagina que estás modelando animales en un zoológico. Crear tres clases: "Animal", "Mamífero" y "Ave".

La clase "Animal" debe tener un método llamado "comer". La clase "Mamífero" debe tener un método llamado "amamantar" y la clase "Ave" un método llamado "volar".

Ahora, crea una clase "Murciélago" que herede de "Mamífero" y "Ave", en ese orden, y por lo tanto debe ser capaz de "amamantar" y "volar", además de "comer"

Finalmente, juega con el orden de herencia de la clase "Murciélago" y observa cómo cambia el MRO y el comportamiento de los métodos al usar super().

[Resultado](/2%20-%20Entendiendo%20herencia/4%20-%20Ejercicios%20II/ejercicio2.py)

## Ejercicio 3

Crear un sistema de vehículos. En este sistema, vamos a tener dos clases principales: **Vehículo y Coche**.

La clase **Vehículo** tendrá los atributos de marca y modelo, y un método que imprima la marca y el modelo del vehículo.

La clase **Coche** heredará de la clase `Vehículo` y también tendrá un atributo adicional: número de puertas, y un método que imprima el número de puertas del coche.

Deberás utilizar `super` en el método de inicialización `__init__` para reutilizar el código de la clase padre (`Vehículo`).

Luego crea una instancia de la clase `Coche` e imprime sus atributos y utiliza sus métodos para asegurarte de que todo funciona correctamente.

[Resultado](/2%20-%20Entendiendo%20herencia/4%20-%20Ejercicios%20II/ejercicio3.py)

## Ejercicio 4

Crear un sistema para dispositivos electrónicos. En este sistema, vamos a tener dos clases principales: **Dispositivo** y **Móvil**.

La clase **Dispositivo** tendrá los atributos de marca y precio, y un método que imprima la marca y el precio del dispositivo.

La clase **Móvil** heredará de la clase `Dispositivo` y también tendrá un atributo adicional: sistema operativo, y un método que imprima el sistema operativo del móvil.

Deberás utilizar `super` en el método de inicialización `__init__` para reutilizar el código de la clase padre (`Dispositivo`).

Luego crea una instancia de la clase `Móvil` e imprime sus atributos y utiliza sus métodos para asegurarte de que todo funciona correctamente.

[Resultado](/2%20-%20Entendiendo%20herencia/4%20-%20Ejercicios%20II/ejercicio4.py)

## Ejercicio 5

Crear un sistema para figuras geométricas. En este sistema, vamos a tener dos clases principales: **Figura** y **Rectángulo**.

La clase **Figura** tendrá los atributos de color y grosor de línea, y un método que imprima el color y el grosor de línea de la figura.

La clase **Rectángulo** heredará de la clase `Figura` y también tendrá atributos adicionales: largo y ancho, y un método que calcule e imprima el área del rectángulo.

Deberás utilizar `super` en el método de inicialización `__init__` para reutilizar el código de la clase padre (`Figura`).

Luego crea una instancia de la clase `Rectángulo` e imprime sus atributos y utiliza sus métodos para asegurarte de que todo funciona correctamente.

[Resultado](/2%20-%20Entendiendo%20herencia/4%20-%20Ejercicios%20II/ejercicio5.py)

## Ejercicio 6

Crear un sistema para gestionar trabajadores. En este sistema, vamos a tener dos clases principales: **Trabajador y Gerente**.

La clase **Trabajador** tendrá los atributos de nombre y salario, y un método que imprima el nombre y el salario del trabajador.

La clase **Gerente** heredará de la clase `Trabajador` y también tendrá un atributo adicional: departamento, y un método que imprima el departamento del gerente.

Deberás utilizar `super` en el método de inicialización `__init__` para reutilizar el código de la clase padre (`Trabajador`).

Luego crea una instancia de la clase `Gerente` e imprime sus atributos y utiliza sus métodos para asegurarte de que todo funciona correctamente.

[Resultado](/2%20-%20Entendiendo%20herencia/4%20-%20Ejercicios%20II/ejercicio6.py)
