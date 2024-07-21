# ¿Que son los métodos?

Los métodos en POO son funciones que se definen dentro de una clase. Estos métodos representan las acciones y/o comportamientos que un objeto de esa clase puede realizar.

Por ejemplo, si tenemos una clase `Celular`, los métodos podrían ser `llamar()`, `cortar()`, `navegar()`, etc. Cada objeto de la clase Celular puede realizar estas acciones.

## Creando un método

```py
class Celular:
    def __init__(self, marca, modelo, camera):
        self.marca = marca
        self.modelo = modelo
        self.camera = camera
    def llamar(self):
        print(f'Estas llamando desde un {self.modelo}...')
    def cortar(self):
        print(f'Terminaste la llamada desde un {self.modelo}...')
```

### Desglose del método `llamar()`

```py
def llamar(self):
    print(f'Estas llamando desde un {self.modelo}...')
```

>[!NOTE]
>Así como se ve, es una función, pero al estar dentro de una clase, ya sabemos que pasa a llamarse método.

Este método tiene un parámetro '**obligatorio**' `self`, porque es la forma en que el python hace referencia al objeto mismo que esta ejecutando el método.

El parámetro `self` es una convención en Python. Es el primer parámetro que se pasa a cualquier método de instancia. Python pasará automáticamente el objeto que está invocando el método al parámetro `self`. Por lo tanto, `self` es una referencia al objeto de la clase que está invocando el método. Esto permite que el método acceda a los atributos y otros métodos del objeto.

En este caso, `self.modelo` se refiere al atributo `modelo` del objeto que está invocando el método `llamar()`. Entonces, si tienes un objeto `cel1` de una clase `Celular` con un atributo modelo, y llamas a `cel1.llamar()`.

```py
cel1 = Celular('Apple', 'iPhone 15', '48MP')
cel2 = Celular('Samsung', 'S23', '48MP')

cel1.llamar()
cel1.cortar()
```

```py
Estas llamando desde un iPhone 15...
Terminaste la llamada desde un iPhone 15...
```
