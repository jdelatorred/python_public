lista = ["hola", 2.0, 5, [10, 20]]

print(lista)

print

print(len(lista))

print

print("hola" in lista)

print

a = [1, 2, 3]
b = [5, 6, 7]
c = a + b
print c

print

#imprime porcion
print c[3:]

print

#imprime porcion
print c[3:5]

print

lista[0] = "Cambio"

print lista

print

del lista[1:3]

print lista

print

#Copiar una lista con operador porcion
a = [1, 2, 3]
b = []
b[:] = a[:]

print b

