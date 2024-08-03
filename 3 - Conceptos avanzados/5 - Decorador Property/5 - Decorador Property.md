# Decoradir `@property`

## ¿Qué es `@property`?

El decorador @property en Python se utiliza para definir métodos que actúan como atributos de una clase. Esto permite acceder a los métodos como si fueran atributos, lo que mejora la legibilidad y el encapsulamiento del código. Aquí tienes una explicación detallada:

@property convierte un método en una propiedad de una clase. Esto significa que puedes acceder al método como si fuera un atributo, sin necesidad de usar paréntesis.

## ¿Cómo se usa?

El decorador @property se aplica a un método sin parámetros, convirtiéndolo en un atributo de solo lectura. Para permitir la escritura y la eliminación del atributo, se utilizan los decoradores @<property_name>.setter y @<property_name>.deleter respectivamente.

Aquí tienes un ejemplo básico:

```py
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, new_name):
        self.__nombre = new_name
        return self.__nombre

    @nombre.deleter
    def nombre(self):
        del self.__nombre

# Instanciando objeto
persona1 = Persona('James', 29)

# Mostrando el atributo privado con la propiedad (ex-método) getter
print(persona1.nombre) # output: James

# Intentando cambiar el atributo privado de manera "normal"
persona1.__nombre = 'María'
print(persona1.nombre) # output: James

# Cambiando el atributo privado con un método setter
persona1.nombre = 'Ikigai'
print(persona1.nombre) # output: Ikigai

# Eliminar el nombre usando el deleter
del persona1.nombre
```

## Beneficios de usar @property

* Encapsulación: Permite ocultar detalles de implementación y proporcionar una interfaz pública controlada.

* Interfaz limpia: Acceso a métodos como si fueran atributos.

* Validación y control: Añade lógica de validación o transformación cuando se accede o modifica un atributo.

* Compatibilidad: Permite cambiar la implementación interna sin modificar la interfaz pública.
