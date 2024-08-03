class Perro:
    def hablar(self):
        return "Guau"

class Gato:
    def hablar(self):
        return "Miau"

def hacer_hablar(animal):
    return animal.hablar()

perro = Perro()
gato = Gato()

print(gato.hablar())
print(perro.hablar())

print(hacer_hablar(gato))
print(hacer_hablar(perro))