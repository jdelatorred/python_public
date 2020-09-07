class Carta:
    def __init__(self, palo=0, valor=0):
        self.palo = palo
        self.valor = valor
    listaDePalos = ["Treeboles", "Diamantes", "Corazones", "Picas"]

    listaDeValores = ["nada", "As", "2", "3", "4", "5", "6", "7", "8", "9",
         "10", "Sota", "Reina", "Rey"]


    def __str__(self):
        return (self.listaDeValores[self.valor] + " de " +
        self.listaDePalos[self.palo])


    def __cmp__(self, otro):
        # controlar el palo
        if self.palo > otro.palo:
            return 1
        if self.palo < otro.palo:
            return -1
        # si son del mismo palo, controlar el valor
        if self.valor > otro.valor:
            return 1
        if self.valor < otro.valor:
            return -1
        # los valores son iguales, es un empate
        return 0

carta1 = Carta(1, 11)

print(carta1)

carta2 = Carta(1, 3)

print(carta2)
