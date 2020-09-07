import math
import statistics
from functools import reduce

def area(r):
    ''' Area of cicle with radius r'''
    return math.pi * (r**2)

radii = [2, 5, 7.1, 0.3, 10]

#Method 1 direct and traditional
areas = []
for r in radii:
    a = area(r)
    areas.append(a)

areas

#Method 2 MAP function
list(map(area, radii))

temps = [("Berlin", 29), ("Cairo", 36), ("Buenos Aires", 19), ("Los Angeles", 26), ("Tokyo", 27), ("New York", 82.4), ("London", 22), ("Beijing", 32)]

c_to_f = lambda data: (data[0], (9/5)*data[1] + 32)

list(map(c_to_f, temps))
print(list(map(c_to_f, temps)))

#usemos la funcion filter para devolver sobre una lista los elementos que son mayores del promedio
data = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
avg = statistics.mean(data)
print(avg)
print(list(filter(lambda x: x > avg, data)))

#usemos la funcion filter para remover elementos perdidos
countries = ["", "Argentina", "", "Brazil", "Chile", "Colombia", "", "Ecuador", "", "", "Venezuela"]
print(list(filter(None,countries)))

#usemos la funcion reduce para ejecutar iterativamente una funcion sobre una lista
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
multiplier = lambda x, y: x*y
print(reduce(multiplier, primes))