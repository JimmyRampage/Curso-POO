# Que es POO

Es un paradigma de programación que utiliza objetos y representa cosas de la vida real y sus interacciones.

En POO, los objetos son instancias de clases, algo así como la "creación" del objeto a partir de una clase. Una clase actúa como un molde que define las propiedades (atributos) y las acciones (métodos) que sus objetos pueden tener.

>[!TIP]
>En definitiva, la Programación Orientada a Objetos (POO) es una metodología que imita el comportamiento de los objetos en la vida real, los cuales tienen características (atributos) y realizan acciones (métodos).

La POO se centra en el encapsulamiento, la herencia y el polimorfismo, que facilitan la reutilización del código, la abstracción y la modularidad.

1. **Encapsulamiento**: Agrupa datos y métodos que operan sobre esos datos dentro de una misma unidad (la clase). Esto permite ocultar los detalles internos de implementación y proteger la integridad de los datos.

2. **Herencia**: Permite crear nuevas clases basadas en clases existentes. Las nuevas clases heredan atributos y métodos de las clases base, lo que fomenta la reutilización del código y la creación de jerarquías de clases.

3. **Polimorfismo**: Permite que diferentes clases puedan ser tratadas de la misma manera a través de una interfaz común. Esto facilita la flexibilidad y la capacidad de extender sistemas sin modificar su código existente.

4. **Abstracción**: Permite definir la interfaz de objetos sin especificar los detalles de implementación. Esto ayuda a simplificar el diseño y a centrarse en lo esencial.

## ¿Que pasa si no uso POO?

Imaginemos que tenemos una fabrica de celulares y queremos crear diferentes marcas y modelos. Normalmente esto se haría de la siguiente manera:

```py
celular1_marca = 'Samsung'
celular2_marca = 'Apple'
celular3_marca = 'Huawei'

celular1_modelo = 'S23'
celular2_modelo = 'iPhone 15 Pro'
celular3_modelo = 'P20 pro'

celular1_camT = '48MP'
celular2_camT = '48MP'
celular3_camT = '12MP'

celular1_camF = '24MP'
celular2_camF = '20MP'
celular3_camF = '8MP'
```

> Pero esto no es óptimo, es tedioso y propenso a errores, ya que cada celular requiere un conjunto separado de variables.

Otra alternativa podría ser con matrices:

```py
celulares = []
celulares.append(['Samsung', 'S23', '48MP', '24MP'])
celulares.append(['Apple', 'iPhone 15 Pro', '48MP', '20MP'])
celulares.append(['Huawei', 'P20 Pro', '12MP', '8MP'])

```

> Aunque esto es mejor, sigue siendo poco óptimo, difícil de mantener y menos intuitivo al manejar atributos específicos de cada celular.

Estos problemas se solucionan de manera eficiente con la Programación Orientada a Objetos:

```py
class Celular:
    def __init__(self, marca, modelo, camT, camF):
        self.marca = marca
        self.modelo = modelo
        self.camT = camT
        self.camF = camF
    def mostrar_info(self):
        return f'{self.marca} {self.modelo} - Cámara trasera: {self.camT}, Cámara frontal: {self.camF}'

celular1 = Celular('Samsung', 'S23', '48MP', '24MP')
celular2 = Celular('Apple', 'iPhone 15 Pro', '48MP', '20MP')
celular3 = Celular('Huawei', 'P20 Pro', '12MP', '8MP')

print(celular1.mostrar_info())
print(celular2.mostrar_info())
print(celular3.mostrar_info())
```

>Con POO, se encapsulan los atributos y métodos relacionados en una clase. Esto hace que el código sea más modular, reutilizable y fácil de mantener.
