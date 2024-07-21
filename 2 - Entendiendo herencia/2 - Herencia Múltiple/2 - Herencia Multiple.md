# Herencia Múltiple

La herencia múltiple es una característica de algunos lenguajes de programación orientados a objetos, que permite que una clase herede atributos y métodos de más de una clase base. Esta característica proporciona una gran flexibilidad, aunque también puede llevar a complicaciones como el problema del "diamante" en la resolución de métodos.

## Ejemplo de Herencia Múltiple

A continuación se presenta un ejemplo que demuestra cómo se puede implementar la herencia múltiple en Python.

### Clases Base

Primero, definimos dos clases base: `Persona` y `Artista`.

```python
class Persona:
    def __init__(self, nombre, edad, nacionalidad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        self.sexo = sexo

    def presentarse(self):
        mensaje = f'Hola, mi nombre es {self.nombre}, tengo {self.edad} años, soy {self.nacionalidad} y soy {self.sexo}'
        return print(mensaje)

class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad

    def mostrar_habilidad(self):
        hab = f'Mi habilidad es: {self.habilidad}'
        return print(hab)
```

### Clase Derivada con Herencia Múltiple

Luego, definimos una clase `EmpleadoArtista` que hereda de ambas clases `Persona` y `Artista`.

```python
class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        Persona.__init__(self, nombre, edad, nacionalidad, None)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa

    def presentarse(self):
        return super().mostrar_habilidad()
```

>[!TIP]
>`Super()` busca el método de la clase padre.

#### ¿Por qué no se usa `super()` en el constructor (`__init__`) de `EmpleadoArtista`?

En el constructor de `EmpleadoArtista`, se llama explícitamente a los constructores de `Persona` y `Artista` usando `Clase.__init__(self, ...)` en lugar de `super().__init__()`. Esto se hace para asegurarse de que ambos constructores sean llamados y sus atributos inicializados correctamente, ya que `super()` solo llamaría al siguiente constructor en la cadena de herencia según el MRO (Method Resolution Order), lo cual no es suficiente en herencia múltiple directa.

#### ¿Qué significa el uso de `super()`?

`super()` es una función que se utiliza para llamar a un método de una superclase. En Python, `super()` se usa comúnmente para llamar a métodos de una clase base dentro de una clase derivada. `super()` toma dos argumentos: la clase actual y un objeto que es una instancia de esa clase.

```python
super(SubClass, self).method()
```

### Método `presentarse`

En el método `presentarse` de `EmpleadoArtista`, se usa `super().mostrar_habilidad()` para llamar al método `mostrar_habilidad` de la clase base más a la izquierda en la lista de herencia (en este caso, `Artista`).

```python
def presentarse(self):
    return super().mostrar_habilidad()
```

Esto asegura que se llame al método `mostrar_habilidad` de la primera clase base en la lista de herencia (en este caso, `Artista`).

## Instanciando un Objeto y Probando la Herencia Múltiple

```python
james = EmpleadoArtista('James', 29, 'chileno', 'Guitarrista', 2500, 'Google')

herencia = issubclass(EmpleadoArtista, Artista)
instancia = isinstance(james, EmpleadoArtista)

print(herencia)
print(instancia)

james.presentarse()
```

### Desglose del Código

* **Clase `Persona`**: Define atributos como `nombre`, `edad`, `nacionalidad`, y `sexo`, y un método `presentarse` que imprime una presentación del objeto.

* **Clase `Artista`**: Define el atributo `habilidad` y un método `mostrar_habilidad` que imprime la habilidad del artista.

* **Clase `EmpleadoArtista`**: Hereda de `Persona` y `Artista`. Su constructor inicializa atributos de ambas clases base y define métodos `mostrar_habilidad` y `presentarse` que sobrescriben los métodos de las clases base.

>[!TIP]
>
> * `issubclass(EmpleadoArtista, Artista)` devuelve `True`, lo que confirma que `EmpleadoArtista` es una subclase de `Artista`.
>
> * `isinstance(james, EmpleadoArtista)` también devuelve `True`, confirmando que `james` es una instancia de `EmpleadoArtista`.
