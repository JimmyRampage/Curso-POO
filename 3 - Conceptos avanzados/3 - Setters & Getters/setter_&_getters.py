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