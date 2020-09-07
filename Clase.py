class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    def __add__(self, otro):
        return Punto(self.x + otro.x, self.y + otro.y)


punto = Punto(1, 2)

print(punto.x)
print(punto.y)
print(punto.__str__())
print(str(punto))

punto = Punto()

print(punto.x)
print(punto.y)
print(punto.__str__())

print(str(punto))
