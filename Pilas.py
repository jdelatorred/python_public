class Pila :
    def __init__(self) :
        self.elementos = []
    def push(self, elemento) :
        self.elementos.append(elemento)
    def pop(self) :
        return self.elementos.pop()
    def isEmpty(self) :
        return (self.elementos == [])






s = Pila()
s.push(54)
s.push(45)
s.push("+")

while not s.isEmpty() :
    print(s.pop())
