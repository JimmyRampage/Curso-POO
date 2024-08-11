# class Ave:
#     def volar(self):
#         return 'Estoy volando'

# class Pinguino(Pajaro):
#     def volar(self):
#         return 'No puedo volar'

# def hacer_volar(ave = Ave):

# Clase para compartir todo lo que las aves tienen en común
class Ave:
    def comer(self):
        return "Esta ave está comiendo"

# Se aplica el principio, para agregar funcionalidades a una clase diferente (subclase)
class AveVoladora(Ave):
    def volar(self):
        return 'Volando'

# Nuevamente se aplica el principio gracias a otro tipo de aves
class AveNoVoladora(Ave):
    pass

def hacer_comer(ave):
    print(ave.comer())

def hacer_volar(ave):
    if isinstance(ave, AveVoladora):
        print(ave.volar())
    else:
        print("Esta ave no puede volar")

paloma = AveVoladora()
pinguino = AveNoVoladora()

hacer_comer(paloma)  # Salida: "Esta ave está comiendo"
hacer_comer(pinguino)  # Salida: "Esta ave está comiendo"

hacer_volar(paloma)   # Salida: "Volando"
hacer_volar(pinguino) # Salida: "Esta ave no puede volar"