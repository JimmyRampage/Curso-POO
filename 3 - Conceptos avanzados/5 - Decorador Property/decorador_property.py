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