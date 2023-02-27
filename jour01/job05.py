class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Affiche X et Y
    def affichersLesPoints(self):
        return print("x =", self.x, "y =", self.y)

    # Affiche seulement X
    def afficherX(self):
        return print("x =", self.x)

    # Affiche seulement Y
    def afficherY(self):
        return print("y =", self.y)

    # Permet de changer la valeur de X
    def changerX(self, x):
        self.x = x

    # Permet de changer la valeur de Y
    def changerY(self, y):
        self.y = y


point = Point(120, 100)
point.affichersLesPoints()

point.afficherX()
point.afficherY()

point.changerX(20), point.changerY(10)
point.affichersLesPoints()
