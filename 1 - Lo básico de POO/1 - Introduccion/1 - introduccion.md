# Que es POO

Es un paradigma de programación que utiliza objetos y representa cosas de la vida real y sus interacciones.

Los objetos son instancias de clases, que representan entidades con propiedades (atributos) y acciones (métodos).

La POO se centra en el encapsulamiento, la herencia y el polimorfismo, que facilitan la reutilización del código, la abstracción y la modularidad.

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

> Pero esto no es optimo,es tedioso trabajar con algo así.

Otra alternativa podría ser con matrices:

```py
celulares = []
celular1[0] = ['Samsung', 'S23', '48MP']
```

> Pero finalmente no es optimo tampoco.

Esto se soluciona con la Programación Orientada a Objetos
