# Decoradores

## ¿Qué es un decorador?

Un decorador es una función que envuelve otra función, añadiéndole funcionalidad antes o después de su ejecución, sin modificar su código. Los decoradores se utilizan a menudo para añadir características como logging, validación, acceso a bases de datos, etc., de una manera modular y reutilizable.

## ¿Para qué sirven los decoradores?

* Añadir comportamiento: Permiten añadir comportamiento adicional a las funciones o métodos existentes.

* DRY (Don't Repeat Yourself): Ayudan a mantener el código más limpio y reutilizable, evitando la repetición de código.

* Modularidad: Facilitan la división de la funcionalidad en módulos, mejorando la organización del código.

* Legibilidad: Aumentan la legibilidad del código al separar claramente la lógica de la función principal de la lógica adicional.

## ¿Cómo se usan los decoradores?

Para usar un decorador, se coloca el símbolo **`@`** seguido del nombre del decorador antes de la definición de una función. A continuación se presenta un ejemplo básico de un decorador y su uso:

Ejemplo básico de decorador

```py
def decorador(func):
    def func_modificada():
        print('Antes de llamar a la función')
        func()
        print('Después de llamar a la función')
    return func_modificada

@decorador
def saludo():
    print('Hola Mundo!')

saludo()
```

print:

```py
Algo se está haciendo antes de la función.
Hola!
Algo se está haciendo después de la función.
```

En este ejemplo, `decorador` es una función decoradora que añade mensajes antes y después de la ejecución de la función saludar.

## Decorador con parámetros en la función original

Si la función original toma parámetros, el decorador debe ser diseñado para aceptarlos y pasarlos a la función original. Aquí hay un ejemplo:

```py
def decorador(func):
    def wrap(*args, **kwargs):
        print("Algo se está haciendo antes de la función.")
        resultado = func(*args, **kwargs)
        print("Algo se está haciendo después de la función.")
        return resultado
    return wrap

@decorador
def saludar(nombre):
    print(f"Hola, {nombre}!")

saludar("Juan")
```

print:

```py
Algo se está haciendo antes de la función.
Hola, Juan!
Algo se está haciendo después de la función.
```

## Decoradores anidados

Es posible usar múltiples decoradores en una sola función. Se aplicarán en el orden en que se definen (de arriba hacia abajo):

```py
def decorador1(func):
    def wrap():
        print("Decorador 1")
        func()
        print("Decorador 1 después")
    return wrap

def decorador2(func):
    def wrap():
        print("Decorador 2")
        func()
        print("Decorador 2 después")
    return wrap

@decorador1
@decorador2
def saludar():
    print("Hola!")

saludar()
```

print:

```py
Decorador 1
Decorador 2
Hola!
Decorador 2 después
Decorador 1 después
```

## Decoradores en clases

Los decoradores también se pueden usar en métodos de clases. Aquí hay un ejemplo de un decorador que se aplica a un método de instancia:

```py
def decorador_metodo(func):
    def envoltura(self, *args, **kwargs):
        print(f"Llamando al método {func.__name__} de la instancia {self}")
        return func(self, *args, **kwargs)
    return envoltura

class MiClase:
    @decorador_metodo
    def metodo(self):
        print("Método de la clase ejecutado.")

obj = MiClase()
obj.metodo()
```

Salida:

```py
Llamando al método metodo de la instancia <__main__.MiClase object at 0x...>
Método de la clase ejecutado.
```

## Decoradores con argumentos

Para crear un decorador que acepte argumentos, se necesita una capa adicional de funciones. Aquí hay un ejemplo:

```py
def repetidor(veces):
    def decorador(func):
        def envoltura(*args, **kwargs):
            for _ in range(veces):
                func(*args, **kwargs)
        return envoltura
    return decorador

@repetidor(3)
def saludar(nombre):
    print(f"Hola, {nombre}!")

saludar("Juan")
```

Print:

```py
Hola, Juan!
Hola, Juan!
Hola, Juan!
```

En este caso, repetidor es un decorador que toma un argumento (veces) y devuelve un decorador que repite la ejecución de la función especificada el número de veces indicado.
