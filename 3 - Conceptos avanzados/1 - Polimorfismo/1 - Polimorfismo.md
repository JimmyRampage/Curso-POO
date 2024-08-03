# ¿Que es polimorfismo?

El polimorfismo es un concepto fundamental en POO que permite que una sola interfaz pueda ser utilizada para diferentes tipos de datos. En Python, el polimorfismo se refiere a la capacidad de diferentes clases de responder a la misma llamada de método de maneras específicas para cada clase.

## Características del Polimorfismo

1. **Métodos Sobrecargados**: Los métodos con el mismo nombre pueden ser definidos en diferentes clases. Cada clase puede implementar este método de manera diferente.
2. **Interfaz Común**: Diferentes clases pueden implementar la misma interfaz, lo que permite a los objetos de estas clases ser utilizados de manera intercambiable.
3. **Flexibilidad y Extensibilidad**: Permite escribir código más flexible y extensible, ya que los objetos pueden ser procesados sin conocer su tipo exacto de antemano.

## Ejemplos de Polimorfismo en Python

### Ejemplo 1: Polimorfismo con Métodos

#### Opción 1

Aquí tenemos dos clases, `Perro` y `Gato`, que implementan el mismo método `hablar`.

En estas dos opciones, el mismo método `hablar` se comporta de manera diferente según el objeto que lo invoque.

```py
class Perro:
    def hablar(self):
        return "Guau"

class Gato:
    def hablar(self):
        return "Miau"

perro = Perro()
gato = Gato()

print(gato.hablar()) # Miau
print(perro.hablar()) # Guau
```

#### Opción 2

```py
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

print(hacer_hablar(gato))
print(hacer_hablar(perro))
```

### Ejemplo 2: Polimorfismo con Herencia

El polimorfismo también se puede lograr mediante herencia, donde una clase base define un método que es sobrescrito por las clases derivadas.

```py
class Animal:
    def hablar(self):
        pass

class Perro(Animal):
    def hablar(self):
        return "Guau"

class Gato(Animal):
    def hablar(self):
        return "Miau"

def hacer_hablar(animal):
    print(animal.hablar())

# Crear instancias de las clases derivadas
perro = Perro()
gato = Gato()

# Llamar al método hacer_hablar
hacer_hablar(perro)  # Guau
hacer_hablar(gato)   # Miau
```

En este caso, `Perro` y `Gato` heredan de `Animal` y sobrescriben el método `hablar`.

### Ejemplo 3: Polimorfismo con Operadores

El polimorfismo también se puede observar con operadores. Por ejemplo, el operador `+` se comporta de manera diferente dependiendo del tipo de operandos:

```py
# Polimorfismo con números
print(3 + 5)  # 8

# Polimorfismo con cadenas
print("Hola" + " Mundo")  # Hola Mundo

# Polimorfismo con listas
print([1, 2, 3] + [4, 5, 6])  # [1, 2, 3, 4, 5, 6]
```

## Beneficios del Polimorfismo

* **Reutilización del Código**: Los mismos métodos pueden ser reutilizados para diferentes tipos de objetos.
* **Flexibilidad**: Los programas se vuelven más flexibles y fáciles de extender y mantener.
* **Intercambiabilidad**: Permite el uso de diferentes objetos de manera intercambiable sin cambiar el código que los utiliza.
