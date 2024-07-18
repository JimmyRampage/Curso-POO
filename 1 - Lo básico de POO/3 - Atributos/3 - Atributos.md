# ¿Que son los atributos?

Los atributos en la Programación Orientada a Objetos (POO) en Python son variables que se definen dentro de una clase. Estos atributos representan el estado o las características de un objeto de esa clase.

Por ejemplo, si tenemos una clase `Celular`, los atributos podrían ser `color`, `marca`, `modelo`, etc. Cada objeto o instancia de la clase `Celular` tendrá sus propios valores para estos atributos.

## Función inicial

¿Que ocurre si nosotros queremos definir el contenido de las variables al momento de instanciar un objeto?

Esto se resuelve con una función inicial (o método constructor) `def __init__(self):`.

```py
class Celular:
    def __init__(self, marca, modelo, camera):
        self.marca = marca
        self.modelo = modelo
        self.camera = camera
```

Esta función se ejecuta automáticamente al instanciar un objeto, y registra los parámetros entregados en las variables (atributos).

>[!NOTE]
>El parámetro `self` no se entrega

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
