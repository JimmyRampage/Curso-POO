# Que son las clases y los objetos

En la programación orientada a objetos (POO) en Python, las clases y los objetos son dos conceptos fundamentales:

* **Clase**: Una clase es como un plano o plantilla para crear objetos. Define un conjunto de atributos que caracterizarán cualquier objeto que sea fabricado a partir de la clase. Los atributos son datos miembros (variables de clase y variables de instancia) y métodos, accesados vía notación de punto.

* **Objeto**: Un objeto es una instancia de una clase. Cuando se define una clase, no se asigna memoria para sus atributos. Pero cuando se crea el objeto, se asigna un espacio de memoria para esa variable.

## Creando una clase

Se utiliza la palabra reservada `class`, seguido del nombre de la clase que, por convención los nombres de las clases siempre se utiliza PascalCase

[PEP8 | Class Names](https://pep8.org/#class-names)

### Primera Clase

```py
class Celular():
    marca = 'Samsung'
    modelo = 'S23'
    camera = '48MP'
```

>[!IMPORTANT]
>Esta primera clase de nombre `Celular()` tiene atributos estáticos, eso quiere decir que siempre serán los mismos valores
>
>Esto quiere decir que cada vez que yo instancie un objeto `Celular()`, este tendrá la misma marca, mismo modelo y misma cámara.

#### Instanciando un objeto

Cuando hablamos de instanciar nos referimos a crear un objeto desde una clase.

```py
celular1 = Celular()
print(celular1)
```

##### Resultado de la instancia

```py
<__main__.Celular object at 0x1030c7310>
```

>[!NOTE]
>`__main__` hace referencia al modulo que esta ejecutándose. `Celular` nos dice que es el nombre de la clase, y luego nos responde que es un objeto y el lugar en la memoria ram en que es almacenado. (Al terminar el programa esto se elimina).

#### Mostrando sus propiedades

```py
print(celular1.marca)
print(celular1.modelo)
print(celular1.camera)
```

##### Resultado de las propiedades

```py
'Samsung'
'S23'
'48MP'
```
