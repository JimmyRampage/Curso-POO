# Métodos dunder o mágicos

Los métodos "dunder" (double underscore), también conocidos como métodos mágicos o métodos especiales, son métodos en Python que tienen nombres rodeados por dos guiones bajos (por ejemplo, `__init__`). Estos métodos permiten definir comportamientos especiales para los objetos, como la inicialización, la representación, la comparación, las operaciones aritméticas, entre otros. Se utilizan para crear funcionalidades que no se pueden lograr con los métodos normales.

## Métodos de Inicialización y Destrucción

### `__init__(self, ...)`

* **Propósito**: Inicializar una nueva instancia de una clase.
* **Uso**: Establecer el estado inicial del objeto, es decir, sus atributos.
* **Cómo Implementarlo**:

    ```python
    class Persona:
        def __init__(self, nombre, edad):
            self.nombre = nombre
            self.edad = edad
    ```

* **Errores Comunes**:
  * Olvidar inicializar todos los atributos necesarios.
  * No llamar a `super().__init__()` en clases derivadas cuando sea necesario.

### `__new__(cls, ...)`

* **Propósito**: Crear y retornar una nueva instancia de una clase.
* **Uso**: Principalmente en la creación de instancias de clases inmutables como `int`, `str`, etc.
* **Cómo Implementarlo**:

    ```python
    class Singleton:
        _instance = None

        def __new__(cls, *args, **kwargs):
            if not cls._instance:
                cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
            return cls._instance
    ```

* **Errores Comunes**:
  * No retornar una instancia desde `__new__()`.
  * No llamar a `super().__new__()` en clases derivadas.

### `__del__(self)`

* **Propósito**: Destructor de la instancia, llamado cuando el objeto es recolectado por el recolector de basura.
* **Uso**: Limpieza de recursos como archivos o conexiones de red.
* **Cómo Implementarlo**:

    ```python
    class Recurso:
        def __del__(self):
            print("Recurso liberado")
    ```

* **Errores Comunes**:
  * Asumir que se llamará inmediatamente al finalizar el objeto.
  * Intentar acceder a otros objetos que pueden haber sido ya recolectados.

## Métodos de Representación

### `__str__(self)`

* **Propósito**: Retornar una cadena que representa al objeto de una manera legible para humanos.
* **Uso**: Usado por `str()`, `print()`.
* **Cómo Implementarlo**:

    ```python
    class Persona:
        def __str__(self):
            return f"{self.nombre}, {self.edad} años"
    ```

* **Errores Comunes**:
  * Proporcionar una representación que no sea informativa o legible.

### `__repr__(self)`

* **Propósito**: Retornar una cadena que representa al objeto de una manera detallada y precisa.
* **Uso**: Usado por `repr()`, y en la consola interactiva.
* **Cómo Implementarlo**:

    ```python
    class Persona:
        def __repr__(self):
            return f"Persona(nombre={self.nombre!r}, edad={self.edad!r})"
    ```

* **Errores Comunes**:
  * No proporcionar suficiente detalle para recrear el objeto.

## Métodos de Conversión

### `__bytes__(self)`

* **Propósito**: Convierte el objeto a una secuencia de bytes.
* **Uso**: Usado por `bytes()`.
* **Cómo Implementarlo**:

    ```python
    class Datos:
        def __bytes__(self):
            return bytes(f"{self.valor}", 'utf-8')
    ```

* **Errores Comunes**:
  * Proporcionar una conversión que no sea consistente o completa.

### `__format__(self, format_spec)`

* **Propósito**: Formatea el objeto usando la especificación dada.
* **Uso**: Usado por `format()`.
* **Cómo Implementarlo**:

    ```python
    class Persona:
        def __format__(self, format_spec):
            if format_spec == "formal":
                return f"{self.nombre}, {self.edad} años"
            else:
                return self.__str__()
    ```

* **Errores Comunes**:
  * No manejar correctamente las diferentes especificaciones de formato.

### `__int__(self)`, `__float__(self)`, `__complex__(self)`

* **Propósito**: Convierte el objeto a un entero, flotante o complejo.
* **Uso**: Usado por `int()`, `float()`, `complex()`.
* **Cómo Implementarlo**:

    ```python
    class Contador:
        def __init__(self, valor):
            self.valor = valor

        def __int__(self):
            return int(self.valor)
    ```

* **Errores Comunes**:
  * Proporcionar una conversión que no tenga sentido para el objeto.

## Métodos de Contenedor

### `__len__(self)`

* **Propósito**: Retorna la longitud del objeto.
* **Uso**: Usado por `len()`.
* **Cómo Implementarlo**:

    ```python
    class Grupo:
        def __init__(self, miembros):
            self.miembros = miembros

        def __len__(self):
            return len(self.miembros)
    ```

* **Errores Comunes**:
  * No retornar un entero válido.

### `__getitem__(self, key)`

* **Propósito**: Permite el acceso a elementos usando índices.
* **Uso**: Usado por la notación `obj[key]`.
* **Cómo Implementarlo**:

    ```python
    class Grupo:
        def __init__(self, miembros):
            self.miembros = miembros

        def __getitem__(self, key):
            return self.miembros[key]
    ```

* **Errores Comunes**:
  * No manejar correctamente índices fuera de rango.

### `__setitem__(self, key, value)`

* **Propósito**: Permite asignar valores a elementos usando índices.
* **Uso**: Usado por la notación `obj[key] = value`.
* **Cómo Implementarlo**:

    ```python
    class Grupo:
        def __init__(self, miembros):
            self.miembros = miembros

        def __setitem__(self, key, value):
            self.miembros[key] = value
    ```

* **Errores Comunes**:
  * No manejar correctamente índices fuera de rango.

### `__delitem__(self, key)`

* **Propósito**: Permite eliminar elementos usando índices.
* **Uso**: Usado por la notación `del obj[key]`.
* **Cómo Implementarlo**:

    ```python
    class Grupo:
        def __init__(self, miembros):
            self.miembros = miembros

        def __delitem__(self, key):
            del self.miembros[key]
    ```

* **Errores Comunes**:
  * No manejar correctamente índices fuera de rango.

### `__iter__(self)`

* **Propósito**: Retorna un iterador para el objeto.
* **Uso**: Usado por `iter()` y en bucles `for`.
* **Cómo Implementarlo**:

    ```python
    class Grupo:
        def __init__(self, miembros):
            self.miembros = miembros

        def __iter__(self):
            return iter(self.miembros)
    ```

* **Errores Comunes**:
  * No retornar un objeto iterador válido.

### `__next__(self)`

* **Propósito**: Retorna el siguiente elemento en un iterador.
* **Uso**: Usado por `next()`.
* **Cómo Implementarlo**:

    ```python
    class Contador:
        def __iter__(self):
            self.n = 0
            return self

        def __next__(self):
            if self.n < 3:
                self.n += 1
                return self.n
            else:
                raise StopIteration
    ```

* **Errores Comunes**:
  * No manejar correctamente el fin de la iteración.

## Métodos de Comparación

### `__eq__(self, other)`, `__ne__(self, other)`

* **Propósito**: Define el comportamiento para la igualdad (`==`) y desigualdad (`!=`).
* **Uso**: Usado por `==` y `!=`.
* **Cómo Implementarlo**:

    ```python
    class Persona:
        def __init__(self, nombre, edad):
            self.nombre = nombre
            self.edad = edad

        def __eq__(self, other):
            return self.nombre == other.nombre and self.edad == other.edad
    ```

* **Errores Comunes**:
  * No manejar correctamente la comparación con objetos de diferentes tipos.

### `__lt__(self, other)`, `__le__(self, other)`, `__gt__(self, other)`, `__ge__(self, other)`

* **Propósito**: Define el comportamiento para comparaciones de orden (`<`, `<=`, `>`, `>=`).
* **Uso**: Usado por `<`, `<=`, `>`, `>=`.
* **Cómo Implementarlo**:

    ```python
    class Persona:
        def __init__(self, nombre, edad):
            self.nombre = nombre
            self.edad = edad

        def __lt

__(self, other):
            return self.edad < other.edad
    ```

* **Errores Comunes**:
  * No mantener la consistencia entre todas las comparaciones.

## Métodos de Aritmética y Asignación

### `__add__(self, other)`, `__sub__(self, other)`, `__mul__(self, other)`, `__truediv__(self, other)`, `__floordiv__(self, other)`, `__mod__(self, other)`, `__pow__(self, other)`

* **Propósito**: Define el comportamiento para operaciones aritméticas.
* **Uso**: Usado por `+`, `-`, `*`, `/`, `//`, `%`, `**`.
* **Cómo Implementarlo**:

    ```python
    class Numero:
        def __init__(self, valor):
            self.valor = valor

        def __add__(self, other):
            return Numero(self.valor + other.valor)
    ```

* **Errores Comunes**:
  * No manejar correctamente la operación con tipos no compatibles.

### `__iadd__(self, other)`, `__isub__(self, other)`, `__imul__(self, other)`, `__itruediv__(self, other)`, `__ifloordiv__(self, other)`, `__imod__(self, other)`, `__ipow__(self, other)`

* **Propósito**: Define el comportamiento para operaciones aritméticas in situ.
* **Uso**: Usado por `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`.
* **Cómo Implementarlo**:

    ```python
    class Numero:
        def __init__(self, valor):
            self.valor = valor

        def __iadd__(self, other):
            self.valor += other.valor
            return self
    ```

* **Errores Comunes**:
  * No retornar `self` después de la modificación.

## Otros Métodos Especiales

### `__call__(self, *args, **kwargs)`

* **Propósito**: Permite que una instancia de la clase sea llamada como una función.
* **Uso**: Usado cuando se llama a una instancia de la clase.
* **Cómo Implementarlo**:

    ```python
    class MiClase:
        def __call__(self, *args, **kwargs):
            print("Instancia llamada como función")
    ```

* **Errores Comunes**:
  * No implementar la lógica deseada en el método `__call__`.

### `__contains__(self, item)`

* **Propósito**: Define el comportamiento para la operación de pertenencia (`in`).
* **Uso**: Usado por `in`.
* **Cómo Implementarlo**:

    ```python
    class Grupo:
        def __init__(self, miembros):
            self.miembros = miembros

        def __contains__(self, item):
            return item in self.miembros
    ```

* **Errores Comunes**:
  * No manejar correctamente el caso cuando el elemento no está presente.

### `__enter__(self)` y `__exit__(self, exc_type, exc_value, traceback)`

* **Propósito**: Usados en contextos con `with` para manejo de recursos.
* **Uso**: Usado por `with`.
* **Cómo Implementarlo**:

    ```python
    class GestorRecursos:
        def __enter__(self):
            print("Entrando en el contexto")
            return self

        def __exit__(self, exc_type, exc_value, traceback):
            print("Saliendo del contexto")
    ```

* **Errores Comunes**:
  * No liberar correctamente los recursos en `__exit__`.

### `__index__(self)`

* **Propósito**: Define el comportamiento de conversión a entero.
* **Uso**: Usado por `hex()`, `oct()`, `bin()`, y otros.
* **Cómo Implementarlo**:

    ```python
    class MiClase:
        def __init__(self, valor):
            self.valor = valor

        def __index__(self):
            return self.valor
    ```

* **Errores Comunes**:
  * No retornar un valor entero válido.

### `__bool__(self)`

* **Propósito**: Define el comportamiento de conversión a booleano.
* **Uso**: Usado por `bool()`, y en contextos que requieren una evaluación booleana.
* **Cómo Implementarlo**:

    ```python
    class MiClase:
        def __init__(self, valor):
            self.valor = valor

        def __bool__(self):
            return bool(self.valor)
    ```

* **Errores Comunes**:
  * Proporcionar una conversión que no tenga sentido para el objeto.
