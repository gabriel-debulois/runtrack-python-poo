class Rectangle:
    def __init__(self, longeur=10, largeur=5):
        self.__longeur = longeur
        self.__largeur = largeur

    def afficher(self):
        print("longeur =",self.__longeur,"largeur =",self.__largeur)

    def changerValeur(self, longeur, largeur):
        self.__longeur = longeur
        self.__largeur = largeur


rectangle = Rectangle()
rectangle.afficher()
rectangle.changerValeur(20, 10)
rectangle.afficher()