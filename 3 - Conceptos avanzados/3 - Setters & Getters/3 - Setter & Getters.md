# Setter & Getters

## ¿Que son?

Los **setters** y **getters** son métodos utilizados en programación orientada a objetos para acceder y modificar los valores de los atributos privados de una clase. Aquí tienes una breve explicación:

- **Getters**: Son métodos que permiten obtener el valor de un atributo privado. Suelen tener el prefijo `get` seguido del nombre del atributo. Por ejemplo, si tienes un atributo `nombre`, el getter sería `get_nombre()`.
- **Setters**: Son métodos que permiten modificar el valor de un atributo privado. Suelen tener el prefijo `set` seguido del nombre del atributo. Por ejemplo, si tienes un atributo `nombre`, el setter sería `set_nombre('ejemplo')`.

Estos métodos ayudan a mantener el principio de encapsulamiento, permitiendo controlar cómo se accede y se modifica el estado interno de un objeto.

### Ejemplo

Se crea la clase persona atributos privados, además se crean dos métodos llamados `get_nombre` para mostrar el nombre y `set_nombre` para cambiar el nombre.

```py
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self._edad = edad

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, new_name):
        self.__nombre = new_name
        return self.__nombre

# Instanciando objeto
persona1 = Persona('James', 29)
# Mostrando el atributo privado con un método getter
print(persona1.get_nombre()) # output: James

# Intentando cambiar el atributo privado de manera "normal"
persona1.__nombre = 'María'
print(persona1.get_nombre()) # output: James

# Cambiando el atributo privado con un método setter
persona1.set_nombre('Ikigai')
print(persona1.get_nombre()) # output: Ikigai
```
