from math import sqrt
from punkt2d import Punkt2D  # Punkt2D ligger punkt2d.py


class LinjeSegment:
    def __init__(self, punkt_1, punkt_2):  # Konstruktør
        self.endepunkt_1 = punkt_1
        self.endepunkt_2 = punkt_2
        self.beregn_længde()

    def beregn_længde(self):
        x_afstand = self.endepunkt_1.x - self.endepunkt_2.x
        y_afstand = self.endepunkt_1.y - self.endepunkt_2.y
        self.længde = sqrt((x_afstand) ** 2 + (y_afstand) ** 2)

    def endepunkt(self):
        print(self.endepunkt_1)

# Test
p1 = Punkt2D(1, 2, 'hej')
p2 = Punkt2D(4, 6, 'mopo')
ls = LinjeSegment(p1, p2)
ls.endepunkt()
