class A:
    def hablar(self):
        print('Hola desde A')

class F:
    def hablar(self):
        print('Hola desde F')

class B(A):
    pass

class C(F):
    def hablar(self):
        print('Hola desde C')

class D(B,C):
    pass

d = D()

d.hablar()

print(D.__mro__)
print(D.mro())

print(type(D.__mro__))
print(type(D.mro()))

mro = D.mro()

contador = 0
for i in mro:
    contador += 1
    print(contador, i)