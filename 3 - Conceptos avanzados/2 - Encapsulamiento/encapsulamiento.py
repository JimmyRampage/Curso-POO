class MiClase:
    def __init__(self):
        self._atributo_protegido = 'atributo protegido con un underscore'
        self.__atributo_privado = 'atributo muy privado con doble underscore'

objeto = MiClase()
print(objeto._atributo_protegido)
print(objeto.__atributo_privado)
