class Cola:
    def __init__(self):
        self.longitud = 0
        self.cabeza = None

    def estaVacia(self):
        return (self.longitud == 0)

    def inserta(self, carga):
        nodo = Nodo(carga)
        nodo.siguiente = None
        if self.cabeza == None:
            # si la lista est¶a vac¶³a el nuevo nodo va el primero
            self.cabeza = nodo
        else:
            # encuentra el ¶ultimo nodo de la lista
            ultimo = self.cabeza
            while ultimo.siguiente: ultimo = ultimo.siguiente
            # a~nadir el nuevo nodo
            ultimo.siguiente = nodo
        self.longitud = self.longitud + 1

    def quita(self):
        carga = self.cabeza.carga
        self.cabeza = self.cabeza.siguiente
        self.longitud = self.longitud - 1
        return carga
