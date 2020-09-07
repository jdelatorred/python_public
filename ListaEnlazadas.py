class Nodo:
    def __init__(self, carga=None, siguiente=None):
        self.carga = carga
        self.siguiente = siguiente
        def __str__(self):
            return str(self.carga)

def imprimeLista(nodo):
    print("[")
    while nodo:
        print(nodo.carga)
        nodo = nodo.siguiente
        print(",")
    print("]")

nodo1 = Nodo(1)
nodo2 = Nodo(2)
nodo3 = Nodo(3)


nodo1.siguiente = nodo2

nodo2.siguiente = nodo3

imprimeLista(nodo1)

imprimeLista(nodo2)

imprimeLista(nodo3)
