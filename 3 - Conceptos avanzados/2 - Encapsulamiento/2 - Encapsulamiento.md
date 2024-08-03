# ¿Que es el encapsulamiento?

El encapsulamiento es uno de los fundamentos de la programación orientada a objetos y se refiere a la práctica de mantener los detalles internos de cómo se implementa un objeto ocultos del mundo exterior. En Python, esto se logra principalmente a través del uso de métodos y atributos privados.

Es importante mencionar que Python no tiene una forma estricta de restringir el acceso a sus atributos o métodos privados (como lo hacen otros lenguajes como Java o C++), pero por convención, cualquier atributo o método que comienza con dos guiones bajos (__) se considera privado y no debe ser accedido directamente. Sin embargo, técnicamente aún es posible acceder a estos atributos/métodos “privados” si realmente necesitas hacerlo, pero generalmente se considera una mala práctica.

También existen los atributos o métodos protegidos, que solo se crean con un guion bajo, estos si se pueden acceder fácilmente, pero son indicativos para el desarrollador que no se debería acceder a ellos.

En términos más simples, el encapsulamiento es como una cápsula (de ahí el nombre) que oculta los datos internos del objeto del resto del programa.

## Ejemplo

```py
class MiClase:
    def __init__(self):
        self._atributo_protegido = 'atributo protegido con un underscore'
        self.__atributo_privado = 'atributo muy privado con doble underscore'
```

### Instanciando

```py
objeto = MiClase()
```

### Interactuando con atributo protegido

```py
print(objeto._atributo_protegido)
```

#### mostrando en pantalla atributo protegido

```py
atributo protegido con un underscore
```

### Interactuando con atributo privado

```py
print(objeto.__atributo_privado)
```

#### mostrando en pantalla atributo privado

```py
Traceback (most recent call last):
  File "/Users/jimmyrampage/Code/Dalto_POO/3 - Conceptos avanzados/2 - Encapsulamiento/encapsulamiento.py", line 8, in <module>
    print(objeto.__atributo_muy_privado)
AttributeError: 'MiClase' object has no attribute '__atributo_muy_privado'. Did you mean: '_MiClase__atributo_muy_privado'?
```
