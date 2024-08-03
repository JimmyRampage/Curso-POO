# ¿Que son los atributos?

Los atributos en la Programación Orientada a Objetos son variables que se definen dentro de una clase. Estos atributos representan el estado o las características de un objeto de esa clase.

Por ejemplo, si tenemos una clase `Celular`, los atributos podrían ser `color`, `marca`, `modelo`, etc. Cada objeto o instancia de la clase `Celular` tendrá sus propios valores para estos atributos.

## Función inicial

¿Que ocurre si nosotros queremos definir el contenido de las variables al momento de instanciar un objeto?

Esto se resuelve con una función inicial (o método constructor) `__init__(self):`.

>[!NOTE]
>`self` Mientras use self dentro de un método puedo modificar los valores de sus atributos.

```py
class Celular:
    def __init__(self, marca, modelo, camera):
        self.marca = marca
        self.modelo = modelo
        self.camera = camera
```

Esta función se ejecuta automáticamente al instanciar un objeto, y registra los parámetros entregados en las variables (atributos).

>[!NOTE]
>El parámetro self no se pasa al llamar al método; es agregado automáticamente por Python y se refiere a la instancia que se está creando.

### Instanciando un objeto

```py
cel1 = Celular('Apple', 'iPhone 15', '48MP')
cel2 = Celular('Samsung', 'S23', '48MP')
```

### Mostrando en pantalla

```py
print(cel1.marca)
print(cel2.modelo)
```

```py
Apple
S23
```

## Atributos de clase o estáticos vs. atributos de instancia

Es importante distinguir entre atributos de clase y atributos de instancia:

* **Atributos de clase o estáticos**: Son compartidos por todas las instancias de la clase. Se definen directamente dentro de la clase y fuera de cualquier método. En algunos lenguajes de programación, los atributos estáticos son sinónimos de los atributos de clase. Sin embargo, en otros lenguajes, los atributos estáticos pueden tener un comportamiento ligeramente diferente, como ser accesibles sin necesidad de crear una instancia de la clase.

* **Atributos de instancia**: Son específicos de cada instancia de la clase. Se definen dentro del método `__init__` usando self.

```py
class Celular:
    categoria = 'Electrónica'

    def __init__(self, marca, modelo, camera):
        self.marca = marca
        self.modelo = modelo
        self.camera = camera

print(Celular.categoria)

cel1 = Celular('Apple', 'iPhone 15', '48MP')
cel2 = Celular('Samsung', 'S23', '48MP')
print(cel1.marca)
print(cel2.modelo)
```

>[!IMPORTANT]
>Modificar un atributo de clase afecta a todas las instancias de esa clase, mientras que modificar un atributo de instancia solo afecta a esa instancia específica.
