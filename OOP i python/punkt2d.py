from math import sqrt


class Punkt2D:  # definition af klasse
    def __init__(self, x, y, navn):  # konstruktør
        self.x = x  # attribut
        self.y = y  # attribut
        self.afstand = sqrt(self.x ** 2 + self.y ** 2)
        self.navn = navn

    def udskriv_koordinater(self):  # metode
        print("x-koordinatet er:", self.x)
        print("y-koordinatet er:", self.y)

    def afstand_til_origo(self):  # metode
        return sqrt(self.x ** 2 + self.y ** 2)
    
    def print_afstand_til_origo(self):
        print("Afstanden til origo er ", self.afstand_til_origo())


# Test
punkt = Punkt2D(3, 4,"Mit punkt")  # objekt oprettes (instantiering)
print(punkt.afstand)
punkt.udskriv_koordinater()  # metode til objekt kaldes
punkt.print_afstand_til_origo()
print(punkt.afstand_til_origo())  # metode til objekt kaldes
