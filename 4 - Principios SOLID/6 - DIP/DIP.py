# class Dictcionario:
#     def verificar_palabra(self, palabra):
#         # Lógica para verificar palabras
#         pass

# class CorrectorOrtografico:
#     def __init__(self) -> None:
#         self.diccionario = Dictcionario()

#     def corregir_texto(self, texto):
#         # Usamos el diccionario para corregir el texto
#         pass

from abc import ABC, abstractmethod

class VerificadorOrtografico(ABC):
    @abstractmethod
    def verificador_palabra(self, palabra):
        pass

class Diccionario(VerificadorOrtografico):
    def verificador_palabra(self, palabra):
        # Lógica para verificar palabras si está en el diccionario
        pass

class ApiVerificadorOrtografico(VerificadorOrtografico):
    def verificador_palabra(self, palabra):
        # Lógica para verificar palabras usando una API externa
        pass

class CorrectorOrtografico:
    def __init__(self, verificador):
        self.verificador = verificador

    def corregir_texto(self, texto):
        #Usamos el verificador para corregir el texto
        pass


verificador_api = ApiVerificadorOrtografico()
corrector = CorrectorOrtografico(verificador_api)