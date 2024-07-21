# ¿Que es la herencia?

La herencia es un principio fundamental de la programación orientada a objetos, permite definir una clase que hereda todos los métodos y propiedades de otra clase. La clase de la que se hereda se llama **clase base** o `clase padre`, y la clase que hereda se llama **clase derivada** o `clase hija`.

La herencia permite la reutilización de código, ya que puedes crear una `clase hija` que incluya métodos y propiedades de la **clase padre**, y luego añadir nuevos métodos y propiedades específicos de la **clase hija**.

## Creando una clase

¿Porque querríamos heredar atributos y métodos de una clase a otra?

Supongamos que queremos crear 3 clases, Persona, Empleado y Estudiante.

Para este caso, las 3 clases comparten atributos en común como, el nombre, la edad, la nacionalidad, el sexo, etc...

Es por eso que heredar es tan practico.

### Clase `Persona`

```py
class Persona:
    def __init__(self, nombre, edad, nacionalidad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        self.sexo = sexo
    def presentarse(self):
        mensaje = f'Hola, mi nombre es {self.nombre}, tengo {self.edad} años, soy {self.nacionalidad} y soy {self.sexo}'
        return print(mensaje)
```

### Heredando de `Persona` a `Empleado`

```py
class Empleado(Persona):
    pass
```

Con esa linea de código, creamos una nueva clase llamada `Empleado` que heredo todo lo que contiene la clase `Persona`

#### Instanciando un `Empleado`

```py
empleado1 = Empleado('James',29,'chileno','Masculino')
empleado1.presentarse()
```

```py
Hola, mi nombre es James, tengo 29 años y soy chileno
```

### Heredando atributos y agregando nuevos

En Python, no puedes evitar que una subclase herede atributos de su superclase directamente, ya que la subclase hereda todos los atributos y métodos de la superclase. Sin embargo, puedes controlar qué atributos se usan o se exponen en la subclase. Si deseas no utilizar un atributo, simplemente no inicialices ese atributo en la subclase y no lo uses en los métodos de la subclase.

Utilizamos el constructor `__init__()` en el cual se escriben todos los atributos que queremos utilizar en `Empleado` y agregamos los nuevos que son de nuestro interés, como `cargo` y `salario`.

Luego utilizamos el constructor `super()` dentro de `__init__` para definir cuales son los atributos que vamos a heredar.

>[!TIP]
>Podemos inicializar los parámetros que no vamos a utilizar con `None`. Es importante tener claridad sobre la ubicación de los parámetros que no utilizaremos.

Para finalizar, agregamos el o los atributos nuevos `self.atributo = atributo`

>[!NOTE]
>En empleado no utilizaremos el atributo `sexo` que heredamos de `Persona`

```py
class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, cargo, salario):
        super().__init__(nombre, edad, nacionalidad, None)
        self.cargo = cargo
        self.salario = salario
```
